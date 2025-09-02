#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY TRANSLATOR WITH TRANSLATE-SHELL
Fitur:
- Menggunakan translate-shell (command line)
- Format mapping sederhana
- Preservasi tag/variabel
- Auto-generate nama file
"""

import re
import os
import time
import subprocess
from collections import defaultdict

# ================ CONFIG ================
SUPPORTED_EXTENSIONS = ['.rpy']
JEDA_TERJEMAH = 0.2
DEFAULT_SOURCE_LANG = 'en'
DEFAULT_TARGET_LANG = 'id'
# ========================================

class RenPyTranslator:
    def __init__(self):
        self.input_file = ""
        self.output_file = ""
        self.mapping_file = ""
        self.tag_map = defaultdict(str)
        self.var_map = defaultdict(str)
        self.tag_counter = 1
        self.var_counter = 1
        self.source_lang = DEFAULT_SOURCE_LANG
        self.target_lang = DEFAULT_TARGET_LANG

    def set_languages(self, source, target):
        self.source_lang = source
        self.target_lang = target

    def set_input_file(self, filename):
        self.input_file = filename
        base = os.path.splitext(filename)[0]
        self.mapping_file = f"mapping_{base}.txt"
        self.output_file = f"{base}_{self.target_lang}.rpy"

    def _scan_tags_and_vars(self):
        """Scan semua tag dan variabel dalam file"""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Scan tags {ini}
        for tag in set(re.findall(r'\{([^\}]+)\}', content)):
            if tag not in self.tag_map:
                self.tag_map[tag] = str(self.tag_counter)
                self.tag_counter += 1

        # Scan variables [ini]
        for var in set(re.findall(r'\[([^\]]+)\]', content)):
            if var not in self.var_map:
                self.var_map[var] = str(self.var_counter)
                self.var_counter += 1

        # Simpan mapping file
        with open(self.mapping_file, 'w', encoding='utf-8') as f:
            f.write("=== TAG MAPPING ===\n")
            for tag, num in sorted(self.tag_map.items(), key=lambda x: int(x[1])):
                f.write(f"{{{num}}} = {{{tag}}}\n")
            
            f.write("\n=== VARIABLE MAPPING ===\n")
            for var, num in sorted(self.var_map.items(), key=lambda x: int(x[1])):
                f.write(f"[{num}] = [{var}]\n")

    def _translate_text(self, text):
        """Terjemahkan teks menggunakan translate-shell"""
        try:
            # Escape karakter khusus untuk command line
            text = text.replace('"', '\\"')
            
            # Eksekusi translate-shell
            cmd = [
                'trans',
                '-b',
                f'{self.source_lang}:{self.target_lang}',
                f'"{text}"'
            ]
            result = subprocess.run(
                ' '.join(cmd),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                print(f"\n⚠️ Error menerjemahkan: {result.stderr.strip()}")
                return text
                
            return result.stdout.strip().strip('"')
        except Exception as e:
            print(f"\n⚠️ Gagal menerjemahkan: {str(e)}")
            return text

    def _process_line(self, line):
        """Proses satu baris teks"""
        # Proses variabel [ini] -> [1]
        line = re.sub(
            r'\[([^\]]+)\]',
            lambda m: f"[{self.var_map.get(m.group(1), '?')}]",
            line
        )
        
        # Proses tag {ini} -> {1}
        line = re.sub(
            r'\{([^\}]+)\}',
            lambda m: f"{{{self.tag_map.get(m.group(1), '?')}}}",
            line
        )
        
        # Terjemahkan teks dalam tanda kutip
        return re.sub(
            r'"(.*?)"',
            lambda m: f'"{self._translate_text(m.group(1))}"',
            line
        )

    def run_translation(self):
        """Jalankan proses terjemahan lengkap"""
        if not os.path.exists(self.input_file):
            print(f"❌ File tidak ditemukan: {self.input_file}")
            return False

        print("\n🔍 Memulai proses...")
        print(f"📄 File input: {self.input_file}")
        print(f"🌐 Bahasa: {self.source_lang} → {self.target_lang}")
        
        # Step 1: Scan tags dan variabel
        print("\n🔎 Scanning tags dan variabel...")
        self._scan_tags_and_vars()
        print(f"✅ Ditemukan: {len(self.tag_map)} tags, {len(self.var_map)} variabel")
        print(f"📝 File mapping dibuat: {self.mapping_file}")
        
        # Step 2: Proses terjemahan
        print("\n🚀 Memulai terjemahan... (Mohon tunggu)")
        with open(self.input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        total_lines = len(lines)
        results = []
        start_time = time.time()

        for i, line in enumerate(lines, 1):
            try:
                processed_line = self._process_line(line)
                results.append(processed_line)
                
                # Hitung progress
                percent = (i / total_lines) * 100
                elapsed = time.time() - start_time
                print(f"\r📊 Progress: {percent:.1f}% | Baris: {i}/{total_lines} | Waktu: {elapsed:.1f}s", end='')
                time.sleep(JEDA_TERJEMAH)
            except Exception as e:
                print(f"\n⚠️ Error di baris {i}: {str(e)}")
                results.append(line)  # Simpan line asli jika error

        # Step 3: Simpan hasil
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.writelines(results)

        print(f"\n\n✅ Terjemahan selesai!")
        print(f"📂 File hasil: {self.output_file}")
        print(f"⏱️ Waktu total: {time.time() - start_time:.1f} detik")
        return True

def show_files():
    """Tampilkan file yang tersedia"""
    files = [f for f in os.listdir() 
             if os.path.isfile(f) 
             and os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS]
    
    if not files:
        print("\n❌ Tidak ada file yang didukung")
        print(f"Ekstensi didukung: {', '.join(SUPPORTED_EXTENSIONS)}")
        return None
    
    print("\n📁 File yang tersedia:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    while True:
        choice = input("\nPilih file (nomor): ").strip()
        try:
            return files[int(choice)-1]
        except:
            print("❌ Input tidak valid")

def select_language(prompt, current):
    """Menu pilih bahasa"""
    langs = {
        '1': 'id', '2': 'en', '3': 'ja', 
        '4': 'ko', '5': 'zh', '6': 'es'
    }
    
    print(f"\n{prompt}:")
    for num, lang in langs.items():
        print(f"{num}. {lang.upper()}")
    
    while True:
        choice = input(f"Pilihan [{current}]: ").strip()
        if not choice:
            return current
        if choice in langs:
            return langs[choice]
        print("❌ Pilihan tidak valid")

def main():
    translator = RenPyTranslator()
    
    print("\n=== REN'PY TRANSLATOR ===")
    print("Menggunakan translate-shell")
    print("Pastikan sudah install:")
    print("1. translate-shell (brew install translate-shell)")
    print("2. Python library subprocess\n")
    
    # Pilih file
    selected_file = show_files()
    if not selected_file:
        return
    translator.set_input_file(selected_file)
    
    # Pilih bahasa
    translator.set_languages(
        select_language("Bahasa Sumber", DEFAULT_SOURCE_LANG),
        select_language("Bahasa Target", DEFAULT_TARGET_LANG)
    )
    
    # Jalankan terjemahan
    translator.run_translation()

if __name__ == "__main__":
    main()