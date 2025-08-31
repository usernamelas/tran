#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY AUTOMATIC TAG PROTECTOR v5.2
Fitur:
- Auto-rename mapping file jika sudah ada
- Deteksi otmatis semua tag & variabel
- Assign angka unik
- Progress bar real-time
- LOGGING SISTEM TERJEMAHAN (NEW!)
"""

import re
import os
import time
import subprocess
from collections import defaultdict
from datetime import datetime

# ================ CONFIG ================
INPUT_FILE = "x-episode1.rpy"    # File input
BAHASA_ASAL = "en"          # Bahasa sumber
BAHASA_TUJUAN = "id"        # Bahasa target
JEDA_TERJEMAH = 0.3         # Delay antar terjemahan (detik)
# ========================================

class RenPyAutoTranslator:
    def __init__(self):
        self.output_file = self._generate_output_name()
        self.mapping_file = self._generate_mapping_name()
        self.log_file = self._generate_log_name()
        self.tag_map = defaultdict(str)
        self.var_map = defaultdict(str)
        self.tag_counter = 1
        self.var_counter = 1
        self.total_lines = 0
        
        # Logging counters
        self.translation_stats = {
            'success': 0,
            'failed': 0,
            'empty_input': 0,
            'empty_output': 0,
            'errors': 0
        }

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

    def _generate_log_name(self):
        """Generate nama unik untuk file log"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"translation_log_{timestamp}.txt"

    def _init_log_file(self):
        """Inisialisasi file log"""
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("=== REN'PY TRANSLATION LOG ===\n")
            f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Input: {INPUT_FILE}\n")
            f.write(f"Output: {self.output_file}\n")
            f.write(f"Bahasa: {BAHASA_ASAL} -> {BAHASA_TUJUAN}\n")
            f.write("="*50 + "\n\n")

    def _log_translation(self, line_num, status, original_text, translated_text="", error_msg="", context=""):
        """Log hasil terjemahan ke file"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"BARIS {line_num} | STATUS: {status}\n")
            if context:
                f.write(f"CONTEXT: {context.strip()}\n")
            f.write(f"ASLI   : '{original_text}'\n")
            if translated_text:
                f.write(f"HASIL  : '{translated_text}'\n")
            if error_msg:
                f.write(f"ERROR  : {error_msg}\n")
            f.write("-" * 40 + "\n\n")

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

    def _translate_text(self, text, line_num, context=""):
        """Terjemahkan teks dengan logging"""
        # Check empty input
        if not text or not text.strip():
            self.translation_stats['empty_input'] += 1
            self._log_translation(line_num, "EMPTY_INPUT", text, context=context)
            return text

        try:
            # Escape quotes untuk shell command
            escaped_text = text.replace('"', '\\"').replace("'", "\\'")
            
            result = subprocess.run(
                f'trans -b {BAHASA_ASAL}:{BAHASA_TUJUAN} "{escaped_text}"',
                shell=True, capture_output=True, text=True, timeout=15
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                self.translation_stats['errors'] += 1
                self._log_translation(line_num, "ERROR", text, error_msg=error_msg, context=context)
                return text
            
            translated = result.stdout.strip()
            
            # Check empty output
            if not translated:
                self.translation_stats['empty_output'] += 1
                self._log_translation(line_num, "EMPTY_OUTPUT", text, translated, context=context)
                return text
            
            # Success
            self.translation_stats['success'] += 1
            self._log_translation(line_num, "SUCCESS", text, translated, context=context)
            return translated
            
        except subprocess.TimeoutExpired:
            self.translation_stats['errors'] += 1
            self._log_translation(line_num, "TIMEOUT", text, error_msg="Translation timeout", context=context)
            return text
        except Exception as e:
            self.translation_stats['failed'] += 1
            self._log_translation(line_num, "FAILED", text, error_msg=str(e), context=context)
            return text

    def _process_line(self, line, line_num):
        """Proses satu baris dengan logging"""
        original_line = line
        
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
        
        # Terjemahkan teks dalam quotes
        def translate_match(match):
            text = match.group(1)
            translated = self._translate_text(text, line_num, context=original_line)
            return f'"{translated}"'
        
        processed_line = re.sub(r'"(.*?)"', translate_match, line)
        return processed_line

    def _write_summary_log(self):
        """Tulis ringkasan statistik ke log"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*50 + "\n")
            f.write("RINGKASAN TERJEMAHAN\n")
            f.write("="*50 + "\n")
            f.write(f"✅ Berhasil      : {self.translation_stats['success']}\n")
            f.write(f"❌ Gagal         : {self.translation_stats['failed']}\n")
            f.write(f"⚠️ Error         : {self.translation_stats['errors']}\n")
            f.write(f"📝 Input Kosong  : {self.translation_stats['empty_input']}\n")
            f.write(f"📄 Output Kosong : {self.translation_stats['empty_output']}\n")
            f.write(f"📊 Total Proses  : {sum(self.translation_stats.values())}\n")

    def run(self):
        """Eksekusi utama"""
        if not os.path.exists(INPUT_FILE):
            print(f"❌ File tidak ditemukan: {INPUT_FILE}")
            return

        # Inisialisasi log
        self._init_log_file()

        print("🔍 Scanning tags dan variabel...")
        self._scan_tags_and_vars()

        print("\n🚀 Memulai terjemahan dengan logging...")
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.total_lines = len(lines)
        results = []

        for i, line in enumerate(lines, 1):
            processed = self._process_line(line, i)
            results.append(processed)
            
            # Progress bar
            percent = (i / self.total_lines) * 100
            print(f"\r📊 Progress: {percent:.1f}% | Baris: {i}/{self.total_lines}", end='')
            time.sleep(JEDA_TERJEMAH)

        # Simpan hasil
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.writelines(results)

        # Tulis ringkasan log
        self._write_summary_log()

        print(f"\n✅ Selesai! File tersimpan di:")
        print(f"- Hasil     : {self.output_file}")
        print(f"- Mapping   : {self.mapping_file}")
        print(f"- Log       : {self.log_file}")
        print(f"\n📊 Statistik:")
        print(f"- Berhasil  : {self.translation_stats['success']}")
        print(f"- Gagal     : {self.translation_stats['failed'] + self.translation_stats['errors']}")
        print(f"- Kosong    : {self.translation_stats['empty_input'] + self.translation_stats['empty_output']}")

if __name__ == "__main__":
    print("\n=== REN'PY AUTO TRANSLATOR v5.2 ===")
    translator = RenPyAutoTranslator()
    translator.run()