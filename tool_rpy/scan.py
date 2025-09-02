#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSLATION CHECKER & APPLIER v2.0
Enhanced version with interactive menu system

Features:
- Interactive menu system
- Selective file scanning
- Integration with external translation script
- Multiple log format support (CSV/JSON)

Usage:
  python script.py    # Interactive menu mode
  python script.py scan    # Direct scan mode (legacy)
  python script.py apply   # Direct apply mode (legacy)
"""

import re
import os
import csv
import sys
import glob
import json
import subprocess
from datetime import datetime

# ================ CONFIG ================
RPY_PATTERN = "*.rpy"                 # Pattern file .rpy yang mau dicek
CSV_OUTPUT = "untranslated_texts.csv" # Output CSV untuk scanning
JSON_OUTPUT = "untranslated_texts.json" # Alternative JSON output
BACKUP_SUFFIX = "_pre_apply"          # Backup sebelum apply
TRANSLATION_SCRIPT = "translate.py"   # External translation script
ENGLISH_THRESHOLD = 0.3               # Threshold untuk deteksi English (30%)
# ========================================

class TranslationManager:
    def __init__(self):
        # Common English words yang sering muncul di dialog
        self.english_patterns = [
            # Common verbs
            r'\b(said|says|think|thought|know|want|like|love|hate|need|can|will|would|should|could|may|might|must|have|has|had|do|does|did|get|got|go|goes|went|come|came|take|took|give|gave|make|made|see|saw|look|tell|ask)\b',
            
            # Common adjectives  
            r'\b(good|bad|great|nice|beautiful|ugly|big|small|large|little|old|new|young|happy|sad|angry|tired|hungry|thirsty|hot|cold|warm|cool|fast|slow|easy|hard|difficult|simple|important|special)\b',
            
            # Common nouns
            r'\b(time|day|night|morning|evening|week|month|year|home|house|room|door|window|car|money|work|job|food|water|book|phone|computer|friend|family|mother|father|sister|brother|child|man|woman|girl|boy|people|person)\b',
            
            # Common phrases
            r'\b(you know|I think|I mean|of course|by the way|let me|wait for|look at|listen to|talk about|what about|how about|right now|just now|over there|in here|out there)\b',
            
            # Question words
            r'\b(what|where|when|why|how|who|which|whose)\b',
            
            # Pronouns
            r'\b(you|your|yours|I|my|mine|me|we|our|ours|us|he|his|him|she|her|hers|they|their|theirs|them|it|its|this|that|these|those)\b',
            
            # Connectors
            r'\b(and|but|or|so|because|if|when|then|than|as|like|with|without|for|from|to|in|on|at|by|up|down|out|off|over|under|through|between|among)\b'
        ]
        
        # Compile patterns untuk performance
        self.compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.english_patterns]
        
        # Indonesian words untuk false positive check
        self.indonesian_words = {
            'dan', 'atau', 'tapi', 'tetapi', 'jika', 'kalau', 'karena', 'sebab', 'untuk', 'dari', 'ke', 'di', 'pada', 'dengan', 'tanpa', 'atas', 'bawah', 'dalam', 'luar', 'antara', 'saya', 'aku', 'kamu', 'dia', 'mereka', 'kita', 'kami', 'ini', 'itu', 'yang', 'adalah', 'akan', 'sudah', 'belum', 'tidak', 'jangan', 'bisa', 'dapat', 'harus', 'mau', 'ingin', 'suka', 'cinta', 'benci', 'butuh', 'perlu', 'baik', 'buruk', 'bagus', 'jelek', 'cantik', 'ganteng', 'besar', 'kecil', 'tinggi', 'rendah', 'panjang', 'pendek', 'lama', 'baru', 'tua', 'muda', 'senang', 'sedih', 'marah', 'capek', 'lapar', 'haus', 'panas', 'dingin', 'hangat', 'sejuk', 'cepat', 'lambat', 'mudah', 'susah', 'sulit', 'simple', 'penting', 'khusus', 'waktu', 'hari', 'malam', 'pagi', 'sore', 'siang', 'minggu', 'bulan', 'tahun', 'rumah', 'kamar', 'pintu', 'jendela', 'mobil', 'uang', 'kerja', 'makanan', 'air', 'buku', 'telepon', 'komputer', 'teman', 'keluarga', 'ibu', 'ayah', 'kakak', 'adik', 'anak', 'pria', 'wanita', 'perempuan', 'laki', 'orang'
        }

    def show_main_menu(self):
        """Display main interactive menu"""
        while True:
            print("\n" + "="*60)
            print("🛠️  TRANSLATION CHECKER & APPLIER v2.0")
            print("="*60)
            print("1. 📄 Scan specific file    - Pilih file .rpy untuk di-scan")
            print("2. 📁 Scan all files       - Scan semua file .rpy di folder")
            print("3. 🌐 Translate file       - Jalankan script translate.py")
            print("4. ✅ Apply translations   - Apply dari file log (CSV/JSON)")
            print("5. ❌ Exit                 - Keluar dari program")
            print("="*60)
            
            try:
                choice = input("Pilih menu (1-5): ").strip()
                
                if choice == '1':
                    self.menu_scan_specific()
                elif choice == '2':
                    self.menu_scan_all()
                elif choice == '3':
                    self.menu_translate()
                elif choice == '4':
                    self.menu_apply()
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

    def get_rpy_files(self):
        """Get all .rpy files in current directory"""
        files = glob.glob(RPY_PATTERN)
        return sorted([f for f in files if os.path.isfile(f)])

    def get_log_files(self):
        """Get all log files (CSV and JSON) in current directory"""
        csv_files = glob.glob("*.csv")
        json_files = glob.glob("*.json")
        log_files = []
        
        # Filter for translation-related files
        for f in csv_files + json_files:
            if any(keyword in f.lower() for keyword in ['untranslated', 'translation', 'translate']):
                log_files.append(f)
        
        return sorted(log_files)

    def display_file_list(self, files, file_type="files"):
        """Display numbered list of files"""
        if not files:
            print(f"❌ Tidak ada {file_type} ditemukan di folder ini.")
            return None
            
        print(f"\n📂 Daftar {file_type} yang tersedia:")
        print("-" * 40)
        for i, filename in enumerate(files, 1):
            file_size = os.path.getsize(filename)
            print(f"{i:2}. {filename:<30} ({file_size:,} bytes)")
        print("-" * 40)
        return files

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

    def menu_scan_specific(self):
        """Menu for scanning specific file"""
        print("\n🔍 SCAN SPECIFIC FILE")
        print("="*40)
        
        files = self.get_rpy_files()
        displayed_files = self.display_file_list(files, "file .rpy")
        
        if not displayed_files:
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        selected_file = self.select_file(files, "file .rpy")
        if not selected_file:
            return
            
        print(f"\n🎯 Scanning file: {selected_file}")
        self.scan_files([selected_file])
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_scan_all(self):
        """Menu for scanning all files"""
        print("\n🔍 SCAN ALL FILES")
        print("="*40)
        
        files = self.get_rpy_files()
        if not files:
            print("❌ Tidak ada file .rpy ditemukan di folder ini.")
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        print(f"📋 Akan melakukan scan pada {len(files)} file .rpy:")
        for i, filename in enumerate(files, 1):
            print(f"   {i}. {filename}")
            
        confirm = input("\nLanjutkan scan? (y/n): ").strip().lower()
        if confirm in ['y', 'yes', 'ya']:
            print(f"\n🎯 Scanning {len(files)} files...")
            self.scan_files(files)
        else:
            print("❌ Scan dibatalkan.")
            
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_translate(self):
        """Menu for running external translation script"""
        print("\n🌐 TRANSLATE FILE")
        print("="*40)
        
        if not os.path.exists(TRANSLATION_SCRIPT):
            print(f"❌ Script translate tidak ditemukan: {TRANSLATION_SCRIPT}")
            print(f"   Pastikan file {TRANSLATION_SCRIPT} ada di folder yang sama.")
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        print(f"🔧 Menjalankan script: {TRANSLATION_SCRIPT}")
        
        try:
            # Run the external translation script
            result = subprocess.run([sys.executable, TRANSLATION_SCRIPT], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Script translate berhasil dijalankan!")
                if result.stdout:
                    print("📄 Output:")
                    print(result.stdout)
            else:
                print("❌ Error saat menjalankan script translate:")
                if result.stderr:
                    print(result.stderr)
                    
        except FileNotFoundError:
            print(f"❌ Python interpreter tidak ditemukan.")
        except Exception as e:
            print(f"❌ Error: {e}")
            
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_apply(self):
        """Menu for applying translations"""
        print("\n✅ APPLY TRANSLATIONS")
        print("="*40)
        
        log_files = self.get_log_files()
        displayed_files = self.display_file_list(log_files, "file log")
        
        if not displayed_files:
            print("💡 Tip: File log biasanya bernama 'untranslated_texts.csv' atau sejenisnya")
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        selected_file = self.select_file(log_files, "file log")
        if not selected_file:
            return
            
        print(f"\n🎯 Applying translations from: {selected_file}")
        
        # Determine file format and apply
        if selected_file.endswith('.csv'):
            self.apply_translations_from_csv(selected_file)
        elif selected_file.endswith('.json'):
            self.apply_translations_from_json(selected_file)
        else:
            print("❌ Format file tidak didukung. Hanya CSV dan JSON.")
            
        input("\nTekan Enter untuk kembali ke menu...")

    def _is_likely_english(self, text):
        """Check if text contains English patterns"""
        # Remove Ren'Py tags and variables
        clean_text = re.sub(r'\{[^}]*\}', '', text)
        clean_text = re.sub(r'\[[^\]]*\]', '', clean_text)
        
        # Remove punctuation for word analysis
        words = re.findall(r'\b[a-zA-Z]{3,}\b', clean_text.lower())
        
        if len(words) == 0:
            return False
        
        english_matches = 0
        total_words = len(words)
        
        # Check each word against English patterns
        for word in words:
            # Skip if it's a known Indonesian word
            if word in self.indonesian_words:
                continue
                
            # Check against English patterns
            for pattern in self.compiled_patterns:
                if pattern.search(word):
                    english_matches += 1
                    break
        
        # Consider it English if >threshold% of words match English patterns
        english_ratio = english_matches / total_words if total_words > 0 else 0
        return english_ratio > ENGLISH_THRESHOLD

    def _extract_dialog_text(self, line):
        """Extract dialog text from Ren'Py line"""
        # Pattern untuk character dialog: character_name "dialog text"
        char_dialog = re.match(r'^\s*(\w+)\s+"([^"]*)"', line)
        if char_dialog:
            return char_dialog.group(2)
        
        # Pattern untuk narrator dialog: "dialog text"
        narrator_dialog = re.match(r'^\s*"([^"]*)"', line)
        if narrator_dialog:
            return narrator_dialog.group(1)
        
        return None

    def scan_files(self, files_to_scan=None):
        """Scan files for untranslated text"""
        if files_to_scan is None:
            files_to_scan = self.get_rpy_files()
        
        if not files_to_scan:
            print(f"❌ No files found matching pattern: {RPY_PATTERN}")
            return
        
        untranslated_entries = []
        total_lines_checked = 0
        files_with_issues = 0
        
        for filepath in files_to_scan:
            print(f"📂 Scanning: {filepath}")
            file_issues = 0
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                for line_num, line in enumerate(lines, 1):
                    total_lines_checked += 1
                    
                    # Skip empty lines and comments
                    if not line.strip() or line.strip().startswith('#'):
                        continue
                    
                    # Extract dialog text
                    dialog_text = self._extract_dialog_text(line.strip())
                    if not dialog_text:
                        continue
                    
                    # Check if it's likely English
                    if self._is_likely_english(dialog_text):
                        untranslated_entries.append({
                            'filename': filepath,
                            'line_number': line_num,
                            'original_text': dialog_text.strip(),
                            'translation': ''  # Empty for manual input
                        })
                        file_issues += 1
                
                if file_issues > 0:
                    print(f"   ⚠️ Found {file_issues} untranslated lines")
                    files_with_issues += 1
                else:
                    print(f"   ✅ All dialogues appear translated")
                    
            except UnicodeDecodeError:
                print(f"   ❌ Encoding error reading file: {filepath}")
            except FileNotFoundError:
                print(f"   ❌ File not found: {filepath}")
            except Exception as e:
                print(f"   ❌ Error reading file: {e}")
        
        # Save results
        if untranslated_entries:
            # Save as CSV
            with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['filename', 'line_number', 'original_text', 'translation']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(untranslated_entries)
            
            # Also save as JSON for compatibility
            with open(JSON_OUTPUT, 'w', encoding='utf-8') as jsonfile:
                json.dump(untranslated_entries, jsonfile, indent=2, ensure_ascii=False)
            
            print("\n" + "=" * 60)
            print("📊 SCAN RESULTS:")
            print(f"   Files scanned: {len(files_to_scan)}")
            print(f"   Files with issues: {files_with_issues}")
            print(f"   Lines checked: {total_lines_checked}")
            print(f"   Untranslated entries: {len(untranslated_entries)}")
            print(f"   CSV report: {CSV_OUTPUT}")
            print(f"   JSON report: {JSON_OUTPUT}")
            print("\n🎯 NEXT STEPS:")
            print(f"   1. Open {CSV_OUTPUT} in Excel/LibreOffice")
            print(f"   2. Fill the 'translation' column manually")
            print(f"   3. Save the file")
            print(f"   4. Use menu option 4 to apply translations")
        else:
            print("\n🎉 No untranslated text found! All dialogues appear to be in Indonesian.")

    def apply_translations_from_csv(self, csv_file):
        """Apply translations from CSV file"""
        translations = {}
        try:
            with open(csv_file, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    filename = row['filename']
                    line_num = int(row['line_number'])
                    original = row['original_text'].strip()
                    translation = row['translation'].strip()
                    
                    # Skip empty translations
                    if not translation:
                        continue
                    
                    if filename not in translations:
                        translations[filename] = {}
                    
                    translations[filename][line_num] = {
                        'original': original,
                        'translation': translation
                    }
        except FileNotFoundError:
            print(f"❌ CSV file not found: {csv_file}")
            return
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return
        
        self._apply_translations(translations)

    def apply_translations_from_json(self, json_file):
        """Apply translations from JSON file"""
        try:
            with open(json_file, 'r', encoding='utf-8') as jsonfile:
                entries = json.load(jsonfile)
            
            translations = {}
            for entry in entries:
                filename = entry['filename']
                line_num = int(entry['line_number'])
                original = entry['original_text'].strip()
                translation = entry['translation'].strip()
                
                # Skip empty translations
                if not translation:
                    continue
                
                if filename not in translations:
                    translations[filename] = {}
                
                translations[filename][line_num] = {
                    'original': original,
                    'translation': translation
                }
                
        except FileNotFoundError:
            print(f"❌ JSON file not found: {json_file}")
            return
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON format in: {json_file}")
            return
        except Exception as e:
            print(f"❌ Error reading JSON: {e}")
            return
        
        self._apply_translations(translations)

    def _apply_translations(self, translations):
        """Apply translations to files"""
        if not translations:
            print("⚠️ No translations found in file.")
            print("   Make sure you filled the 'translation' column.")
            return
        
        # Apply translations
        files_updated = 0
        total_translations = 0
        
        for filename, file_translations in translations.items():
            if not os.path.exists(filename):
                print(f"⚠️ File not found: {filename}")
                continue
            
            print(f"📝 Updating: {filename}")
            
            # Create backup
            backup_path = filename + BACKUP_SUFFIX
            if not os.path.exists(backup_path):
                try:
                    with open(filename, 'r', encoding='utf-8') as src, \
                         open(backup_path, 'w', encoding='utf-8') as dst:
                        dst.write(src.read())
                    print(f"   💾 Backup: {backup_path}")
                except Exception as e:
                    print(f"   ❌ Error creating backup: {e}")
                    continue
            
            # Read and update file
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                updates_in_file = 0
                for line_num, translation_data in file_translations.items():
                    if line_num <= len(lines):
                        line = lines[line_num - 1]
                        original_text = translation_data['original']
                        new_translation = translation_data['translation']
                        
                        # Replace the dialog text
                        if original_text in line:
                            updated_line = line.replace(original_text, new_translation)
                            lines[line_num - 1] = updated_line
                            updates_in_file += 1
                            total_translations += 1
                        else:
                            print(f"   ⚠️ Line {line_num}: Original text not found")
                
                # Write updated file
                with open(filename, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                if updates_in_file > 0:
                    print(f"   ✅ Applied {updates_in_file} translations")
                    files_updated += 1
                else:
                    print(f"   ℹ️ No translations applied")
                    
            except Exception as e:
                print(f"   ❌ Error updating file: {e}")
        
        print("\n" + "=" * 60)
        print("✅ APPLY RESULTS:")
        print(f"   Files updated: {files_updated}")
        print(f"   Total translations applied: {total_translations}")
        print(f"   Backup files created with suffix: {BACKUP_SUFFIX}")

    def apply_translations(self):
        """Legacy method for backward compatibility"""
        self.apply_translations_from_csv(CSV_OUTPUT)

    def show_help(self):
        """Show usage help"""
        print("🛠️ TRANSLATION CHECKER & APPLIER v2.0")
        print("Enhanced version with interactive menu system")
        print("\nUSAGE:")
        print(f"  python {sys.argv[0]}        # Interactive menu mode (recommended)")
        print(f"  python {sys.argv[0]} scan   # Legacy: scan all files")
        print(f"  python {sys.argv[0]} apply  # Legacy: apply from {CSV_OUTPUT}")
        print(f"  python {sys.argv[0]} help   # Show this help")
        print("\nFEATURES:")
        print("  • Interactive menu system")
        print("  • Selective file scanning")
        print("  • Integration with external translation scripts")
        print("  • Multiple log format support (CSV/JSON)")
        print("  • Automatic backup before applying changes")

def main():
    manager = TranslationManager()
    
    if len(sys.argv) == 1:
        # No arguments = interactive menu mode
        manager.show_main_menu()
    elif len(sys.argv) == 2:
        mode = sys.argv[1].lower()
        
        if mode == 'scan':
            # Legacy mode: scan all files
            manager.scan_files()
        elif mode == 'apply':
            # Legacy mode: apply from default CSV
            manager.apply_translations()
        elif mode == 'help':
            manager.show_help()
        elif mode == 'menu':
            manager.show_main_menu()
        else:
            print(f"❌ Unknown mode: {mode}")
            manager.show_help()
    else:
        print("❌ Too many arguments.")
        manager.show_help()

if __name__ == "__main__":
    main()
