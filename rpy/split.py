import os
import glob
import math
import time
from datetime import datetime

# ==================== BAHASA ====================
TEXT = {
    'id': {
        'title': "🛠️  ALAT PEMISAH & PENGGABUNG FILE TEKS",
        'current_file': "File saat ini",
        'no_file': "(belum dipilih)",
        'menu': [
            "1. Pilih file",
            "2. Pisahkan file (by LINE COUNT)",
            "3. Gabungkan file *_part*",
            "4. Ganti bahasa (ID/EN)",
            "5. Keluar"
        ],
        'choose_file': "📂 Daftar file teks di folder ini:",
        'no_supported_files': "❌ Tidak ada file teks yang didukung!",
        'supported_formats': "Format yang didukung",
        'invalid_choice': "❌ Pilihan tidak valid!",
        'split_title': "🔪 MEMISAHKAN FILE (BY LINES)",
        'split_enter_lines': "Jumlah lines per file (default 3000): ",
        'stats': "📊 Statistik:",
        'total_lines': "Total lines (termasuk kosong)",
        'will_create': "Akan dibuat {} file part",
        'created': "✔ Dibuat: {} ({} lines)",
        'merge_title': "🧲 MODE PENGGABUNGAN",
        'no_part_files': "❌ Tidak ada file part ditemukan!",
        'part_list': "Daftar file part:",
        'enter_output_name': "Nama file hasil gabungan (tanpa ekstensi): ",
        'default_output': "gabungan",
        'merge_success': "✅ Berhasil dibuat: {}",
        'language_change': "🌐 Bahasa diubah ke: Indonesia"
    },
    'en': {
        'title': "🛠️  TEXT FILE SPLITTER & MERGER TOOL",
        'current_file': "Current file",
        'no_file': "(not selected)",
        'menu': [
            "1. Select file",
            "2. Split file (by LINE COUNT)",
            "3. Merge *_part* files",
            "4. Change language (EN/ID)",
            "5. Exit"
        ],
        'choose_file': "📂 Text files in current folder:",
        'no_supported_files': "❌ No supported text files found!",
        'supported_formats': "Supported formats",
        'invalid_choice': "❌ Invalid choice!",
        'split_title': "🔪 SPLITTING FILE (BY LINES)",
        'split_enter_lines': "Lines per file (default 3000): ",
        'stats': "📊 Statistics:",
        'total_lines': "Total lines (including empty)",
        'will_create': "Will create {} part files",
        'created': "✔ Created: {} ({} lines)",
        'merge_title': "🧲 MERGE MODE",
        'no_part_files': "❌ No part files found!",
        'part_list': "Part files list:",
        'enter_output_name': "Output file name (without extension): ",
        'default_output': "merged",
        'merge_success': "✅ Successfully created: {}",
        'language_change': "🌐 Language changed to: English"
    }
}

# Default language
LANG = 'id'

def t(key):
    """Get translated text"""
    return TEXT[LANG].get(key, key)

# ==================== FUNGSI UTAMA ====================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu(nama_file=None):
    """Menampilkan menu utama"""
    print("\n" + "="*40)
    print(t('title'))
    print("="*40)
    if nama_file:
        print(f"{t('current_file')}: {nama_file}")
    else:
        print(f"{t('current_file')}: {t('no_file')}")
    print("="*40)
    for item in t('menu'):
        print(item)
    print("="*40)

def pilih_file():
    """Memilih file teks"""
    print(f"\n{t('choose_file')}")
    ekstensi = ('.txt', '.json', '.rpy', '.rpym', '.xml', '.csv', '.doc', '.log')
    files = [f for f in os.listdir() if f.lower().endswith(ekstensi)]
    
    if not files:
        print(f"{t('no_supported_files')}")
        print(f"{t('supported_formats')}: {', '.join(ekstensi)}")
        return None
    
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    try:
        pilihan = int(input("\nPilih nomor file: " if LANG == 'id' else "\nSelect file number: "))
        return files[pilihan-1]
    except (ValueError, IndexError):
        print(t('invalid_choice'))
        return None

def hitung_total_lines(nama_file):
    """Menghitung total lines termasuk kosong"""
    with open(nama_file, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

def split_file_by_lines(nama_file):
    """Membagi file teks berdasarkan line count"""
    if not nama_file:
        print("❌ Harap pilih file terlebih dahulu!" if LANG == 'id' else "❌ Please select a file first!")
        return
    
    print(f"\n{t('split_title')}: {nama_file}")
    
    try:
        prompt = t('split_enter_lines')
        max_lines = int(input(prompt) or 3000)
    except ValueError:
        max_lines = 3000
    
    total_lines = hitung_total_lines(nama_file)
    num_files = math.ceil(total_lines / max_lines)
    
    print(f"\n{t('stats')}")
    print(f"- {t('total_lines')}: {total_lines}")
    print(f"- {t('will_create').format(num_files)}")
    
    with open(nama_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i in range(num_files):
        part_lines = lines[i*max_lines : (i+1)*max_lines]
        nama, ext = os.path.splitext(nama_file)
        output_file = f"{nama}_part{i+1}{ext}"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(part_lines)
        
        print(t('created').format(output_file, len(part_lines)))

def merge_files():
    """Gabungkan file part"""
    print(f"\n{t('merge_title')}")
    files = sorted(glob.glob("*_part*.*"))
    
    if not files:
        print(t('no_part_files'))
        return
    
    print(t('part_list'))
    for f in files:
        print(f"- {f}")
    
    nama_output = input(f"\n{t('enter_output_name')}").strip()
    if not nama_output:
        nama_output = t('default_output')
    
    ext = os.path.splitext(files[0])[1]
    output_file = f"{nama_output}{ext}"
    
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file in files:
            with open(file, 'r', encoding='utf-8') as in_f:
                out_f.writelines(in_f.readlines())
            print(f"✔ {'Ditambahkan' if LANG == 'id' else 'Added'}: {file}")
    
    print(f"\n{t('merge_success').format(output_file)}")
    print(f"Total lines: {hitung_total_lines(output_file)}")

def ganti_bahasa():
    """Ganti bahasa Indonesia/English"""
    global LANG
    LANG = 'en' if LANG == 'id' else 'id'
    print(f"\n{t('language_change')}")
    time.sleep(1)

def main():
    """Program utama"""
    clear_screen()
    current_file = None
    
    while True:
        tampilkan_menu(current_file)
        choice = input("Pilih menu (1-5): " if LANG == 'id' else "Select option (1-5): ").strip()
        
        if choice == "1":
            current_file = pilih_file()
        elif choice == "2":
            split_file_by_lines(current_file)
        elif choice == "3":
            merge_files()
        elif choice == "4":
            ganti_bahasa()
        elif choice == "5":
            print("\n👋 Sampai jumpa!" if LANG == 'id' else "\n👋 Goodbye!")
            break
        else:
            print(t('invalid_choice'))
        
        input("\nTekan Enter untuk melanjutkan..." if LANG == 'id' else "\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()