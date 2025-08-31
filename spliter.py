import os
import glob
import math

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu(nama_file=None):
    """Menampilkan menu utama"""
    print("\n" + "="*40)
    print("🛠️  ALAT PEMISAH & PENGGABUNG FILE TEKS")
    print("="*40)
    if nama_file:
        print(f"File saat ini: {nama_file}")
    else:
        print("File saat ini: (belum dipilih)")
    print("="*40)
    print("1. Pilih file")
    print("2. Pisahkan file (by LINE COUNT)")
    print("3. Gabungkan file *_part*")
    print("4. Keluar")
    print("="*40)

def pilih_file():
    """Memilih file teks (support .txt, .json, .rpy, .xml, dll)"""
    print("\n📂 Daftar file teks di folder ini:")
    # Support ekstensi umum file teks
    ekstensi = ('.txt', '.json', '.rpy', '.xml', '.csv', '.doc', '.log')
    files = [f for f in os.listdir() if f.lower().endswith(ekstensi)]
    
    if not files:
        print("❌ Tidak ada file teks yang didukung!")
        print("Format yang didukung: .txt, .json, .rpy, .xml, .csv, .doc, .log")
        return None
    
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    try:
        pilihan = int(input("\nPilih nomor file: "))
        return files[pilihan-1]
    except (ValueError, IndexError):
        print("❌ Pilihan tidak valid!")
        return None

def hitung_total_lines(nama_file):
    """Menghitung total lines termasuk baris kosong"""
    with open(nama_file, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

def split_file_by_lines(nama_file):
    """Membagi file teks berdasarkan line count"""
    if not nama_file:
        print("❌ Harap pilih file terlebih dahulu!")
        return
    
    print(f"\n🔪 MEMISAHKAN FILE (BY LINES): {nama_file}")
    
    try:
        max_lines = int(input("Jumlah lines per file (default 3000): ") or 3000)
    except ValueError:
        print("⚠️ Input tidak valid! Menggunakan default 3000")
        max_lines = 3000
    
    total_lines = hitung_total_lines(nama_file)
    num_files = math.ceil(total_lines / max_lines)
    
    print(f"\n📊 Statistik:")
    print(f"- File input  : {nama_file}")
    print(f"- Total lines : {total_lines}")
    print(f"- Jumlah file : {num_files}")
    print(f"- Lines/file  : ~{max_lines}")
    
    confirm = input("\nLanjutkan? (y/n): ").lower()
    if confirm != 'y':
        return
    
    print("\n🚀 Memulai proses...")
    with open(nama_file, 'r', encoding='utf-8') as f:
        for i in range(num_files):
            # Pertahankan ekstensi file asli
            nama, ext = os.path.splitext(nama_file)
            output_file = f"{nama}_part{i+1}{ext}"
            
            with open(output_file, 'w', encoding='utf-8') as out_f:
                lines_written = 0
                while lines_written < max_lines:
                    line = f.readline()
                    if not line:
                        break
                    out_f.write(line)
                    lines_written += 1
            print(f"✔ Dibuat: {output_file} ({lines_written} lines)")
    
    print("\n✅ Proses selesai!")

def merge_files():
    """Menggabungkan file teks yang terpisah"""
    print("\n🧲 MODE PENGGABUNGAN FILE")
    # Cari file dengan pola *_part*.* (pertahankan ekstensi asli)
    files = sorted(glob.glob("*_part*.*"))
    
    if not files:
        print("\n❌ Tidak ditemukan file dengan pola '*_part*'")
        return
    
    print("\n📋 Daftar file yang akan digabung:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    confirm = input("\nLanjutkan? (y/n): ").lower()
    if confirm != 'y':
        return
    
    # Pertahankan ekstensi file pertama
    ext = os.path.splitext(files[0])[1]
    output_file = f"GABUNGAN{ext}"
    
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file in files:
            with open(file, 'r', encoding='utf-8') as in_f:
                out_f.write(in_f.read())
    
    print(f"\n🎉 Berhasil dibuat: {output_file}")
    print(f"Total lines: {hitung_total_lines(output_file)}")

def main():
    """Program utama"""
    clear_screen()
    print("✨ Selamat datang di Text File Split & Merge Tool ✨")
    current_file = None
    
    while True:
        tampilkan_menu(current_file)
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == "1":
            current_file = pilih_file()
        elif pilihan == "2":
            split_file_by_lines(current_file)
        elif pilihan == "3":
            merge_files()
        elif pilihan == "4":
            print("\n👋 Sampai jumpa!")
            break
        else:
            print("\n⚠️ Pilihan tidak valid! Silakan coba lagi")
        
        input("\nTekan Enter untuk kembali ke menu...")
        clear_screen()

if __name__ == "__main__":
    main()