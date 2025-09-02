#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APPLY TRANSLATIONS v1.1
Simple script untuk apply translations dari file log (CSV/JSON) ke file .rpy

Features:
- Support CSV dan JSON format
- Interactive file selection
- Safe approach: read original → write new file
- No backup complications, original files untouched
- Clear progress tracking
- Support semua file JSON (tidak hanya yang berpattern tertentu)

Usage:
  python apply.py                    # Interactive mode
  python apply.py filename.csv       # Direct apply from CSV
  python apply.py filename.json      # Direct apply from JSON
"""

import json
import os
import sys
import csv
import glob
from datetime import datetime

# ================ CONFIG ================
OUTPUT_SUFFIX = "_translated"         # Suffix untuk file hasil translate
LOG_PATTERN = "*untranslated*.csv"    # Pattern untuk mencari file log CSV
# ========================================

class TranslationApplier:
    def __init__(self):
        self.files_processed = 0
        self.translations_applied = 0
        self.errors = []

    def show_main_menu(self):
        """Display main interactive menu"""
        while True:
            print("\n" + "="*60)
            print("✅ APPLY TRANSLATIONS v1.1")
            print("="*60)
            print("1. 📄 Apply from CSV file    - Pilih file CSV untuk di-apply")
            print("2. 📄 Apply from JSON file   - Pilih file JSON untuk di-apply")
            print("3. 🔍 Show available files   - Tampilkan semua file log")
            print("4. 📊 Preview translations   - Preview tanpa apply")
            print("5. ❌ Exit                   - Keluar dari program")
            print("="*60)
            
            try:
                choice = input("Pilih menu (1-5): ").strip()
                
                if choice == '1':
                    self.menu_apply_csv()
                elif choice == '2':
                    self.menu_apply_json()
                elif choice == '3':
                    self.menu_show_files()
                elif choice == '4':
                    self.menu_preview()
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

    def get_csv_files(self):
        """Get all CSV files that might contain translations"""
        files = glob.glob(LOG_PATTERN)
        # Also include other CSV files that might be translation files
        all_csv = glob.glob("*.csv")
        for f in all_csv:
            if f not in files and any(keyword in f.lower() for keyword in ['translate', 'trans']):
                files.append(f)
        return sorted([f for f in files if os.path.isfile(f)])

    def get_json_files(self):
        """Get all JSON files (support semua file JSON)"""
        # Mengambil semua file JSON di direktori
        files = glob.glob("*.json")
        return sorted([f for f in files if os.path.isfile(f)])

    def display_file_list(self, files, file_type="files"):
        """Display numbered list of files"""
        if not files:
            print(f"❌ Tidak ada {file_type} ditemukan di folder ini.")
            return None
            
        print(f"\n📂 Daftar {file_type} yang tersedia:")
        print("-" * 60)
        for i, filename in enumerate(files, 1):
            file_size = os.path.getsize(filename)
            # Try to get entry count
            entry_count = self.get_entry_count(filename)
            print(f"{i:2}. {filename:<35} ({file_size:,} bytes) [{entry_count} entries]")
        print("-" * 60)
        return files

    def get_entry_count(self, filename):
        """Get number of entries in log file"""
        try:
            if filename.endswith('.csv'):
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    return sum(1 for row in reader)
            elif filename.endswith('.json'):
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return len(data) if isinstance(data, list) else 0
        except:
            return "?"

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

    def menu_apply_csv(self):
        """Menu for applying from CSV file"""
        print("\n✅ APPLY FROM CSV FILE")
        print("="*40)
        
        files = self.get_csv_files()
        displayed_files = self.display_file_list(files, "file CSV")
        
        if not displayed_files:
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        selected_file = self.select_file(files, "file CSV")
        if not selected_file:
            return
            
        print(f"\n🎯 Applying translations from: {selected_file}")
        self.apply_from_csv(selected_file)
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_apply_json(self):
        """Menu for applying from JSON file"""
        print("\n✅ APPLY FROM JSON FILE")
        print("="*40)
        
        files = self.get_json_files()
        displayed_files = self.display_file_list(files, "file JSON")
        
        if not displayed_files:
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        selected_file = self.select_file(files, "file JSON")
        if not selected_file:
            return
            
        print(f"\n🎯 Applying translations from: {selected_file}")
        self.apply_from_json(selected_file)
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_show_files(self):
        """Menu for showing all available files"""
        print("\n🔍 AVAILABLE FILES")
        print("="*40)
        
        csv_files = self.get_csv_files()
        json_files = self.get_json_files()
        
        if csv_files:
            print("\n📄 CSV Files:")
            self.display_file_list(csv_files, "file CSV")
        
        if json_files:
            print("\n📄 JSON Files:")
            self.display_file_list(json_files, "file JSON")
        
        if not csv_files and not json_files:
            print("❌ Tidak ada file log ditemukan.")
        
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_preview(self):
        """Menu for previewing translations without applying"""
        print("\n📊 PREVIEW TRANSLATIONS")
        print("="*40)
        print("Feature coming soon!")
        input("Tekan Enter untuk kembali ke menu...")

    def load_translations_from_csv(self, csv_file):
        """Load translations from CSV file"""
        translations = {}
        try:
            with open(csv_file, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    filename = row.get('filename', '').strip()
                    line_number = row.get('line_number', '').strip()
                    original = row.get('original_text', '').strip()
                    translation = row.get('translation', '').strip()
                    
                    # Skip empty translations or invalid data
                    if not all([filename, line_number, original, translation]):
                        continue
                    
                    try:
                        line_num = int(line_number)
                    except ValueError:
                        continue
                    
                    if filename not in translations:
                        translations[filename] = {}
                    
                    translations[filename][line_num] = {
                        'original': original,
                        'translation': translation
                    }
        
            return translations
            
        except FileNotFoundError:
            print(f"❌ CSV file not found: {csv_file}")
            return {}
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return {}

    def load_translations_from_json(self, json_file):
        """Load translations from JSON file"""
        try:
            with open(json_file, 'r', encoding='utf-8') as jsonfile:
                entries = json.load(jsonfile)
            
            translations = {}
            
            # Handle different JSON structures
            if isinstance(entries, list):
                # Format: list of translation entries
                for entry in entries:
                    self.process_json_entry(entry, translations)
            elif isinstance(entries, dict):
                # Format: dictionary with filename as keys
                for filename, file_entries in entries.items():
                    if isinstance(file_entries, list):
                        for entry in file_entries:
                            # Add filename if not present in entry
                            if 'filename' not in entry:
                                entry['filename'] = filename
                            self.process_json_entry(entry, translations)
            else:
                print("❌ JSON format not supported.")
                return {}
                
            return translations
            
        except FileNotFoundError:
            print(f"❌ JSON file not found: {json_file}")
            return {}
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON format in: {json_file}")
            return {}
        except Exception as e:
            print(f"❌ Error reading JSON: {e}")
            return {}

    def process_json_entry(self, entry, translations):
        """Process a single JSON entry and add to translations dictionary"""
        filename = entry.get('filename', '').strip()
        line_number = entry.get('line_number', '')
        original = entry.get('original_text', '').strip()
        translation = entry.get('translation', '').strip()
        
        # Skip empty translations or invalid data
        if not all([filename, original, translation]):
            return
        
        try:
            line_num = int(line_number) if line_number else 0
        except (ValueError, TypeError):
            line_num = 0
        
        if filename not in translations:
            translations[filename] = {}
        
        # If no line number, use incremental numbering
        if line_num == 0:
            line_num = len(translations[filename]) + 1
        
        translations[filename][line_num] = {
            'original': original,
            'translation': translation
        }

    def apply_from_csv(self, csv_file):
        """Apply translations from CSV file"""
        translations = self.load_translations_from_csv(csv_file)
        if translations:
            self.apply_translations(translations)

    def apply_from_json(self, json_file):
        """Apply translations from JSON file"""
        translations = self.load_translations_from_json(json_file)
        if translations:
            self.apply_translations(translations)

    def apply_translations(self, translations):
        """Apply translations to files"""
        if not translations:
            print("⚠️ No translations found in file.")
            return
        
        # Reset counters
        self.files_processed = 0
        self.translations_applied = 0
        self.errors = []
        
        print(f"\n📊 Found translations for {len(translations)} files")
        
        # Show preview
        total_translations = sum(len(file_trans) for file_trans in translations.values())
        print(f"📋 Total translations to apply: {total_translations}")
        
        # Confirm before applying
        confirm = input("\nApply translations? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes', 'ya']:
            print("❌ Apply cancelled.")
            return
        
        # Apply to each file
        for filename, file_translations in translations.items():
            print(f"\n📝 Processing: {filename}")
            
            if not os.path.exists(filename):
                print(f"   ❌ Original file not found: {filename}")
                self.errors.append(f"File not found: {filename}")
                continue
            
            # Create new filename
            base_name = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            new_filename = f"{base_name}{OUTPUT_SUFFIX}{extension}"
            
            try:
                # Read original file
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Apply translations
                updates_in_file = 0
                for line_num, translation_data in file_translations.items():
                    if 1 <= line_num <= len(lines):
                        line = lines[line_num - 1]
                        original_text = translation_data['original']
                        new_translation = translation_data['translation']
                        
                        # Replace the dialog text
                        if original_text in line:
                            updated_line = line.replace(original_text, new_translation)
                            lines[line_num - 1] = updated_line
                            updates_in_file += 1
                            self.translations_applied += 1
                        else:
                            print(f"   ⚠️ Line {line_num}: Original text not found")
                    else:
                        print(f"   ⚠️ Line {line_num}: Line number out of range")
                
                # Write new file
                with open(new_filename, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                print(f"   ✅ Applied {updates_in_file} translations → {new_filename}")
                self.files_processed += 1
                
            except Exception as e:
                error_msg = f"Error processing {filename}: {e}"
                print(f"   ❌ {error_msg}")
                self.errors.append(error_msg)
        
        # Show final results
        self.show_results()

    def show_results(self):
        """Show final results"""
        print("\n" + "=" * 60)
        print("🎯 APPLY RESULTS:")
        print(f"   Files processed successfully: {self.files_processed}")
        print(f"   Total translations applied: {self.translations_applied}")
        print(f"   Errors encountered: {len(self.errors)}")
        
        if self.errors:
            print(f"\n⚠️ Errors:")
            for error in self.errors[:3]:  # Show first 3 errors
                print(f"   - {error}")
            if len(self.errors) > 3:
                print(f"   ... and {len(self.errors) - 3} more errors")
        
        if self.files_processed > 0:
            print(f"\n✅ SUCCESS!")
            print(f"   New translated files created with '{OUTPUT_SUFFIX}' suffix")
            print(f"   Original files remain untouched")
            print(f"\n🎯 NEXT STEPS:")
            print(f"   1. Test the new *{OUTPUT_SUFFIX}.rpy files")
            print(f"   2. If everything works, replace original files")
            print(f"   3. Original files serve as automatic backup")

def main():
    applier = TranslationApplier()
    
    if len(sys.argv) == 1:
        # Interactive menu mode
        applier.show_main_menu()
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        
        if filename.lower() in ['help', '--help', '-h']:
            print("✅ APPLY TRANSLATIONS v1.1")
            print("Usage:")
            print(f"  python {sys.argv[0]}           # Interactive menu")
            print(f"  python {sys.argv[0]} file.csv  # Apply from CSV")
            print(f"  python {sys.argv[0]} file.json # Apply from JSON")
            print(f"  python {sys.argv[0]} help      # Show this help")
        elif os.path.exists(filename):
            if filename.endswith('.csv'):
                print(f"✅ Direct apply from CSV: {filename}")
                applier.apply_from_csv(filename)
            elif filename.endswith('.json'):
                print(f"✅ Direct apply from JSON: {filename}")
                applier.apply_from_json(filename)
            else:
                print("❌ Unsupported file format. Use .csv or .json files.")
        else:
            print(f"❌ File not found: {filename}")
    else:
        print("❌ Too many arguments.")
        print(f"Usage: python {sys.argv[0]} [filename.csv|filename.json]")

if __name__ == "__main__":
    main()