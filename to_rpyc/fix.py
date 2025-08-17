import os
import re

def list_rpy_files():
    """Mencari semua file .rpy di direktori saat ini"""
    rpy_files = [f for f in os.listdir('.') if f.endswith('.rpy')]
    return rpy_files

def show_menu(files):
    """Menampilkan menu pilihan file"""
    print("\nDaftar file .rpy yang ditemukan:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    print("0. Keluar")
    
    while True:
        try:
            choice = int(input("\nPilih file yang ingin diperbaiki (nomor): "))
            if 0 <= choice <= len(files):
                return choice
            print("Pilihan tidak valid!")
        except ValueError:
            print("Masukkan angka saja!")

def fix_rpy_file(filename):
    """Memperbaiki masalah tanda kutip pada file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Perbaikan utama:
        # 1. Ganti ""text" menjadi "text"
        content = re.sub(r'""(.+?)""', r'"\1"', content)
        # 2. Perbaiki escape quotes yang salah
        content = re.sub(r'\\"', '"', content)
        # 3. Pastikan setiap baris dialog diawali dengan karakter dan "
        content = re.sub(r'^([a-zA-Z0-9_]+)\s+""', r'\1 "', content, flags=re.MULTILINE)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"\n✅ File {filename} berhasil diperbaiki!")
    except Exception as e:
        print(f"\n❌ Gagal memperbaiki {filename}: {str(e)}")

def main():
    print("=== RPY File Fixer ===")
    files = list_rpy_files()
    
    if not files:
        print("Tidak ditemukan file .rpy di folder ini!")
        return
    
    while True:
        choice = show_menu(files)
        if choice == 0:
            print("Keluar...")
            break
            
        file_to_fix = files[choice-1]
        print(f"\nMemperbaiki file: {file_to_fix}...")
        fix_rpy_file(file_to_fix)
        
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()