#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY AUTOMATIC TAG PROTECTOR v5.1
Fitur:
- Auto-rename mapping file jika sudah ada
- Deteksi otomatis semua tag & variabel
- Assign angka unik
- Progress bar real-time
"""

import re
import os
import time
import subprocess
from collections import defaultdict

# ================ CONFIG ================
INPUT_FILE = "x-NTR_part5.rpy"    # File input
BAHASA_ASAL = "en"          # Bahasa sumber
BAHASA_TUJUAN = "id"        # Bahasa target
JEDA_TERJEMAH = 0.3         # Delay antar terjemahan (detik)
# ========================================

class RenPyAutoTranslator:
    def __init__(self):
        self.output_file = self._generate_output_name()
        self.mapping_file = self._generate_mapping_name()
        self.tag_map = defaultdict(str)
        self.var_map = defaultdict(str)
        self.tag_counter = 1
        self.var_counter = 1
        self.total_lines = 0

    def _generate_output_name(self):
        """Generate nama output: script.rpy -> script_id.rpy"""
        base, ext = os.path.splitext(INPUT_FILE)
        return f"{base}_{BAHASA_TUJUAN}{ext}"

    def _generate_mapping_name(self):
        """Generate nama unik untuk file mapping"""
        base_name = "tag_mapping.txt"
        counter = 1
        
        while os.path.exists(base_name):
            base_name = f"tag_mapping_{counter}.txt"
            counter += 1
        
        if counter > 1:
            print(f"⚠️ File tag_mapping.txt sudah ada, membuat {base_name}")
        
        return base_name

    def _scan_tags_and_vars(self):
        """Deteksi semua tag dan variabel"""
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # Scan tags
        for tag in set(re.findall(r'\{([^\}]+)\}', content)):
            if tag not in self.tag_map:
                self.tag_map[tag] = str(self.tag_counter)
                self.tag_counter += 1

        # Scan variables
        for var in set(re.findall(r'\[([^\]]+)\]', content)):
            if var not in self.var_map:
                self.var_map[var] = str(self.var_counter)
                self.var_counter += 1

        # Simpan mapping
        with open(self.mapping_file, 'w', encoding='utf-8') as f:
            f.write("=== TAG MAPPING ===\n")
            for tag, num in sorted(self.tag_map.items(), key=lambda x: int(x[1])):
                f.write(f"{{{num}}} = {{{tag}}}\n")
            
            f.write("\n=== VARIABLE MAPPING ===\n")
            for var, num in sorted(self.var_map.items(), key=lambda x: int(x[1])):
                f.write(f"[{num}] = [{var}]\n")

    def _translate_text(self, text):
        """Terjemahkan teks"""
        try:
            result = subprocess.run(
                f'trans -b {BAHASA_ASAL}:{BAHASA_TUJUAN} "{text}"',
                shell=True, capture_output=True, text=True, timeout=10
            )
            return result.stdout.strip()
        except:
            return text

    def _process_line(self, line):
        """Proses satu baris"""
        # Ganti variabel
        line = re.sub(
            r'\[([^\]]+)\]', 
            lambda m: f"[{self.var_map.get(m.group(1), '?')}]", 
            line
        )
        
        # Ganti tag
        line = re.sub(
            r'\{([^\}]+)\}', 
            lambda m: f"{{{self.tag_map.get(m.group(1), '?')}}}", 
            line
        )
        
        # Terjemahkan teks
        return re.sub(
            r'"(.*?)"', 
            lambda m: f'"{self._translate_text(m.group(1))}"', 
            line
        )

    def run(self):
        """Eksekusi utama"""
        if not os.path.exists(INPUT_FILE):
            print(f"❌ File tidak ditemukan: {INPUT_FILE}")
            return

        print("🔍 Scanning tags dan variabel...")
        self._scan_tags_and_vars()

        print("\n🚀 Memulai terjemahan...")
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.total_lines = len(lines)
        results = []

        for i, line in enumerate(lines, 1):
            results.append(self._process_line(line))
            
            # Progress bar
            percent = (i / self.total_lines) * 100
            print(f"\r📊 Progress: {percent:.1f}% | Baris: {i}/{self.total_lines}", end='')
            time.sleep(JEDA_TERJEMAH)

        # Simpan hasil
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.writelines(results)

        print(f"\n✅ Selesai! File tersimpan di:")
        print(f"- Hasil: {self.output_file}")
        print(f"- Mapping: {self.mapping_file}")

if __name__ == "__main__":
    print("\n=== REN'PY AUTO TRANSLATOR ===")
    translator = RenPyAutoTranslator()
    translator.run()