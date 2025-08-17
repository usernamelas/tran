import os
import re
from pathlib import Path

def list_rpy_files():
    """Daftar file .rpy di folder saat ini (tanpa file hasil perbaikan)"""
    return [f for f in os.listdir('.') 
            if f.endswith('.rpy') 
            and not f.startswith('fixed_')]

def create_fixed_file(original_path):
    """Buat file baru dengan awalan 'fixed_'"""
    fixed_name = f"fixed_{original_path}"
    counter = 1
    while os.path.exists(fixed_name):
        fixed_name = f"fixed_{counter}_{original_path}"
        counter += 1
    return fixed_name

def fix_content(content):
    """Perbaiki konten file"""
    # 1. Perbaiki tanda kutip ganda
    content = re.sub(r'""\s*(.*?)\s*""', r'"\1"', content, flags=re.DOTALL)
    
    # 2. Perbaiki escape quotes
    content = re.sub(r'(?<!\\)\\"', '"', content)
    
    # 3. Normalisasi definisi karakter
    content = re.sub(r"u'#([0-9a-f]{6})'", r"'\#\1'", content, flags=re.IGNORECASE)
    
    return content

def process_file(original_file):
    """Proses file dan simpan sebagai file baru"""
    try:
        # Baca file asli
        with open(original_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Buat file perbaikan
        fixed_file = create_fixed_file(original_file)
        fixed_content = fix_content(original_content)
        
        # Tulis file baru
        with open(fixed_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✅ Hasil disimpan di: {fixed_file}")
        print(f"   Ukuran: {os.path.getsize(fixed_file)/1024:.1f} KB")
        return True
    
    except Exception as e:
        print(f"❌ Gagal memproses {original_file}: {str(e)}")
        return False

def main():
    print("=== RPY File Fixer (Mode Aman) ===")
    print("Akan membuat file baru dengan awalan 'fixed_'")
    
    files = list_rpy_files()
    if not files:
        print("Tidak ditemukan file .rpy di folder ini!")
        return
    
    while True:
        # Tampilkan menu
        print("\nDaftar file:")
        for i, f in enumerate(files, 1):
            size = os.path.getsize(f)/1024
            print(f"{i}. {f} ({size:.1f} KB)")
        print("0. Keluar")
        
        # Input pilihan
        try:
            choice = int(input("Pilih file (0 untuk keluar): "))
            if choice == 0:
                break
            if 1 <= choice <= len(files):
                selected = files[choice-1]
                print(f"\nMemproses: {selected}...")
                process_file(selected)
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Harap masukkan angka!")

if __name__ == "__main__":
    main()