#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENHANCED REN'PY TAG RESTORER v2.0
Features:
- Interactive menu system
- Lists all .rpy files in directory
- Lists all .txt files for mapping
- Custom output filename
"""

import os
import re

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_files(extension):
    """Get all files with given extension in current directory"""
    return [f for f in os.listdir() if f.endswith(extension)]

def show_menu(title, items):
    """Display interactive menu"""
    clear_screen()
    print(f"\n=== {title} ===")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print(f"{len(items)+1}. Exit")
    
    while True:
        try:
            choice = int(input("\nSelect: "))
            if 1 <= choice <= len(items):
                return items[choice-1]
            elif choice == len(items)+1:
                return None
        except ValueError:
            print("Please enter a number")

def restore_tags(rpy_file, mapping_file, output_file):
    """Restore tags based on mapping"""
    # Load mappings
    tag_map = {}
    var_map = {}
    
    with open(mapping_file, 'r', encoding='utf-8') as f:
        current_section = None
        for line in f:
            line = line.strip()
            if line.startswith("==="):
                if "TAG" in line: current_section = "tag"
                elif "VARIABLE" in line: current_section = "var"
                continue
            
            if current_section == "tag":
                match = re.match(r'\{(\d+)\} = \{(.+)\}', line)
                if match:
                    tag_map[match.group(1)] = match.group(2)
            elif current_section == "var":
                match = re.match(r'\[(\d+)\] = \[(.+)\]', line)
                if match:
                    var_map[match.group(1)] = match.group(2)
    
    # Process file
    with open(rpy_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Restore tags
    content = re.sub(r'\{(\d+)\}', lambda m: f"{{{tag_map.get(m.group(1), 'UNKNOWN_TAG')}}}", content)
    content = re.sub(r'\[(\d+)\]', lambda m: f"[{var_map.get(m.group(1), 'UNKNOWN_VAR')}]", content)
    
    # Save output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Successfully restored {rpy_file}")
    print(f"🔖 Used mapping: {mapping_file}")
    print(f"💾 Saved as: {output_file}")

def main():
    while True:
        clear_screen()
        print("=== REN'PY TAG RESTORER ===")
        print("by_namelast")
        print("1. Restore File")
        print("2. Exit")
        
        choice = input("\nSelect option: ")
        
        if choice == '1':
            # Select RPY file
            rpy_files = get_files('.rpy')
            if not rpy_files:
                input("No .rpy files found. Press Enter to continue...")
                continue
                
            selected_rpy = show_menu("SELECT RPY FILE", rpy_files)
            if not selected_rpy:
                continue
                
            # Select mapping file
            txt_files = get_files('.txt')
            if not txt_files:
                input("No .txt mapping files found. Press Enter to continue...")
                continue
                
            selected_txt = show_menu("SELECT MAPPING FILE", txt_files)
            if not selected_txt:
                continue
                
            # Get output filename
            output_name = input("\nEnter output filename (without extension): ").strip()
            if not output_name:
                output_name = f"{os.path.splitext(selected_rpy)[0]}_restored"
            
            output_file = f"{output_name}.rpy"
            
            # Process file
            restore_tags(selected_rpy, selected_txt, output_file)
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            print("Goodbye!")
            print("by_namelast")
            break
            
        else:
            print("Invalid choice")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()