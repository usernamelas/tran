#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON TRANSLATOR v1.0
Script untuk menerjemahkan file JSON menggunakan translate-shell

Requirements:
- translate-shell harus terinstall: sudo apt install translate-shell
- atau download dari: https://github.com/soimort/translate-shell

Features:
- Menggunakan translate-shell untuk translation
- Interactive file selection
- Batch translation with progress tracking
- Error handling and retry mechanism
- Backup original file
- Resume interrupted translation sessions

Usage:
  python translate.py           # Interactive mode
  python translate.py filename.json  # Direct translate specific file
"""

import json
import os
import sys
import time
import glob
import subprocess
import shutil
from datetime import datetime

# ================ CONFIG ================
INPUT_PATTERN = "*untranslated*.json"  # Pattern untuk file JSON input
OUTPUT_SUFFIX = "_translated"          # Suffix untuk file hasil translate
BACKUP_SUFFIX = "_backup"             # Suffix untuk backup file
DELAY_BETWEEN_REQUESTS = 2            # Delay antar request (seconds) untuk avoid rate limit
BATCH_SIZE = 5                        # Batch size untuk progress tracking
SOURCE_LANG = "en"                    # Source language (English)
TARGET_LANG = "id"                    # Target language (Indonesian)
MAX_RETRIES = 3                       # Maximum retry attempts
# ========================================

class JSONTranslator:
    def __init__(self):
        self.total_entries = 0
        self.completed_entries = 0
        self.failed_entries = []
        self.translate_shell_available = self.check_translate_shell()

    def check_translate_shell(self):
        """Check if translate-shell is available"""
        try:
            result = subprocess.run(['trans', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    def show_main_menu(self):
        """Display main interactive menu"""
        if not self.translate_shell_available:
            print("❌ translate-shell tidak ditemukan!")
            print("   Install dengan: sudo apt install translate-shell")
            print("   Atau download dari: https://github.com/soimort/translate-shell")
            return

        while True:
            print("\n" + "="*60)
            print("🌐 JSON TRANSLATOR v1.0 (translate-shell)")
            print("="*60)
            print("1. 📄 Translate JSON file    - Pilih file JSON untuk diterjemahkan")
            print("2. 🔍 Show available files   - Tampilkan file JSON yang tersedia")
            print("3. 📊 Check translation      - Cek progress file yang sudah ada")
            print("4. 🛠️ Resume translation     - Lanjutkan translate yang terhenti")
            print("5. ❌ Exit                   - Keluar dari program")
            print("="*60)
            
            try:
                choice = input("Pilih menu (1-5): ").strip()
                
                if choice == '1':
                    self.menu_translate_file()
                elif choice == '2':
                    self.menu_show_files()
                elif choice == '3':
                    self.menu_check_translation()
                elif choice == '4':
                    self.menu_resume_translation()
                elif choice == '5':
                    print("👋 Terima kasih! Program selesai.")
                    break
                else:
                    print("❌ Pilihan tidak valid. Silakan pilih 1-5.")
                    
            except KeyboardInterrupt:
                print("\n👋 Program dihentikan oleh user.")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

    def get_json_files(self):
        """Get all JSON files matching pattern"""
        files = glob.glob(INPUT_PATTERN)
        # Also include any JSON files that might be translation files
        all_json = glob.glob("*.json")
        for f in all_json:
            if f not in files and any(keyword in f.lower() for keyword in ['translate', 'untrans']):
                files.append(f)
        return sorted([f for f in files if os.path.isfile(f)])

    def display_file_list(self, files, file_type="files"):
        """Display numbered list of files"""
        if not files:
            print(f"❌ Tidak ada {file_type} ditemukan di folder ini.")
            return None
            
        print(f"\n📂 Daftar {file_type} yang tersedia:")
        print("-" * 50)
        for i, filename in enumerate(files, 1):
            file_size = os.path.getsize(filename)
            # Check if already translated
            status = self.check_file_translation_status(filename)
            print(f"{i:2}. {filename:<30} ({file_size:,} bytes) {status}")
        print("-" * 50)
        return files

    def check_file_translation_status(self, filename):
        """Check translation status of a file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if not isinstance(data, list):
                return "[❓ Format tidak dikenal]"
            
            total = len(data)
            translated = sum(1 for entry in data if entry.get('translation', '').strip())
            
            if translated == 0:
                return "[🔴 Belum diterjemahkan]"
            elif translated == total:
                return "[🟢 Sudah lengkap]"
            else:
                return f"[🟡 {translated}/{total} selesai]"
                
        except Exception:
            return "[❓ Error reading file]"

    def select_file(self, files, file_type="file"):
        """Let user select a file from the list"""
        if not files:
            return None
            
        try:
            choice = input(f"\nPilih {file_type} (nomor): ").strip()
            
            if choice.lower() in ['q', 'quit', 'exit']:
                return None
                
            index = int(choice) - 1
            if 0 <= index < len(files):
                return files[index]
            else:
                print(f"❌ Nomor tidak valid. Pilih 1-{len(files)}")
                return None
                
        except ValueError:
            print("❌ Input tidak valid. Masukkan nomor file.")
            return None

    def menu_translate_file(self):
        """Menu for translating specific file"""
        print("\n🌐 TRANSLATE JSON FILE")
        print("="*40)
        
        files = self.get_json_files()
        displayed_files = self.display_file_list(files, "file JSON")
        
        if not displayed_files:
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        selected_file = self.select_file(files, "file JSON")
        if not selected_file:
            return
            
        print(f"\n🎯 Translating file: {selected_file}")
        self.translate_json_file(selected_file)
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_show_files(self):
        """Menu for showing available files"""
        print("\n🔍 AVAILABLE FILES")
        print("="*40)
        
        files = self.get_json_files()
        self.display_file_list(files, "file JSON")
        
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_check_translation(self):
        """Menu for checking translation progress"""
        print("\n📊 CHECK TRANSLATION PROGRESS")
        print("="*40)
        
        files = self.get_json_files()
        if not files:
            print("❌ Tidak ada file JSON ditemukan.")
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        for filename in files:
            print(f"\n📄 {filename}")
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if not isinstance(data, list):
                    print("   ❓ Format file tidak dikenal")
                    continue
                
                total = len(data)
                translated = sum(1 for entry in data if entry.get('translation', '').strip())
                untranslated = total - translated
                
                print(f"   📊 Total entries: {total}")
                print(f"   ✅ Translated: {translated}")
                print(f"   ⏳ Remaining: {untranslated}")
                
                if untranslated > 0:
                    progress = (translated / total) * 100
                    print(f"   📈 Progress: {progress:.1f}%")
                else:
                    print("   🎉 Translation complete!")
                    
            except Exception as e:
                print(f"   ❌ Error reading file: {e}")
        
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_resume_translation(self):
        """Menu for resuming translation"""
        print("\n🛠️ RESUME TRANSLATION")
        print("="*40)
        
        files = self.get_json_files()
        # Filter files that have partial translations
        partial_files = []
        
        for filename in files:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if isinstance(data, list):
                    total = len(data)
                    translated = sum(1 for entry in data if entry.get('translation', '').strip())
                    if 0 < translated < total:
                        partial_files.append(filename)
            except Exception:
                continue
        
        if not partial_files:
            print("❌ Tidak ada file dengan translation yang terhenti.")
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        print("🔍 File dengan translation yang bisa dilanjutkan:")
        displayed_files = self.display_file_list(partial_files, "file JSON")
        
        selected_file = self.select_file(partial_files, "file JSON")
        if not selected_file:
            return
            
        print(f"\n🔄 Resuming translation: {selected_file}")
        self.translate_json_file(selected_file, resume=True)
        input("\nTekan Enter untuk kembali ke menu...")

    def translate_text(self, text, retries=0):
        """Translate text using translate-shell"""
        if not text.strip():
            return ""
        
        try:
            # Escape quotes and special characters
            escaped_text = text.replace('"', '\\"').replace("'", "\\'")
            
            # Use translate-shell command
            cmd = ['trans', f'{SOURCE_LANG}:{TARGET_LANG}', '-brief', escaped_text]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and result.stdout.strip():
                translated = result.stdout.strip()
                # Clean up the translation
                translated = translated.replace('\n', ' ').strip()
                return translated
            else:
                error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                print(f"   ⚠️ Translation error: {error_msg}")
                return None
                
        except subprocess.TimeoutExpired:
            print(f"   ⏱️ Translation timeout for: {text[:50]}...")
            return None
        except Exception as e:
            print(f"   ❌ Error translating: {e}")
            return None

    def translate_json_file(self, filename, resume=False):
        """Translate entries in JSON file"""
        # Create backup
        if not resume:
            backup_name = filename.replace('.json', f'{BACKUP_SUFFIX}.json')
            if not os.path.exists(backup_name):
                shutil.copy2(filename, backup_name)
                print(f"💾 Backup created: {backup_name}")
        
        # Load JSON data
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
            return
        
        if not isinstance(data, list):
            print("❌ JSON format not supported. Expected list of translation entries.")
            return
        
        # Count entries
        self.total_entries = len(data)
        self.completed_entries = sum(1 for entry in data if entry.get('translation', '').strip())
        remaining = self.total_entries - self.completed_entries
        
        if remaining == 0:
            print("🎉 All entries already translated!")
            return
        
        print(f"📊 Translation Status:")
        print(f"   Total entries: {self.total_entries}")
        print(f"   Already translated: {self.completed_entries}")
        print(f"   Remaining: {remaining}")
        
        if resume:
            print(f"\n🔄 Resuming translation...")
        else:
            print(f"\n🚀 Starting translation...")
        
        confirm = input(f"Continue? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes', 'ya']:
            print("❌ Translation cancelled.")
            return
        
        # Start translation
        self.failed_entries = []
        current_batch = 0
        
        for i, entry in enumerate(data):
            # Skip if already translated (for resume functionality)
            if entry.get('translation', '').strip():
                continue
            
            original_text = entry.get('original_text', '')
            if not original_text.strip():
                continue
            
            print(f"\n[{i+1}/{self.total_entries}] Translating...")
            print(f"📝 Original: {original_text[:80]}{'...' if len(original_text) > 80 else ''}")
            
            # Translate
            translation = self.translate_text(original_text)
            
            if translation:
                entry['translation'] = translation
                self.completed_entries += 1
                print(f"✅ Result: {translation[:80]}{'...' if len(translation) > 80 else ''}")
                
                # Save progress periodically
                current_batch += 1
                if current_batch >= BATCH_SIZE:
                    self.save_progress(filename, data)
                    current_batch = 0
                    print(f"💾 Progress saved ({self.completed_entries}/{self.total_entries})")
            else:
                self.failed_entries.append({
                    'index': i,
                    'text': original_text,
                    'filename': entry.get('filename', ''),
                    'line_number': entry.get('line_number', '')
                })
                print(f"❌ Failed to translate")
            
            # Delay to avoid rate limiting
            if i < len(data) - 1:  # Don't delay on last item
                time.sleep(DELAY_BETWEEN_REQUESTS)
        
        # Final save
        self.save_progress(filename, data)
        
        # Show results
        print("\n" + "="*60)
        print("🎯 TRANSLATION RESULTS:")
        print(f"   Total entries: {self.total_entries}")
        print(f"   Successfully translated: {self.completed_entries}")
        print(f"   Failed: {len(self.failed_entries)}")
        
        if self.failed_entries:
            print(f"\n⚠️ Failed entries:")
            for failed in self.failed_entries[:5]:  # Show first 5
                print(f"   - Line {failed['line_number']}: {failed['text'][:50]}...")
            if len(self.failed_entries) > 5:
                print(f"   ... and {len(self.failed_entries) - 5} more")
        
        # Create translated version
        if self.completed_entries > 0:
            translated_filename = filename.replace('.json', f'{OUTPUT_SUFFIX}.json')
            shutil.copy2(filename, translated_filename)
            print(f"\n📄 Translated file saved as: {translated_filename}")
        
        print(f"\n🎉 Translation {'completed' if len(self.failed_entries) == 0 else 'finished with some failures'}!")

    def save_progress(self, filename, data):
        """Save current progress to file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error saving progress: {e}")

def main():
    translator = JSONTranslator()
    
    if len(sys.argv) == 1:
        # Interactive menu mode
        translator.show_main_menu()
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        
        if arg.endswith('.json') and os.path.exists(arg):
            # Direct file translation
            print(f"🌐 Direct translation mode: {arg}")
            translator.translate_json_file(arg)
        elif arg.lower() in ['help', '--help', '-h']:
            print("🌐 JSON TRANSLATOR v1.0")
            print("Usage:")
            print(f"  python {sys.argv[0]}           # Interactive menu")
            print(f"  python {sys.argv[0]} file.json # Direct translate")
            print(f"  python {sys.argv[0]} help      # Show this help")
        else:
            print(f"❌ File not found or invalid argument: {arg}")
    else:
        print("❌ Too many arguments.")
        print(f"Usage: python {sys.argv[0]} [filename.json]")

if __name__ == "__main__":
    main()