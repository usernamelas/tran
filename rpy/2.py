#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPROVED REN'PY TRANSLATOR WITH TRANSLATE-SHELL
Fitur tambahan:
- Auto restore tags/variables
- Smart quote detection (skip file paths, codes)
- Better error handling
- Support multiple dialogue formats
"""

import re
import os
import time
import subprocess
from collections import defaultdict

# ================ CONFIG ================
SUPPORTED_EXTENSIONS = ['.rpy']
JEDA_TERJEMAH = 0.3
DEFAULT_SOURCE_LANG = 'en'
DEFAULT_TARGET_LANG = 'id'
# ========================================

class ImprovedRenPyTranslator:
    def __init__(self):
        self.input_file = ""
        self.output_file = ""
        self.tag_map = defaultdict(str)
        self.var_map = defaultdict(str)
        self.tag_counter = 1
        self.var_counter = 1
        self.source_lang = DEFAULT_SOURCE_LANG
        self.target_lang = DEFAULT_TARGET_LANG
        self.stats = {'translated': 0, 'skipped': 0, 'failed': 0}

    def set_languages(self, source, target):
        self.source_lang = source
        self.target_lang = target

    def set_input_file(self, filename):
        self.input_file = filename
        base = os.path.splitext(filename)[0]
        self.output_file = f"{base}_{self.target_lang}.rpy"

    def _scan_tags_and_vars(self, content):
        """Scan semua tag dan variabel dalam file"""
        # Scan tags {ini}
        for tag in set(re.findall(r'\{([^\}]+)\}', content)):
            if tag not in self.tag_map:
                placeholder = f"TAGPLACEHOLDER{self.tag_counter}"
                self.tag_map[placeholder] = tag
                self.tag_counter += 1

        # Scan variables [ini]  
        for var in set(re.findall(r'\[([^\]]+)\]', content)):
            if var not in self.var_map:
                placeholder = f"VARPLACEHOLDER{self.var_counter}"
                self.var_map[placeholder] = var
                self.var_counter += 1

    def _protect_codes(self, text):
        """Replace tags/vars dengan placeholder sebelum translate"""
        protected_text = text
        
        # Replace tags {xxx} -> TAGPLACEHOLDER1
        for placeholder, original in self.tag_map.items():
            protected_text = protected_text.replace(f"{{{original}}}", placeholder)
            
        # Replace vars [xxx] -> VARPLACEHOLDER1  
        for placeholder, original in self.var_map.items():
            protected_text = protected_text.replace(f"[{original}]", placeholder)
            
        return protected_text

    def _restore_codes(self, text):
        """Restore placeholder ke tag/var asli setelah translate"""
        restored_text = text
        
        # Restore tags
        for placeholder, original in self.tag_map.items():
            restored_text = restored_text.replace(placeholder, f"{{{original}}}")
            
        # Restore vars
        for placeholder, original in self.var_map.items():
            restored_text = restored_text.replace(placeholder, f"[{original}]")
            
        return restored_text

    def _is_translatable_text(self, text):
        """Check apakah text layak diterjemahkan"""
        # Skip text yang sangat pendek
        if len(text.strip()) < 3:
            return False
            
        # Skip jika mayoritas adalah file path atau code
        if ('.' in text and '/' in text) or text.count('_') > len(text) // 4:
            return False
            
        # Skip jika banyak angka/symbol
        if sum(c.isalnum() for c in text) < len(text) // 2:
            return False
            
        # Skip pure code patterns
        code_patterns = [
            r'^[a-zA-Z_]\w*$',  # variable names
            r'^\d+\.?\d*$',     # numbers
            r'^#[0-9a-fA-F]+$', # hex colors
        ]
        
        for pattern in code_patterns:
            if re.match(pattern, text.strip()):
                return False
                
        return True

    def _translate_text(self, text):
        """Terjemahkan teks menggunakan translate-shell dengan error handling"""
        if not self._is_translatable_text(text):
            self.stats['skipped'] += 1
            return text
            
        try:
            # Protect codes sebelum translate
            protected_text = self._protect_codes(text)
            
            # Escape untuk command line
            escaped_text = protected_text.replace('"', '\\"').replace("'", "\\'")
            
            # Command translate-shell
            cmd = [
                'trans',
                '-b',  # brief mode
                '-t', self.target_lang,
                f'"{escaped_text}"'
            ]
            
            result = subprocess.run(
                ' '.join(cmd),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=15,
                encoding='utf-8'
            )
            
            if result.returncode != 0:
                print(f"\n⚠️ translate-shell error: {result.stderr.strip()}")
                self.stats['failed'] += 1
                return text
                
            translated = result.stdout.strip().strip('"')
            
            # Restore codes setelah translate
            final_text = self._restore_codes(translated)
            self.stats['translated'] += 1
            
            return final_text
            
        except subprocess.TimeoutExpired:
            print(f"\n⏱️ Timeout translating: {text[:30]}...")
            self.stats['failed'] += 1
            return text
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            self.stats['failed'] += 1
            return text

    def _process_line(self, line):
        """Proses satu baris dengan deteksi format yang lebih baik"""
        original_line = line
        
        # Skip baris kode
        stripped = line.strip()
        if (not stripped or stripped.startswith('#') or
            any(stripped.startswith(cmd) for cmd in [
                'label ', 'scene ', 'show ', 'hide ', 'play ', 'stop ',
                'if ', 'else:', 'elif ', 'menu:', 'python:', '$',
                'return', 'jump ', 'call ', 'define ', 'default '
            ])):
            return line

        # Pattern untuk dialogue dengan karakter: character "text"
        char_dialogue = re.match(r'^(\s*)(\w+)\s+"([^"]*)"(.*)$', line)
        if char_dialogue:
            indent, char, dialogue, rest = char_dialogue.groups()
            if dialogue.strip():
                translated_dialogue = self._translate_text(dialogue)
                return f'{indent}{char} "{translated_dialogue}"{rest}\n'
            return line

        # Pattern untuk narrator: "text"
        narrator = re.match(r'^(\s*)"([^"]*)"(.*)$', line)  
        if narrator:
            indent, text, rest = narrator.groups()
            if text.strip():
                translated_text = self._translate_text(text)
                return f'{indent}"{translated_text}"{rest}\n'
            return line

        # Pattern untuk menu choice: "choice":
        choice = re.match(r'^(\s*)"([^"]*)"\s*:(.*)$', line)
        if choice:
            indent, choice_text, rest = choice.groups()
            if choice_text.strip():
                translated_choice = self._translate_text(choice_text)
                return f'{indent}"{translated_choice}":{rest}\n'
            return line

        return line

    def run_translation(self):
        """Jalankan proses terjemahan lengkap"""
        if not os.path.exists(self.input_file):
            print(f"❌ File tidak ditemukan: {self.input_file}")
            return False

        # Check translate-shell
        try:
            subprocess.run(['trans', '--version'], capture_output=True, timeout=5)
        except:
            print("❌ translate-shell tidak terinstall!")
            print("Install dengan: apt install translate-shell")
            return False

        print("\n🔍 Memulai proses...")
        print(f"📄 File input: {self.input_file}")
        print(f"🌐 Bahasa: {self.source_lang} → {self.target_lang}")
        
        # Read file dan scan
        with open(self.input_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.splitlines(keepends=True)

        print("\n🔎 Scanning tags dan variabel...")
        self._scan_tags_and_vars(content)
        print(f"✅ Ditemukan: {len(self.tag_map)} tags, {len(self.var_map)} variabel")
        
        # Process lines
        print("\n🚀 Memulai terjemahan...")
        total_lines = len(lines)
        results = []
        start_time = time.time()

        for i, line in enumerate(lines, 1):
            try:
                processed_line = self._process_line(line)
                results.append(processed_line)
                
                # Progress dengan stats
                percent = (i / total_lines) * 100
                elapsed = time.time() - start_time
                print(f"\r📊 {percent:.1f}% | {i}/{total_lines} | "
                      f"✅{self.stats['translated']} ⏭️{self.stats['skipped']} "
                      f"❌{self.stats['failed']} | {elapsed:.1f}s", end='')
                
                # Rate limiting
                if processed_line != line:  # Ada perubahan = ada terjemahan
                    time.sleep(JEDA_TERJEMAH)
                    
            except KeyboardInterrupt:
                print("\n\n⏹️ Dihentikan oleh user")
                break
            except Exception as e:
                print(f"\n⚠️ Error di baris {i}: {str(e)}")
                results.append(line)
                self.stats['failed'] += 1

        # Save hasil
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.writelines(results)
        except Exception as e:
            print(f"\n❌ Error menyimpan file: {e}")
            return False

        # Summary
        total_time = time.time() - start_time
        print(f"\n\n✅ Terjemahan selesai!")
        print(f"📂 File hasil: {self.output_file}")
        print(f"📊 Statistik:")
        print(f"   - Diterjemahkan: {self.stats['translated']}")
        print(f"   - Dilewati: {self.stats['skipped']}")  
        print(f"   - Gagal: {self.stats['failed']}")
        print(f"⏱️ Waktu total: {total_time:.1f} detik")
        
        return True

def check_dependencies():
    """Check apakah dependencies tersedia"""
    try:
        result = subprocess.run(['trans', '--version'], 
                              capture_output=True, timeout=5, text=True)
        if result.returncode == 0:
            print("✅ translate-shell tersedia")
            return True
    except:
        pass
    
    print("❌ translate-shell tidak ditemukan!")
    print("\nInstall dengan:")
    print("Ubuntu/Debian: apt install translate-shell")
    print("Termux: pkg install translate-shell")
    print("macOS: brew install translate-shell")
    print("Manual: npm install -g translate-shell")
    return False

def show_files():
    """Tampilkan file yang tersedia"""
    files = [f for f in os.listdir() 
             if os.path.isfile(f) 
             and os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS]
    
    if not files:
        print(f"\n❌ Tidak ada file .rpy ditemukan di direktori ini")
        return None
    
    print("\n📁 File .rpy yang tersedia:")
    for i, file in enumerate(files, 1):
        size = os.path.getsize(file) / 1024
        print(f"{i}. {file} ({size:.1f} KB)")
    
    while True:
        try:
            choice = input(f"\nPilih file (1-{len(files)}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                return files[idx]
            print("❌ Nomor tidak valid")
        except ValueError:
            print("❌ Input harus angka")
        except KeyboardInterrupt:
            return None

def main():
    print("\n" + "="*50)
    print("🚀 IMPROVED REN'PY TRANSLATOR")
    print("   Menggunakan translate-shell")
    print("="*50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Initialize translator
    translator = ImprovedRenPyTranslator()
    
    # Pilih file
    selected_file = show_files()
    if not selected_file:
        print("👋 Keluar...")
        return
        
    translator.set_input_file(selected_file)
    
    # Set bahasa (default en->id)
    print(f"\n🌐 Bahasa: {DEFAULT_SOURCE_LANG} → {DEFAULT_TARGET_LANG}")
    confirm = input("Gunakan setting ini? (y/n) [y]: ").strip().lower()
    
    if confirm == 'n':
        source = input(f"Bahasa sumber [{DEFAULT_SOURCE_LANG}]: ").strip() or DEFAULT_SOURCE_LANG
        target = input(f"Bahasa target [{DEFAULT_TARGET_LANG}]: ").strip() or DEFAULT_TARGET_LANG
        translator.set_languages(source, target)
    
    # Konfirmasi
    print(f"\n📋 Ringkasan:")
    print(f"   Input: {translator.input_file}")
    print(f"   Output: {translator.output_file}")
    print(f"   Bahasa: {translator.source_lang} → {translator.target_lang}")
    
    confirm = input("\nLanjutkan? (y/n) [y]: ").strip().lower()
    if confirm == 'n':
        print("👋 Dibatalkan")
        return
    
    # Jalankan terjemahan
    success = translator.run_translation()
    
    if success:
        print(f"\n🎉 Berhasil! Check file: {translator.output_file}")
    else:
        print("\n💥 Terjemahan gagal!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Program dihentikan")