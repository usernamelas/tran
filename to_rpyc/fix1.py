#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RenPy File Fixer - Memperbaiki masalah syntax dan encoding dalam file .rpy
Author: Assistant
Description: Script untuk memperbaiki berbagai masalah dalam file Ren'Py
"""

import re
import os
import sys
from typing import List, Tuple

class RenPyFixer:
    def __init__(self):
        self.fixes_applied = []
        self.line_count = 0
        
    def fix_quotes(self, text: str) -> str:
        """Memperbaiki kutip yang tidak standar"""
        # Ganti kutip Unicode dengan kutip ASCII
        text = text.replace('"', '"')
        text = text.replace('"', '"')
        text = text.replace(''', "'")
        text = text.replace(''', "'")
        return text
    
    def fix_dialog_format(self, line: str) -> str:
        """Memperbaiki format dialog yang rusak"""
        # Pattern untuk dialog yang rusak
        patterns = [
            # Perbaiki dialog tanpa penutup kutip
            (r'p "{i}\*([^"]*)"([^"]*)', r'p "{i}*\1"\2'),
            
            # Perbaiki dialog yang digabung
            (r'"([^"]*)"\.([A-Z][^"]*)"([^"]*)"', r'"\1."\n\2 "\3"'),
            
            # Perbaiki dialog dengan kutip ganda di tengah
            (r'"([^"]*)"([^"]*)"([^"]*)"', r'"\1\2\3"'),
            
            # Perbaiki tag italic yang tidak ditutup
            (r'"{i}([^"}]*)"([^}]*)', r'"{i}\1{/i}"\2'),
        ]
        
        for pattern, replacement in patterns:
            if re.search(pattern, line):
                line = re.sub(pattern, replacement, line)
                
        return line
    
    def fix_character_names(self, line: str) -> str:
        """Memperbaiki format nama karakter"""
        # Pattern untuk nama karakter yang mungkin rusak
        if re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s+"', line):
            # Format sudah benar: karakter "dialog"
            return line
        
        # Perbaiki nama karakter dengan spasi
        line = re.sub(r'^"([^"]+)"\s+"([^"]*)"', r'"\1" "\2"', line)
        
        return line
    
    def fix_commands(self, line: str) -> str:
        """Memperbaiki command Ren'Py yang mungkin rusak"""
        # Perbaiki command show/hide/scene yang rusak
        if line.strip().startswith(('show ', 'hide ', 'scene ')):
            # Pastikan format yang benar untuk transformasi
            line = re.sub(r'with\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\)', r'with \1(\2)', line)
        
        # Perbaiki play sound command
        if 'play sound' in line:
            line = re.sub(r'play sound ([a-zA-Z_][a-zA-Z0-9_]*) loop', r'play sound \1 loop', line)
        
        return line
    
    def fix_labels(self, line: str) -> str:
        """Memperbaiki format label"""
        if line.strip().startswith('label '):
            # Pastikan label diakhiri dengan ":"
            if not line.strip().endswith(':'):
                line = line.rstrip() + ':\n'
        
        return line
    
    def fix_indentation(self, line: str) -> str:
        """Perbaiki indentasi yang mungkin rusak"""
        # Ren'Py menggunakan 4 spasi untuk indentasi
        if line.startswith('\t'):
            # Ganti tab dengan 4 spasi
            line = line.replace('\t', '    ')
        
        return line
    
    def fix_special_characters(self, line: str) -> str:
        """Perbaiki karakter khusus yang mungkin menyebabkan masalah"""
        # Ganti karakter Unicode yang bermasalah
        replacements = {
            '…': '...',
            '–': '-',
            '—': '--',
            '„': '"',
            '‚': "'",
        }
        
        for old, new in replacements.items():
            line = line.replace(old, new)
        
        return line
    
    def validate_line(self, line: str) -> Tuple[bool, str]:
        """Validasi line untuk masalah umum"""
        errors = []
        
        # Check for unmatched quotes
        quote_count = line.count('"')
        if quote_count % 2 != 0 and not line.strip().startswith('#'):
            errors.append("Unmatched quotes")
        
        # Check for unclosed tags
        if '{i}' in line and '{/i}' not in line and '"{i}' not in line:
            errors.append("Unclosed italic tag")
        
        if '{b}' in line and '{/b}' not in line:
            errors.append("Unclosed bold tag")
        
        # Check for invalid characters in labels
        if line.strip().startswith('label '):
            label_name = line.strip()[6:].rstrip(':')
            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', label_name):
                errors.append("Invalid label name")
        
        return len(errors) == 0, "; ".join(errors)
    
    def process_file(self, input_file: str, output_file: str = None) -> bool:
        """Memproses file dan memperbaiki masalah"""
        if not os.path.exists(input_file):
            print(f"Error: File {input_file} tidak ditemukan!")
            return False
        
        if output_file is None:
            output_file = input_file.replace('.rpy', '_fixed.rpy')
        
        try:
            # Baca file dengan encoding UTF-8
            with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
            
            print(f"Memproses {len(lines)} baris...")
            self.line_count = len(lines)
            
            fixed_lines = []
            errors_found = []
            
            for i, line in enumerate(lines, 1):
                original_line = line
                
                # Apply fixes
                line = self.fix_quotes(line)
                line = self.fix_special_characters(line)
                line = self.fix_indentation(line)
                line = self.fix_dialog_format(line)
                line = self.fix_character_names(line)
                line = self.fix_commands(line)
                line = self.fix_labels(line)
                
                # Validate line
                is_valid, error_msg = self.validate_line(line)
                if not is_valid:
                    errors_found.append(f"Line {i}: {error_msg}")
                
                # Track changes
                if line != original_line:
                    self.fixes_applied.append(f"Line {i}: Fixed formatting issues")
                
                fixed_lines.append(line)
            
            # Tulis file yang sudah diperbaiki
            with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
                f.writelines(fixed_lines)
            
            # Print summary
            print(f"\n=== SUMMARY ===")
            print(f"File berhasil diproses: {input_file}")
            print(f"File output: {output_file}")
            print(f"Total baris: {self.line_count}")
            print(f"Perbaikan diterapkan: {len(self.fixes_applied)}")
            
            if errors_found:
                print(f"\n=== ERRORS FOUND ===")
                for error in errors_found[:10]:  # Show first 10 errors
                    print(error)
                if len(errors_found) > 10:
                    print(f"... dan {len(errors_found) - 10} error lainnya")
            
            if self.fixes_applied:
                print(f"\n=== FIXES APPLIED ===")
                for fix in self.fixes_applied[:10]:  # Show first 10 fixes
                    print(fix)
                if len(self.fixes_applied) > 10:
                    print(f"... dan {len(self.fixes_applied) - 10} perbaikan lainnya")
            
            return True
            
        except Exception as e:
            print(f"Error saat memproses file: {str(e)}")
            return False
    
    def fix_specific_issues(self, lines: List[str]) -> List[str]:
        """Memperbaiki masalah spesifik yang ditemukan dalam file"""
        fixed_lines = []
        
        for line in lines:
            # Fix specific broken dialogs found in the file
            if 'p "{i}*menghela napas."' in line:
                line = line.replace('p "{i}*menghela napas."', 'p "{i}*menghela napas.{/i}"')
            
            if '"separate dorms."Pria adalah sarang' in line:
                line = line.replace('"separate dorms."Pria adalah sarang', '"Asrama terpisah. Pria adalah sarang')
            
            if '"thank you and I\'m sorry."Tapi tidak' in line:
                line = line.replace('"thank you and I\'m sorry."Tapi tidak', '"thank you and I\'m sorry." Tapi tidak')
            
            # Fix multiple quotes issues
            line = re.sub(r'""([^"]*)"', r'"\1"', line)
            
            # Fix size tags
            line = re.sub(r'\{size=([^}]+)\}([^{]*)\{/size\}', r'{size=\1}\2{/size}', line)
            
            fixed_lines.append(line)
        
        return fixed_lines

def get_rpy_files(directory: str = ".") -> List[str]:
    """Mendapatkan daftar file .rpy dalam direktori"""
    rpy_files = []
    try:
        for file in os.listdir(directory):
            if file.lower().endswith('.rpy'):
                rpy_files.append(file)
    except OSError as e:
        print(f"Error reading directory: {e}")
    
    return sorted(rpy_files)

def display_menu(files: List[str]) -> str:
    """Menampilkan menu pilihan file"""
    print("\n" + "=" * 60)
    print("🎮 RENPY FILE FIXER v1.0 🛠️")
    print("=" * 60)
    
    if not files:
        print("❌ Tidak ada file .rpy ditemukan di folder ini!")
        print("💡 Pastikan Anda menjalankan script di folder yang berisi file .rpy")
        return None
    
    print(f"📁 Ditemukan {len(files)} file .rpy:")
    print("-" * 60)
    
    for i, file in enumerate(files, 1):
        file_size = os.path.getsize(file) if os.path.exists(file) else 0
        size_mb = file_size / (1024 * 1024)
        print(f"  {i:2d}. {file:<40} ({size_mb:.2f} MB)")
    
    print("-" * 60)
    print("  0.  ❌ Keluar")
    print("=" * 60)
    
    while True:
        try:
            choice = input("\n🔍 Pilih nomor file yang ingin diperbaiki (0 untuk keluar): ").strip()
            
            if choice == '0':
                print("👋 Terima kasih! Sampai jumpa!")
                return None
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(files):
                selected_file = files[choice_num - 1]
                print(f"✅ File terpilih: {selected_file}")
                return selected_file
            else:
                print(f"❌ Pilihan tidak valid! Masukkan angka 1-{len(files)} atau 0 untuk keluar.")
        
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka saja.")
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan oleh user. Bye!")
            return None

def generate_output_filename(input_file: str) -> str:
    """Generate nama file output dengan suffix _fix"""
    name, ext = os.path.splitext(input_file)
    return f"{name}_fix{ext}"

def confirm_process(input_file: str, output_file: str) -> bool:
    """Konfirmasi sebelum memproses file"""
    print(f"\n📋 KONFIRMASI PEMROSESAN:")
    print(f"📥 Input file : {input_file}")
    print(f"📤 Output file: {output_file}")
    
    if os.path.exists(output_file):
        print(f"⚠️  WARNING: File output sudah ada dan akan ditimpa!")
    
    while True:
        confirm = input("\n❓ Lanjutkan proses? (y/n): ").strip().lower()
        if confirm in ['y', 'yes', 'ya']:
            return True
        elif confirm in ['n', 'no', 'tidak']:
            print("❌ Proses dibatalkan.")
            return False
        else:
            print("❌ Masukkan 'y' untuk ya atau 'n' untuk tidak.")

def main():
    """Main function dengan interface yang user-friendly"""
    try:
        # Cari file .rpy di direktori saat ini
        rpy_files = get_rpy_files()
        
        # Tampilkan menu dan ambil pilihan user
        selected_file = display_menu(rpy_files)
        
        if selected_file is None:
            sys.exit(0)
        
        # Generate nama file output
        output_file = generate_output_filename(selected_file)
        
        # Konfirmasi sebelum proses
        if not confirm_process(selected_file, output_file):
            sys.exit(0)
        
        # Proses file
        print(f"\n🔄 Memproses file: {selected_file}")
        print("⏳ Mohon tunggu...")
        
        fixer = RenPyFixer()
        success = fixer.process_file(selected_file, output_file)
        
        if success:
            print(f"\n🎉 FILE BERHASIL DIPERBAIKI!")
            print(f"📁 File hasil: {output_file}")
            print(f"📊 Total baris diproses: {fixer.line_count}")
            print(f"🔧 Total perbaikan: {len(fixer.fixes_applied)}")
            
            # Tanya apakah ingin memproses file lain
            while True:
                another = input(f"\n❓ Ingin memperbaiki file .rpy lain? (y/n): ").strip().lower()
                if another in ['y', 'yes', 'ya']:
                    print("\n" + "🔄" * 20)
                    main()  # Recursive call untuk file lain
                    break
                elif another in ['n', 'no', 'tidak']:
                    print("👋 Terima kasih telah menggunakan RenPy File Fixer!")
                    break
                else:
                    print("❌ Masukkan 'y' untuk ya atau 'n' untuk tidak.")
        else:
            print(f"\n💥 GAGAL MEMPERBAIKI FILE!")
            print("🔍 Cek pesan error di atas untuk detail masalah.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print(f"\n\n👋 Program dihentikan oleh user. Bye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n💥 Error tak terduga: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()