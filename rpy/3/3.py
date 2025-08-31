#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY AUTOMATIC TAG PROTECTOR v5.3
Fitur:
- Auto-rename mapping file jika sudah ada
- Deteksi otomatis semua tag & variabel
- Assign angka unik
- Progress bar real-time
- Smart context detection (FIXED!)
- Logging sistem yang optimal
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
LOG_LEVEL = "ERROR"         # Options: ALL, ERROR, SUMMARY
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
            'errors': 0,
            'skipped_code': 0,
            'total_processed': 0
        }
        
        # Ren'Py keywords yang TIDAK boleh ditranslate
        self.skip_keywords = [
            'show ', 'scene ', 'play ', 'stop ', 'queue ',
            'image ', 'define ', 'transform ', 'screen ',
            'jump ', 'call ', 'return', 'menu:', 'if ',
            'python:', 'init ', 'label ', 'with ',
            'hide ', 'at ', 'as ', '$', 'pause',
            'nvl ', 'window ', 'voice ', 'sound ',
            'music ', 'audio ', 'renpy.'
        ]

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
        if LOG_LEVEL == "SUMMARY":
            return
            
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("=== REN'PY TRANSLATION LOG v5.3 ===\n")
            f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Input: {INPUT_FILE}\n")
            f.write(f"Output: {self.output_file}\n")
            f.write(f"Bahasa: {BAHASA_ASAL} -> {BAHASA_TUJUAN}\n")
            f.write(f"Log Level: {LOG_LEVEL}\n")
            f.write("="*50 + "\n\n")

    def _log_translation(self, line_num, status, original_text, translated_text="", error_msg="", context=""):
        """Log hasil terjemahan ke file"""
        if LOG_LEVEL == "SUMMARY":
            return
        elif LOG_LEVEL == "ERROR" and status == "SUCCESS":
            return
            
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"BARIS {line_num} | STATUS: {status}\n")
            if context:
                f.write(f"CONTEXT: {context.strip()}\n")
            f.write(f"ASLI   : '{original_text}'\n")
            if translated_text and translated_text != original_text:
                f.write(f"HASIL  : '{translated_text}'\n")
            if error_msg:
                f.write(f"ERROR  : {error_msg}\n")
            f.write("-" * 40 + "\n\n")

    def _should_translate(self, line, text_match):
        """Cek apakah teks boleh ditranslate berdasarkan konteks Ren'Py"""
        before_quote = line[:text_match.start()].strip().lower()
        
        # Skip jika ada keyword Ren'Py di awal baris
        for keyword in self.skip_keywords:
            if before_quote.startswith(keyword.lower()):
                return False
        
        # Skip jika format: character "expression" atau character "emotion"
        # Pattern: nama_karakter spasi "text"
        char_pattern = r'^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*$'
        if re.match(char_pattern, before_quote):
            # Cek apakah kemungkinan expression/emotion (biasanya 1 kata)
            text_content = text_match.group(1).strip()
            if len(text_content.split()) <= 2 and not any(char in text_content for char in '.!?,:;'):
                return False
        
        # Skip jika ada tanda $ (Python code)
        if '$' in before_quote:
            return False
            
        # Skip jika di dalam menu options yang pendek
        if before_quote.endswith(':') and len(text_match.group(1).split()) <= 3:
            return False
            
        return True

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
        """Terjemahkan teks dengan logging dan error handling"""
        self.translation_stats['total_processed'] += 1
        
        # Check empty input
        if not text or not text.strip():
            self.translation_stats['empty_input'] += 1
            self._log_translation(line_num, "EMPTY_INPUT", text, context=context)
            return text

        try:
            # Escape quotes dan karakter khusus untuk shell command
            escaped_text = text.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
            
            # Command dengan error handling yang lebih baik
            cmd = f'trans -brief {BAHASA_ASAL}:{BAHASA_TUJUAN} "{escaped_text}"'
            
            result = subprocess.run(
                cmd,
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=20,
                encoding='utf-8'
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip() if result.stderr else "Unknown translation error"
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
            self._log_translation(line_num, "TIMEOUT", text, error_msg="Translation timeout (20s)", context=context)
            return text
        except Exception as e:
            self.translation_stats['failed'] += 1
            self._log_translation(line_num, "EXCEPTION", text, error_msg=f"Unexpected error: {str(e)}", context=context)
            return text

    def _process_line(self, line, line_num):
        """Proses satu baris dengan smart context detection"""
        original_line = line.rstrip()
        
        # Skip baris kosong atau komentar
        if not original_line.strip() or original_line.strip().startswith('#'):
            return line
            
        processed_line = original_line
        
        # Ganti variabel dengan placeholder
        processed_line = re.sub(
            r'\[([^\]]+)\]', 
            lambda m: f"[{self.var_map.get(m.group(1), '?')}]", 
            processed_line
        )
        
        # Ganti tag dengan placeholder
        processed_line = re.sub(
            r'\{([^\}]+)\}', 
            lambda m: f"{{{self.tag_map.get(m.group(1), '?')}}}", 
            processed_line
        )
        
        # Smart translation dengan context detection
        def smart_translate_match(match):
            text = match.group(1)
            
            # Cek apakah boleh ditranslate berdasarkan konteks
            if not self._should_translate(processed_line, match):
                self.translation_stats['skipped_code'] += 1
                self._log_translation(line_num, "SKIPPED_CODE", text, context=original_line)
                return f'"{text}"'  # Return as-is
            
            # Translate jika lolos filter
            translated = self._translate_text(text, line_num, context=original_line)
            return f'"{translated}"'
        
        # Apply smart translation
        final_line = re.sub(r'"(.*?)"', smart_translate_match, processed_line)
        return final_line + '\n'

    def _write_summary_log(self):
        """Tulis ringkasan statistik"""
        summary_text = f"""
{'='*50}
RINGKASAN TERJEMAHAN
{'='*50}
✅ Berhasil ditranslate : {self.translation_stats['success']}
⏩ Skip (Ren'Py code)   : {self.translation_stats['skipped_code']}
❌ Gagal/Error         : {self.translation_stats['failed'] + self.translation_stats['errors']}
📝 Input kosong         : {self.translation_stats['empty_input']}
📄 Output kosong        : {self.translation_stats['empty_output']}
📊 Total diproses       : {self.translation_stats['total_processed']}
📋 Total baris file     : {self.total_lines}
"""
        
        # Tulis ke log file jika bukan SUMMARY only
        if LOG_LEVEL != "SUMMARY":
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(summary_text)
        
        # Print ke console
        print(summary_text)

    def run(self):
        """Eksekusi utama"""
        if not os.path.exists(INPUT_FILE):
            print(f"❌ File tidak ditemukan: {INPUT_FILE}")
            return

        # Inisialisasi log
        self._init_log_file()

        print("🔍 Scanning tags dan variabel...")
        self._scan_tags_and_vars()

        print(f"\n🚀 Memulai terjemahan dengan smart detection (Log: {LOG_LEVEL})...")
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.total_lines = len(lines)
        results = []

        for i, line in enumerate(lines, 1):
            processed = self._process_line(line, i)
            results.append(processed)
            
            # Progress bar dengan info tambahan
            percent = (i / self.total_lines) * 100
            success_rate = (self.translation_stats['success'] / max(1, self.translation_stats['total_processed'])) * 100
            print(f"\r📊 Progress: {percent:.1f}% | Baris: {i}/{self.total_lines} | Success: {success_rate:.0f}%", end='')
            
            if JEDA_TERJEMAH > 0:
                time.sleep(JEDA_TERJEMAH)

        # Simpan hasil
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.writelines(results)
            print(f"\n✅ File output berhasil disimpan!")
        except Exception as e:
            print(f"\n❌ Error menyimpan file: {e}")
            return

        # Tulis ringkasan
        self._write_summary_log()

        print(f"\n📁 File yang dihasilkan:")
        print(f"- Hasil     : {self.output_file}")
        print(f"- Mapping   : {self.mapping_file}")
        if LOG_LEVEL != "SUMMARY":
            print(f"- Log       : {self.log_file}")

        # Warning jika banyak yang gagal
        total_issues = (self.translation_stats['failed'] + 
                       self.translation_stats['errors'] + 
                       self.translation_stats['empty_output'])
        
        if total_issues > 0:
            print(f"\n⚠️ Ada {total_issues} teks bermasalah, cek log untuk detail!")

if __name__ == "__main__":
    print("\n=== REN'PY AUTO TRANSLATOR v5.3 ===")
    print("🆕 Smart Context Detection + Optimized Logging")
    
    # Check dependency
    try:
        result = subprocess.run("trans --version", shell=True, capture_output=True)
        if result.returncode != 0:
            print("❌ translate-shell tidak ditemukan!")
            print("Install dengan: npm install -g translate-shell")
            exit(1)
    except:
        print("❌ Error checking translate-shell dependency")
        exit(1)
    
    translator = RenPyAutoTranslator()
    translator.run()
