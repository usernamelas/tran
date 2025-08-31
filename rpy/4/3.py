#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY AUTOMATIC TAG PROTECTOR v5.3 - FULL FIXED VERSION
Fitur:
- Auto-rename mapping file jika sudah ada
- Deteksi otomatis semua tag & variabel
- Assign angka unik
- Progress bar real-time
- Smart context detection
- Full escape sequence protection (FIXED!)
- Optimized logging system
- Syntax error prevention
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
            'music ', 'audio ', 'renpy.', 'camera '
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

    def _protect_escapes(self, text):
        """Protect semua escape sequences dari Google Translate"""
        replacements = {
            '\\n': '<!NEWLINE!>',
            '\\t': '<!TAB!>',
            '\\"': '<!QUOTE!>',
            '\\\\': '<!BACKSLASH!>',
            '\\r': '<!CARRIAGE!>',
            '\\{': '<!LEFTBRACE!>',
            '\\}': '<!RIGHTBRACE!>'
        }
        
        protected = text
        for old, new in replacements.items():
            protected = protected.replace(old, new)
        return protected

    def _restore_escapes(self, text):
        """Restore escape sequences setelah translate"""
        replacements = {
            '<!NEWLINE!>': '\\n',
            '<!TAB!>': '\\t',
            '<!QUOTE!>': '\\"',
            '<!BACKSLASH!>': '\\\\',
            '<!CARRIAGE!>': '\\r',
            '<!LEFTBRACE!>': '\\{',
            '<!RIGHTBRACE!>': '\\}'
        }
        
        restored = text
        for old, new in replacements.items():
            restored = restored.replace(old, new)
        
        # Clean up extra spaces around tags
        restored = re.sub(r'\{\s+', '{', restored)
        restored = re.sub(r'\s+\}', '}', restored)
        
        return restored

    def _should_translate(self, line, text_match):
        """Cek apakah teks boleh ditranslate berdasarkan konteks Ren'Py"""
        before_quote = line[:text_match.start()].strip().lower()
        
        # Skip jika ada keyword Ren'Py di awal baris
        for keyword in self.skip_keywords:
            if before_quote.startswith(keyword.lower()):
                return False
        
        # Skip jika format: character "expression" atau character "emotion"
        char_pattern = r'^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*$'
        if re.match(char_pattern, before_quote):
            text_content = text_match.group(1).strip()
            # Skip jika kemungkinan expression (1-2 kata, tanpa punctuation)
            if (len(text_content.split()) <= 2 and 
                not any(char in text_content for char in '.!?,:;') and
                len(text_content) < 20):
                return False
        
        # Skip jika ada tanda $ (Python code)
        if '$' in before_quote:
            return False
            
        # Skip jika di dalam menu options yang pendek
        if before_quote.endswith(':') and len(text_match.group(1).split()) <= 3:
            return False
            
        # Skip jika hanya path/filename
        text_content = text_match.group(1)
        if (text_content.endswith(('.png', '.jpg', '.mp3', '.ogg', '.wav')) or
            '/' in text_content or '\\' in text_content):
            return False
            
        return True

    def _scan_tags_and_vars(self):
        """Deteksi semua tag dan variabel"""
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # Scan tags dengan pattern yang lebih akurat
        tag_pattern = r'\{([^{}]+)\}'
        for tag in set(re.findall(tag_pattern, content)):
            if tag not in self.tag_map:
                self.tag_map[tag] = str(self.tag_counter)
                self.tag_counter += 1

        # Scan variables dengan pattern yang lebih akurat
        var_pattern = r'\[([^\[\]]+)\]'
        for var in set(re.findall(var_pattern, content)):
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

        print(f"📋 Ditemukan {len(self.tag_map)} tags dan {len(self.var_map)} variables")

    def _do_translation(self, text):
        """Core translation function"""
        try:
            # Escape untuk shell command
            escaped_text = text.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
            
            # Command dengan flag yang lebih reliable
            cmd = f'trans -brief -no-ansi {BAHASA_ASAL}:{BAHASA_TUJUAN} "{escaped_text}"'
            
            result = subprocess.run(
                cmd,
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=25,
                encoding='utf-8'
            )
            
            if result.returncode != 0:
                return None, result.stderr.strip() if result.stderr else "Translation command failed"
            
            translated = result.stdout.strip()
            
            if not translated:
                return None, "Empty translation result"
                
            return translated, None
            
        except subprocess.TimeoutExpired:
            return None, "Translation timeout (25s)"
        except Exception as e:
            return None, f"Unexpected error: {str(e)}"

    def _translate_text(self, text, line_num, context=""):
        """Terjemahkan teks dengan full protection"""
        self.translation_stats['total_processed'] += 1
        
        # Check empty input
        if not text or not text.strip():
            self.translation_stats['empty_input'] += 1
            self._log_translation(line_num, "EMPTY_INPUT", text, context=context)
            return text

        # Protect escape sequences
        protected_text = self._protect_escapes(text)
        
        # Translate
        translated, error = self._do_translation(protected_text)
        
        if error:
            if "timeout" in error.lower():
                self.translation_stats['errors'] += 1
                self._log_translation(line_num, "TIMEOUT", text, error_msg=error, context=context)
            else:
                self.translation_stats['failed'] += 1
                self._log_translation(line_num, "FAILED", text, error_msg=error, context=context)
            return text
        
        if not translated:
            self.translation_stats['empty_output'] += 1
            self._log_translation(line_num, "EMPTY_OUTPUT", text, context=context)
            return text
        
        # Restore escape sequences
        final_text = self._restore_escapes(translated)
        
        # Success
        self.translation_stats['success'] += 1
        self._log_translation(line_num, "SUCCESS", text, final_text, context=context)
        return final_text

    def _process_line(self, line, line_num):
        """Proses satu baris dengan smart context detection"""
        original_line = line.rstrip()
        
        # Skip baris kosong, komentar, atau pure code
        if (not original_line.strip() or 
            original_line.strip().startswith('#') or
            original_line.strip().startswith('$')):
            return line
        
        processed_line = original_line
        
        # Ganti variabel dengan placeholder
        processed_line = re.sub(
            r'\[([^\[\]]+)\]', 
            lambda m: f"[{self.var_map.get(m.group(1), '?')}]", 
            processed_line
        )
        
        # Ganti tag dengan placeholder
        processed_line = re.sub(
            r'\{([^{}]+)\}', 
            lambda m: f"{{{self.tag_map.get(m.group(1), '?')}}}", 
            processed_line
        )
        
        # Smart translation dengan context detection & escape protection
        def smart_translate_match(match):
            text = match.group(1)
            
            # Cek apakah boleh ditranslate berdasarkan konteks
            if not self._should_translate(processed_line, match):
                self.translation_stats['skipped_code'] += 1
                self._log_translation(line_num, "SKIPPED_CODE", text, context=original_line)
                return f'"{text}"'  # Return as-is
            
            # Translate dengan full protection
            translated = self._translate_text(text, line_num, context=original_line)
            return f'"{translated}"'
        
        # Apply smart translation
        final_line = re.sub(r'"([^"]*)"', smart_translate_match, processed_line)
        return final_line + '\n'

    def _write_summary_log(self):
        """Tulis ringkasan statistik"""
        success_rate = (self.translation_stats['success'] / max(1, self.translation_stats['total_processed'])) * 100
        
        summary_text = f"""
{'='*60}
RINGKASAN TERJEMAHAN v5.3
{'='*60}
✅ Berhasil ditranslate : {self.translation_stats['success']}
⏩ Skip (Ren'Py code)   : {self.translation_stats['skipped_code']}
❌ Gagal/Error         : {self.translation_stats['failed'] + self.translation_stats['errors']}
📝 Input kosong         : {self.translation_stats['empty_input']}
📄 Output kosong        : {self.translation_stats['empty_output']}
📊 Total diproses       : {self.translation_stats['total_processed']}
📋 Total baris file     : {self.total_lines}
🎯 Success Rate         : {success_rate:.1f}%

NEXT STEPS:
1. Copy file {self.output_file} ke folder to_rpyc/
2. Run GitHub Actions workflow untuk compile .rpyc
3. Download hasil compile
4. Inject ke game folder story/
"""
        
        # Tulis ke log file jika bukan SUMMARY only
        if LOG_LEVEL != "SUMMARY":
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(summary_text)
        
        # Print ke console
        print(summary_text)

    def _check_dependencies(self):
        """Check apakah translate-shell tersedia"""
        try:
            result = subprocess.run("trans --version", shell=True, capture_output=True, timeout=5)
            if result.returncode != 0:
                print("❌ translate-shell tidak ditemukan!")
                print("📥 Install dengan: npm install -g translate-shell")
                print("🔗 Atau pakai: sudo apt install translate-shell")
                return False
            
            version = result.stdout.decode().strip()
            print(f"✅ translate-shell detected: {version}")
            return True
        except:
            print("❌ Error checking translate-shell dependency")
            print("📥 Install dengan: npm install -g translate-shell")
            return False

    def _validate_output(self):
        """Validasi syntax output file"""
        try:
            with open(self.output_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic syntax checks
            issues = []
            
            # Check unmatched quotes
            quote_count = content.count('"')
            if quote_count % 2 != 0:
                issues.append("⚠️ Unmatched quotes detected")
            
            # Check unmatched brackets
            if content.count('{') != content.count('}'):
                issues.append("⚠️ Unmatched curly brackets")
            
            if content.count('[') != content.count(']'):
                issues.append("⚠️ Unmatched square brackets")
            
            # Check for broken lines (quotes spanning multiple lines)
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                if line.strip().count('"') % 2 != 0:
                    # Check if it's intentionally multiline or broken
                    if not any(keyword in line.lower() for keyword in ['"""', "'''"]):
                        issues.append(f"⚠️ Possible broken string at line {i}")
            
            if issues:
                print(f"\n🚨 SYNTAX WARNINGS:")
                for issue in issues:
                    print(f"   {issue}")
                print("   Check file before compiling!")
            else:
                print(f"\n✅ Syntax validation passed!")
                
        except Exception as e:
            print(f"\n⚠️ Could not validate syntax: {e}")

    def run(self):
        """Eksekusi utama"""
        print(f"📂 Processing: {INPUT_FILE}")
        
        if not os.path.exists(INPUT_FILE):
            print(f"❌ File tidak ditemukan: {INPUT_FILE}")
            return

        # Check dependencies
        if not self._check_dependencies():
            return

        # Inisialisasi log
        self._init_log_file()

        print("🔍 Scanning tags dan variabel...")
        self._scan_tags_and_vars()

        print(f"\n🚀 Memulai terjemahan dengan smart detection...")
        print(f"⚙️ Mode: {LOG_LEVEL} logging | Delay: {JEDA_TERJEMAH}s")
        
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.total_lines = len(lines)
        results = []

        start_time = time.time()

        for i, line in enumerate(lines, 1):
            processed = self._process_line(line, i)
            results.append(processed)
            
            # Progress bar dengan info tambahan
            percent = (i / self.total_lines) * 100
            success_rate = (self.translation_stats['success'] / max(1, self.translation_stats['total_processed'])) * 100
            
            elapsed = time.time() - start_time
            eta = (elapsed / i) * (self.total_lines - i) if i > 0 else 0
            
            print(f"\r📊 {percent:.1f}% | {i}/{self.total_lines} | Success: {success_rate:.0f}% | ETA: {eta:.0f}s", end='')
            
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

        # Validasi syntax
        self._validate_output()

        # Tulis ringkasan
        self._write_summary_log()

        print(f"\n📁 File yang dihasilkan:")
        print(f"   📄 Hasil     : {self.output_file}")
        print(f"   🗂️ Mapping   : {self.mapping_file}")
        if LOG_LEVEL != "SUMMARY":
            print(f"   📋 Log       : {self.log_file}")

        # Warning jika banyak yang gagal
        total_issues = (self.translation_stats['failed'] + 
                       self.translation_stats['errors'] + 
                       self.translation_stats['empty_output'])
        
        if total_issues > 0:
            print(f"\n⚠️ Ada {total_issues} teks bermasalah, cek log untuk detail!")
        else:
            print(f"\n🎉 Translation completed successfully!")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🎮 REN'PY AUTO TRANSLATOR v5.3 - FULL FIXED")
    print("🛠️ Smart Context + Escape Protection + Syntax Validation")
    print("="*60)
    
    translator = RenPyAutoTranslator()
    translator.run()
    
    print(f"\n🎯 Ready for GitHub Actions compilation!")
    print(f"   1. Upload {translator.output_file} ke folder to_rpyc/")
    print(f"   2. Trigger workflow: compile.yml")
    print(f"   3. Download compiled .rpyc")
    print(f"   4. Inject ke game!")