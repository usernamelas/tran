#!/usr/bin/env python3
"""
Script untuk scan semua file .rpy dan extract variabel-variabel yang ada
"""

import os
import re
import glob
from collections import defaultdict

def extract_variables_from_rpy_files(game_dir):
    """
    Scan semua file .rpy dalam direktori game dan extract variabel-variabel
    """
    variable_patterns = [
        r'\$(\w+)\s*=',          # $variable =
        r'default\s+(\w+)\s*=',  # default variable =
        r'define\s+(\w+)\s*=',   # define variable =
        r'(\w+)\s*=\s*[0-9"]',   # variable = value
    ]
    
    variables_found = defaultdict(list)
    
    # Cari semua file .rpy
    rpy_files = glob.glob(os.path.join(game_dir, "**/*.rpy"), recursive=True)
    
    print(f"Found {len(rpy_files)} .rpy files")
    
    for file_path in rpy_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                filename = os.path.basename(file_path)
                
                for pattern in variable_patterns:
                    matches = re.findall(pattern, content)
                    for var_name in matches:
                        # Filter out common false positives
                        if (len(var_name) > 2 and 
                            not var_name.startswith('_') and
                            var_name not in ['true', 'false', 'null', 'none']):
                            variables_found[var_name].append(filename)
                            
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return variables_found

def generate_monitor_code(variables_dict):
    """
    Generate kode monitor berdasarkan variabel yang ditemukan
    """
    # Kelompokkan variabel berdasarkan pola
    categories = {
        'relationships': [],
        'progress': [],
        'items': [],
        'flags': [],
        'time': [],
        'other': []
    }
    
    relationship_keywords = ['rel', 'affection', 'love', 'trust', 'like']
    progress_keywords = ['progress', 'level', 'stage', 'phase', 'convince']
    items_keywords = ['item', 'have', 'acquired', 'bought', 'own']
    time_keywords = ['day', 'time', 'hour', 'week', 'month']
    flag_keywords = ['flag', 'done', 'complete', 'finished', 'unlocked']
    
    for var_name in variables_dict.keys():
        var_lower = var_name.lower()
        
        if any(keyword in var_lower for keyword in relationship_keywords):
            categories['relationships'].append(var_name)
        elif any(keyword in var_lower for keyword in progress_keywords):
            categories['progress'].append(var_name)
        elif any(keyword in var_lower for keyword in items_keywords):
            categories['items'].append(var_name)
        elif any(keyword in var_lower for keyword in time_keywords):
            categories['time'].append(var_name)
        elif any(keyword in var_lower for keyword in flag_keywords):
            categories['flags'].append(var_name)
        else:
            categories['other'].append(var_name)
    
    # Generate kode Ren'Py
    code = """init python:
    def get_all_game_variables():
        \"\"\"Get semua variabel game yang terdeteksi\"\"\"
        vars_dict = {}
        all_vars = [\n"""
    
    # Tambahkan semua variabel
    all_vars = sorted(variables_dict.keys())
    for var in all_vars:
        code += f'            "{var}",\n'
    
    code += """        ]
        
        for var_name in all_vars:
            try:
                if hasattr(store, var_name):
                    vars_dict[var_name] = getattr(store, var_name)
                else:
                    vars_dict[var_name] = "NOT_FOUND"
            except Exception as e:
                vars_dict[var_name] = f"ERROR: {str(e)}"
        
        return vars_dict
    
    def create_comprehensive_report():
        \"\"\"Buat laporan lengkap dengan semua variabel\"\"\"
        variables = get_all_game_variables()
        
        # Group by category
        report = "=== COMPREHENSIVE GAME REPORT ===\\n\\n"
        \n"""
    
    # Generate kategori
    for category, vars_list in categories.items():
        if vars_list:
            code += f"""        # {category.upper()}
        report += "--- {category.upper()} ---\\n"
        for var in sorted({vars_list}):
            if var in variables:
                report += f"{{var}}: {{variables[var]}}\\n"
        report += "\\n"
        \n"""
    
    code += """        # Semua variabel lainnya
        report += "--- OTHER VARIABLES ---\\n"
        other_vars = sorted(set(variables.keys()) - set(all_categorized_vars))
        for var in other_vars:
            report += f"{var}: {variables[var]}\\n"
        
        # Save to file
        try:
            with open("game_variables_report.txt", "w", encoding="utf-8") as f:
                f.write(report)
            print("Report saved to game_variables_report.txt")
        except:
            print("Could not save report file")
            print(report)
        
        return report
"""
    
    return code

if __name__ == "__main__":
    # Ganti dengan path ke folder game Anda
    game_directory = "."  # Current directory
    
    print("Scanning for .rpy files...")
    variables = extract_variables_from_rpy_files(game_directory)
    
    print(f"\nFound {len(variables)} unique variables:")
    for i, var in enumerate(sorted(variables.keys())[:50]):  # Show first 50
        print(f"  {var}")
    
    if len(variables) > 50:
        print(f"  ... and {len(variables) - 50} more")
    
    # Generate dan save kode monitor
    monitor_code = generate_monitor_code(variables)
    with open("auto_generated_monitor.rpy", "w", encoding="utf-8") as f:
        f.write(monitor_code)
    
    print(f"\nGenerated monitor code saved to auto_generated_monitor.rpy")
    print("Copy the content to your game file or use include statement")