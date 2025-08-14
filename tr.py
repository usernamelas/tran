# Copyright (c) 2016 Jackmcbarn
# Modifications (c) 2023 [Your Name]

import os
import re
import json
import hashlib
from copy import copy
import subprocess

# Konfigurasi file
INPUT_FILE = "ujicoba.rpy"  # Ganti dengan nama file input Anda
OUTPUT_FILE = "ujicoba_id.rpy"  # File output
TARGET_LANG = "id"  # Kode bahasa Indonesia

class RpyTranslator:
    def __init__(self):
        self.translation_cache = {}
        self.line_cache = {}
        
    def translate_text(self, text):
        """Menerjemahkan teks menggunakan translate-shell"""
        if not text or text.isspace():
            return text
            
        if text in self.translation_cache:
            return self.translation_cache[text]
            
        try:
            cmd = f'trans -b en:{TARGET_LANG} "{text}"'
            result = subprocess.getoutput(cmd)
            translated = result.strip()
            self.translation_cache[text] = translated
            return translated
        except Exception as e:
            print(f"Gagal menerjemahkan: {str(e)}")
            return text

    def process_file(self):
        """Memproses file RPY dan membuat versi terjemahannya"""
        if not os.path.exists(INPUT_FILE):
            print(f"File tidak ditemukan: {INPUT_FILE}")
            return False
            
        print(f"Memproses file: {INPUT_FILE}")
        print(f"Hasil akan disimpan ke: {OUTPUT_FILE}")
        
        with open(INPUT_FILE, 'r', encoding='utf-8') as infile, \
             open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            
            lines = infile.readlines()
            total_lines = len(lines)
            
            for i, line in enumerate(lines):
                # Tampilkan progress sederhana
                print(f"Memproses baris {i+1}/{total_lines}", end='\r')
                
                if line.strip().startswith('#') or not line.strip():
                    outfile.write(line)
                    continue
                    
                matches = re.findall(r'"(.*?)"', line)
                if not matches:
                    outfile.write(line)
                    continue
                    
                new_line = line
                for text in matches:
                    if text not in self.line_cache:
                        translated = self.translate_text(text)
                        self.line_cache[text] = translated
                    
                    new_line = new_line.replace(
                        f'"{text}"', 
                        f'"{self.line_cache[text]}"'
                    )
                
                outfile.write(new_line)
                
        print("\nTerjemahan selesai!")
        return True

if __name__ == "__main__":
    # Periksa translate-shell
    try:
        subprocess.run(["trans", "--version"], 
                      check=True, 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE)
    except:
        print("Error: translate-shell belum terinstall!")
        print("Silakan install terlebih dahulu:")
        print("1. Install dependencies: sudo apt install git gawk")
        print("2. Clone repo: git clone https://github.com/soimort/translate-shell")
        print("3. Buat symlink: cd translate-shell && make && sudo make install")
        exit(1)
    
    translator = RpyTranslator()
    translator.process_file()