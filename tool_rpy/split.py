#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON SPLITTER v1.0
Script untuk split JSON gabungan hasil scan menjadi file JSON terpisah per .rpy file

Features:
- Split JSON gabungan berdasarkan filename
- Auto naming: x-bdom.rpy → x-bdom.json
- Interactive file selection
- Preview mode
- Summary report

Usage:
  python split.py                    # Interactive mode
  python split.py combined.json      # Direct split specific file
"""

import json
import os
import sys
import glob
from datetime import datetime
from collections import defaultdict

# ================ CONFIG ================
INPUT_PATTERN = "*.json"           # Pattern untuk mencari JSON files
OUTPUT_SUFFIX = ""                 # Suffix untuk output files (kosong = sama dengan nama .rpy)
BACKUP_ORIGINAL = True             # Backup JSON original sebelum split
# ========================================

class JSONSplitter:
    def __init__(self):
        self.files_created = 0
        self.total_entries = 0
        self.errors = []

    def show_main_menu(self):
        """Display main interactive menu"""
        while True:
            print("\n" + "="*60)
            print("🔧 JSON SPLITTER v1.0")
            print("="*60)
            print("1. 📄 Split JSON file       - Pilih file JSON untuk di-split")
            print("2. 🔍 Show available files  - Tampilkan file JSON yang tersedia")
            print("3. 📊 Preview split result  - Preview tanpa create files")
            print("4. 🧹 Clean split files     - Hapus hasil split sebelumnya")
            print("5. ❌ Exit                  - Keluar dari program")
            print("="*60)
            
            try:
                choice = input("Pilih menu (1-5): ").strip()
                
                if choice == '1':
                    self.menu_split_file()
                elif choice == '2':
                    self.menu_show_files()
                elif choice == '3':
                    self.menu_preview()
                elif choice == '4':
                    self.menu_clean()
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
        """Get all JSON files that might be combined translation files"""
        files = glob.glob(INPUT_PATTERN)
        # Filter for likely combined files (larger files, contains multiple filenames)
        valid_files = []
        
        for f in files:
            if os.path.isfile(f):
                # Quick check if it's a combined file
                try:
                    file_count = self.count_unique_files(f)
                    if file_count > 1:  # More than 1 unique filename = combined
                        valid_files.append(f)
                    elif file_count == 1:  # Could be single file or combined
                        valid_files.append(f)
                except:
                    continue
        
        return sorted(valid_files)

    def count_unique_files(self, json_file):
        """Count unique filenames in JSON file"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if not isinstance(data, list):
                return 0
            
            filenames = set()
            for entry in data:
                if isinstance(entry, dict) and 'filename' in entry:
                    filenames.add(entry['filename'])
            
            return len(filenames)
        except:
            return 0

    def display_file_list(self, files, file_type="files"):
        """Display numbered list of files with analysis"""
        if not files:
            print(f"❌ Tidak ada {file_type} ditemukan di folder ini.")
            return None
            
        print(f"\n📂 Daftar {file_type} yang tersedia:")
        print("-" * 80)
        for i, filename in enumerate(files, 1):
            file_size = os.path.getsize(filename)
            entry_count = self.get_entry_count(filename)
            unique_files = self.count_unique_files(filename)
            
            print(f"{i:2}. {filename:<30} ({file_size:,} bytes) "
                  f"[{entry_count} entries from {unique_files} files]")
        print("-" * 80)
        return files

    def get_entry_count(self, filename):
        """Get number of entries in JSON file"""
        try:
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

    def menu_split_file(self):
        """Menu for splitting JSON file"""
        print("\n🔧 SPLIT JSON FILE")
        print("="*40)
        
        files = self.get_json_files()
        displayed_files = self.display_file_list(files, "file JSON")
        
        if not displayed_files:
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        selected_file = self.select_file(files, "file JSON")
        if not selected_file:
            return
            
        print(f"\n🎯 Splitting file: {selected_file}")
        self.split_json_file(selected_file)
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_show_files(self):
        """Menu for showing available files"""
        print("\n🔍 AVAILABLE FILES")
        print("="*40)
        
        files = self.get_json_files()
        self.display_file_list(files, "file JSON")
        
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_preview(self):
        """Menu for previewing split result"""
        print("\n📊 PREVIEW SPLIT RESULT")
        print("="*40)
        
        files = self.get_json_files()
        displayed_files = self.display_file_list(files, "file JSON")
        
        if not displayed_files:
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        selected_file = self.select_file(files, "file JSON")
        if not selected_file:
            return
            
        print(f"\n🔍 Preview for: {selected_file}")
        self.preview_split(selected_file)
        input("\nTekan Enter untuk kembali ke menu...")

    def menu_clean(self):
        """Menu for cleaning split files"""
        print("\n🧹 CLEAN SPLIT FILES")
        print("="*40)
        
        # Find potential split files (JSON files that match .rpy names)
        rpy_files = glob.glob("*.rpy")
        split_files = []
        
        for rpy in rpy_files:
            base_name = os.path.splitext(rpy)[0]
            json_name = f"{base_name}.json"
            if os.path.exists(json_name):
                split_files.append(json_name)
        
        if not split_files:
            print("❌ Tidak ada split files ditemukan.")
            input("Tekan Enter untuk kembali ke menu...")
            return
        
        print(f"🗑️ Found {len(split_files)} potential split files:")
        for f in split_files:
            print(f"   - {f}")
        
        confirm = input("\nHapus semua split files? (y/n): ").strip().lower()
        if confirm in ['y', 'yes', 'ya']:
            deleted = 0
            for f in split_files:
                try:
                    os.remove(f)
                    deleted += 1
                    print(f"   ✅ Deleted: {f}")
                except Exception as e:
                    print(f"   ❌ Error deleting {f}: {e}")
            
            print(f"\n🎯 Deleted {deleted} files.")
        else:
            print("❌ Delete cancelled.")
        
        input("\nTekan Enter untuk kembali ke menu...")

    def load_json_data(self, json_file):
        """Load and validate JSON data"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if not isinstance(data, list):
                print("❌ JSON format tidak didukung. Harus berupa list of entries.")
                return None
            
            # Validate entries
            valid_entries = []
            for entry in data:
                if (isinstance(entry, dict) and 
                    'filename' in entry and 
                    'line_number' in entry and 
                    'original_text' in entry):
                    valid_entries.append(entry)
            
            if not valid_entries:
                print("❌ Tidak ada entries valid ditemukan.")
                return None
            
            return valid_entries
            
        except FileNotFoundError:
            print(f"❌ File not found: {json_file}")
            return None
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON format: {json_file}")
            return None
        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
            return None

    def group_by_filename(self, entries):
        """Group entries by filename"""
        grouped = defaultdict(list)
        
        for entry in entries:
            filename = entry.get('filename', '').strip()
            if filename:
                grouped[filename].append(entry)
        
        return dict(grouped)

    def preview_split(self, json_file):
        """Preview what files would be created"""
        entries = self.load_json_data(json_file)
        if not entries:
            return
        
        grouped = self.group_by_filename(entries)
        
        print(f"\n📊 Preview for {json_file}:")
        print(f"   Total entries: {len(entries)}")
        print(f"   Will create {len(grouped)} files:")
        print("-" * 60)
        
        for filename, file_entries in grouped.items():
            base_name = os.path.splitext(filename)[0]
            output_name = f"{base_name}.json"
            print(f"   {output_name:<30} ({len(file_entries)} entries)")
        
        print("-" * 60)

    def split_json_file(self, json_file):
        """Split JSON file into separate files per .rpy file"""
        # Load and validate data
        entries = self.load_json_data(json_file)
        if not entries:
            return
        
        # Group by filename
        grouped = self.group_by_filename(entries)
        
        # Show preview
        print(f"\n📊 Split Analysis:")
        print(f"   Input file: {json_file}")
        print(f"   Total entries: {len(entries)}")
        print(f"   Will create {len(grouped)} files:")
        
        for filename, file_entries in grouped.items():
            base_name = os.path.splitext(filename)[0]
            output_name = f"{base_name}.json"
            print(f"     - {output_name} ({len(file_entries)} entries)")
        
        # Confirm
        confirm = input(f"\nProceed with split? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes', 'ya']:
            print("❌ Split cancelled.")
            return
        
        # Create backup if enabled
        if BACKUP_ORIGINAL:
            backup_name = f"{json_file}.backup"
            try:
                with open(json_file, 'r', encoding='utf-8') as src, \
                     open(backup_name, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
                print(f"💾 Backup created: {backup_name}")
            except Exception as e:
                print(f"⚠️ Warning: Could not create backup: {e}")
        
        # Create individual files
        self.files_created = 0
        self.total_entries = 0
        self.errors = []
        
        for filename, file_entries in grouped.items():
            base_name = os.path.splitext(filename)[0]
            output_name = f"{base_name}.json"
            
            try:
                # Check if file already exists
                if os.path.exists(output_name):
                    print(f"⚠️  File exists: {output_name} - overwriting...")
                
                # Write individual JSON file
                with open(output_name, 'w', encoding='utf-8') as f:
                    json.dump(file_entries, f, indent=2, ensure_ascii=False)
                
                print(f"✅ Created: {output_name} ({len(file_entries)} entries)")
                self.files_created += 1
                self.total_entries += len(file_entries)
                
            except Exception as e:
                error_msg = f"Error creating {output_name}: {e}"
                print(f"❌ {error_msg}")
                self.errors.append(error_msg)
        
        # Show results
        self.show_split_results(json_file)

    def show_split_results(self, original_file):
        """Show split results"""
        print("\n" + "=" * 60)
        print("🎯 SPLIT RESULTS:")
        print(f"   Original file: {original_file}")
        print(f"   Files created: {self.files_created}")
        print(f"   Total entries processed: {self.total_entries}")
        print(f"   Errors: {len(self.errors)}")
        
        if self.errors:
            print(f"\n⚠️ Errors encountered:")
            for error in self.errors[:3]:
                print(f"   - {error}")
            if len(self.errors) > 3:
                print(f"   ... and {len(self.errors) - 3} more")
        
        if self.files_created > 0:
            print(f"\n✅ SUCCESS!")
            print(f"   Individual JSON files created for each .rpy file")
            print(f"   You can now translate each file separately")
            print(f"\n🎯 NEXT STEPS:")
            print(f"   1. Translate individual JSON files (manually or using translate.py)")
            print(f"   2. Apply translations using apply.py")
            print(f"   3. Test the translated .rpy files")

def main():
    splitter = JSONSplitter()
    
    if len(sys.argv) == 1:
        # Interactive menu mode
        splitter.show_main_menu()
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        
        if filename.lower() in ['help', '--help', '-h']:
            print("🔧 JSON SPLITTER v1.0")
            print("Usage:")
            print(f"  python {sys.argv[0]}           # Interactive menu")
            print(f"  python {sys.argv[0]} file.json # Direct split")
            print(f"  python {sys.argv[0]} help      # Show this help")
        elif os.path.exists(filename) and filename.endswith('.json'):
            print(f"🔧 Direct split mode: {filename}")
            splitter.split_json_file(filename)
        else:
            print(f"❌ File not found or not a JSON file: {filename}")
    else:
        print("❌ Too many arguments.")
        print(f"Usage: python {sys.argv[0]} [filename.json]")

if __name__ == "__main__":
    main()