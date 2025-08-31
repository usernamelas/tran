#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY TAG RESTORER v3.2
- Colorful UI with proper width
- Creator credit
- Better language switching
- Fixed frame length
"""

import os
import re
import time
from datetime import datetime

# ============== CONFIG ==============
LANGUAGE = "ID"  # "ID" or "EN"
# ====================================

# Color Codes
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

# UI Settings
BOX_WIDTH = 40
CREATOR = "By YourName"  # Ganti dengan nama Anda

def color_text(text, color):
    """Add color to text"""
    return f"{COLORS[color]}{text}{COLORS['reset']}"

def draw_box(title, content="", color="blue"):
    """Draw colored box with title"""
    border = color_text("╔" + "═" * (BOX_WIDTH-2) + "╗", color)
    title_line = color_text("║ ", color) + color_text(title.center(BOX_WIDTH-4), "white") + color_text(" ║", color)
    bottom = color_text("╚" + "═" * (BOX_WIDTH-2) + "╝", color)
    
    print(border)
    print(title_line)
    
    if content:
        for line in content.split('\n'):
            line = line.ljust(BOX_WIDTH-4)
            print(color_text("║ ", color) + line + color_text(" ║", color))
    
    print(bottom)

# Language Strings
TEXTS = {
    "ID": {
        "title": "🛠️ PEMULIH TAG REN'PY 🛠️",
        "menu": [
            "1. Pulihkan File",
            "2. Change Language (ID)",
            "3. Keluar",
            f"\n{CREATOR} | {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        ],
        "file_select": "PILIH FILE .RPY:",
        "map_select": "PILIH MAPPING .TXT:",
        "output_prompt": "Nama file output:",
        "processing": "Memproses...",
        "success": "✅ BERHASIL!",
        "error": "❌ ERROR:",
        "no_files": "Tidak ada file %s ditemukan!",
        "enter_continue": "Tekan Enter untuk lanjut..."
    },
    "EN": {
        "title": "🛠️ REN'PY TAG RESTORER 🛠️",
        "menu": [
            "1. Restore File",
            "2. Change Language (EN)",
            "3. Exit",
            f"\n{CREATOR} | {datetime.now().strftime('%m/%d/%Y %I:%M %p')}"
        ],
        "file_select": "SELECT .RPY FILE:",
        "map_select": "SELECT MAPPING .TXT:",
        "output_prompt": "Output filename:",
        "processing": "Processing...",
        "success": "✅ SUCCESS!",
        "error": "❌ ERROR:",
        "no_files": "No %s files found!",
        "enter_continue": "Press Enter to continue..."
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_files(ext):
    """Get files with extension"""
    return [f for f in sorted(os.listdir()) if f.endswith(ext)]

def select_file(prompt, ext):
    """File selection menu"""
    files = get_files(ext)
    if not files:
        draw_box(TEXTS[LANGUAGE]["error"], TEXTS[LANGUAGE]["no_files"] % ext, "red")
        return None
    
    file_list = "\n".join(f"{i+1}. {f}" for i, f in enumerate(files))
    draw_box(prompt, file_list, "cyan")
    try:
        choice = int(input(color_text("> ", "yellow"))) - 1
        return files[choice]
    except (ValueError, IndexError):
        return None

def restore_file(rpy_file, map_file, out_file):
    """Restore tags from mapping"""
    try:
        # Load mapping
        tag_map = {}
        var_map = {}
        
        with open(map_file, 'r', encoding='utf-8') as f:
            section = None
            for line in f:
                line = line.strip()
                if "TAG" in line: section = "tag"
                elif "VARIABLE" in line: section = "var"
                elif line:
                    if section == "tag":
                        if match := re.match(r'\{(\d+)\} = \{(.+)\}', line):
                            tag_map[match.group(1)] = match.group(2)
                    elif section == "var":
                        if match := re.match(r'\[(\d+)\] = \[(.+)\]', line):
                            var_map[match.group(1)] = match.group(2)
        
        # Process file
        with open(rpy_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'\{(\d+)\}', lambda m: f"{{{tag_map.get(m.group(1), 'UNKNOWN_TAG')}}}", content)
        content = re.sub(r'\[(\d+)\]', lambda m: f"[{var_map.get(m.group(1), 'UNKNOWN_VAR')}]", content)
        
        # Save
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        result_msg = f"Input: {rpy_file}\nMapping: {map_file}\nOutput: {out_file}"
        draw_box(TEXTS[LANGUAGE]["success"], result_msg, "green")
    
    except Exception as e:
        draw_box(TEXTS[LANGUAGE]["error"], str(e), "red")

def main():
    global LANGUAGE
    while True:
        clear_screen()
        draw_box(TEXTS[LANGUAGE]["title"], color="magenta")
        
        # Main menu
        menu_text = "\n".join(TEXTS[LANGUAGE]["menu"])
        draw_box("MENU", menu_text, "blue")
        
        choice = input(color_text("> ", "yellow"))
        
        if choice == "1":
            # File selection
            rpy_file = select_file(TEXTS[LANGUAGE]["file_select"], ".rpy")
            if not rpy_file:
                input(color_text(TEXTS[LANGUAGE]["enter_continue"], "cyan"))
                continue
                
            map_file = select_file(TEXTS[LANGUAGE]["map_select"], ".txt")
            if not map_file:
                input(color_text(TEXTS[LANGUAGE]["enter_continue"], "cyan"))
                continue
            
            # Output name
            base_name = os.path.splitext(rpy_file)[0]
            prompt = f"{TEXTS[LANGUAGE]['output_prompt']} ({base_name}_restored.rpy)"
            print(color_text(prompt, "cyan"))
            out_name = input(color_text("> ", "yellow"))
            out_file = f"{out_name or base_name + '_restored'}.rpy"
            
            # Process
            print(color_text(TEXTS[LANGUAGE]["processing"], "yellow"))
            restore_file(rpy_file, map_file, out_file)
            input(color_text(TEXTS[LANGUAGE]["enter_continue"], "cyan"))
            
        elif choice == "2":
            LANGUAGE = "EN" if LANGUAGE == "ID" else "ID"
            print(color_text(f"Language changed to {LANGUAGE}", "green"))
            time.sleep(1)
            
        elif choice == "3":
            print(color_text("Goodbye! / Sampai jumpa!", "magenta"))
            break
            
        else:
            print(color_text("Invalid choice / Pilihan tidak valid", "red"))
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(color_text("\nOperation cancelled / Dibatalkan", "red"))
    except Exception as e:
        draw_box("CRITICAL ERROR", str(e), "red")