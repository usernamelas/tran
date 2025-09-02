#!/usr/bin/env python3
import os
import re
import json
import subprocess
import time
from pathlib import Path

# Konfigurasi
COLOR = {
    "merah": "\033[91m",
    "hijau": "\033[92m",
    "kuning": "\033[93m",
    "biru": "\033[94m",
    "reset": "\033[0m"
}

FORMAT_FILE = ('.json', '.txt', '.rpy', '.rpym', '.xml', '.ini', '.yaml', '.po')

# Konfigurasi untuk mencegah rate limiting
DELAY_BETWEEN_REQUESTS = 1  # Delay 1 detik antara permintaan terjemahan
MAX_RETRIES = 3  # Jumlah maksimal percobaan ulang jika gagal

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header():
    print(f"{COLOR['biru']}")
    print("="*60)
    print(" ALAT PENERJEMAH FILE GAME/APK ".center(60))
    print("="*60)
    print(f"{COLOR['reset']}")
    print(f"Format didukung: {', '.join(FORMAT_FILE)}\n")

def pilih_file():
    files = [f for f in os.listdir() if f.lower().endswith(FORMAT_FILE)]
    
    if not files:
        print(f"{COLOR['merah']}Tidak ada file yang didukung ditemukan!{COLOR['reset']}")
        return None
    
    print("File yang tersedia:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    try:
        pilihan = int(input("\nPilih nomor file: ")) - 1
        return files[pilihan]
    except (ValueError, IndexError):
        print(f"{COLOR['merah']}Input tidak valid!{COLOR['reset']}")
        return None

def tampilkan_contoh(nama_file, jumlah=10):
    print(f"\n{COLOR['kuning']}Contoh isi file (10 baris pertama):{COLOR['reset']}")
    
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            for i in range(jumlah):
                line = f.readline()
                if not line:
                    break
                print(f"{i+1}. {line.strip()}")
    except UnicodeDecodeError:
        print(f"{COLOR['merah']}File tidak bisa dibaca sebagai teks!{COLOR['reset']}")
        return False
    return True

def pilih_bahasa():
    print("\nDaftar kode bahasa:")
    print("en - English")
    print("id - Indonesia")
    print("ja - Jepang")
    print("zh - Mandarin")
    print("ko - Korea")
    print("es - Spanyol")
    print("fr - Prancis")
    
    dari_bahasa = input("\nDari bahasa (kode): ").strip()
    ke_bahasa = input("Ke bahasa (kode): ").strip()
    
    return dari_bahasa, ke_bahasa

def input_nama_output(nama_file):
    nama, ext = os.path.splitext(nama_file)
    while True:
        nama_output = input(f"\nNama file output (tanpa ekstensi, default 'terjemahan_{nama}'): ").strip()
        if not nama_output:
            return f"terjemahan_{nama}{ext}"
        if not any(c in nama_output for c in '\\/:*?"<>|'):
            return f"{nama_output}{ext}"
        print(f"{COLOR['merah']}Nama file tidak boleh mengandung karakter khusus!{COLOR['reset']}")

def terjemahkan_teks(teks, dari_bahasa, ke_bahasa, retry_count=0):
    try:
        # Skip jika teks kosong atau hanya spasi
        if not teks or teks.isspace():
            return teks
            
        hasil = subprocess.run(
            ["trans", "-b", f"{dari_bahasa}:{ke_bahasa}", teks],
            capture_output=True,
            text=True,
            timeout=30,  # Timeout 30 detik
            check=True
        )
        return hasil.stdout.strip()
    except subprocess.CalledProcessError as e:
        if retry_count < MAX_RETRIES:
            print(f"{COLOR['kuning']}Percobaan ulang {retry_count+1}/{MAX_RETRIES} untuk: {teks[:50]}...{COLOR['reset']}")
            time.sleep(DELAY_BETWEEN_REQUESTS * 2)  # Tunggu lebih lama untuk percobaan ulang
            return terjemahkan_teks(teks, dari_bahasa, ke_bahasa, retry_count + 1)
        print(f"{COLOR['merah']}Error menerjemahkan setelah {MAX_RETRIES} percobaan: {teks[:50]}...{COLOR['reset']}")
        return teks  # Kembalikan teks asli jika gagal
    except subprocess.TimeoutExpired:
        if retry_count < MAX_RETRIES:
            print(f"{COLOR['kuning']}Timeout, percobaan ulang {retry_count+1}/{MAX_RETRIES} untuk: {teks[:50]}...{COLOR['reset']}")
            time.sleep(DELAY_BETWEEN_REQUESTS * 2)
            return terjemahkan_teks(teks, dari_bahasa, ke_bahasa, retry_count + 1)
        print(f"{COLOR['merah']}Timeout setelah {MAX_RETRIES} percobaan: {teks[:50]}...{COLOR['reset']}")
        return teks
    except Exception as e:
        print(f"{COLOR['merah']}Error tidak terduga: {e}{COLOR['reset']}")
        return teks

def proses_json(nama_file, dari_bahasa, ke_bahasa, nama_output):
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"{COLOR['merah']}File JSON tidak valid!{COLOR['reset']}")
        return False
    
    contoh_diterjemahkan = 0
    hasil = {}
    
    print(f"\n{COLOR['hijau']}Contoh hasil terjemahan:{COLOR['reset']}")
    for k, v in list(data.items())[:10]:
        if isinstance(v, str):
            terjemahan = terjemahkan_teks(v, dari_bahasa, ke_bahasa)
            hasil[k] = terjemahan
            print(f'"{k}": "{v}" -> "{terjemahan}"')
            contoh_diterjemahkan += 1
            time.sleep(DELAY_BETWEEN_REQUESTS)  # Delay untuk contoh juga
    
    if contoh_diterjemahkan == 0:
        print(f"{COLOR['merah']}Tidak ada teks yang bisa diterjemahkan!{COLOR['reset']}")
        return False
    
    while True:
        print("\nPilihan:")
        print("1. Lanjutkan terjemahan seluruh file")
        print("2. Pilih ulang bahasa")
        print("3. Batalkan")
        
        pilihan = input("Pilihan Anda (1-3): ")
        
        if pilihan == '1':
            total = len(data)
            for i, (k, v) in enumerate(data.items(), 1):
                if isinstance(v, str):
                    hasil[k] = terjemahkan_teks(v, dari_bahasa, ke_bahasa)
                    print(f"{COLOR['hijau']}[{i}/{total}] {COLOR['reset']}{k}: {hasil[k][:50]}...")
                    time.sleep(DELAY_BETWEEN_REQUESTS)  # Delay untuk mencegah rate limiting
                else:
                    hasil[k] = v  # Simpan nilai non-string apa adanya
            
            with open(nama_output, 'w', encoding='utf-8') as f:
                json.dump(hasil, f, indent=2, ensure_ascii=False)
            
            print(f"\n{COLOR['hijau']}File hasil disimpan sebagai: {nama_output}{COLOR['reset']}")
            return True
            
        elif pilihan == '2':
            return 'ubah_bahasa'
        elif pilihan == '3':
            return False
        else:
            print(f"{COLOR['merah']}Pilihan tidak valid!{COLOR['reset']}")

def proses_teks(nama_file, dari_bahasa, ke_bahasa, nama_output):
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"{COLOR['merah']}File tidak bisa dibaca sebagai teks!{COLOR['reset']}")
        return False
    
    pola_rpy = re.compile(r'(old|new) "(.+)"')
    pola_umum = re.compile(r'"(.*?)"')
    
    contoh_diterjemahkan = 0
    hasil = []
    
    print(f"\n{COLOR['hijau']}Contoh hasil terjemahan:{COLOR['reset']}")
    for line in lines[:10]:
        line = line.strip()
        if not line:
            continue
            
        match = pola_rpy.search(line)
        if match:
            tipe, teks = match.groups()
            if tipe == 'new' and teks:
                terjemahan = terjemahkan_teks(teks, dari_bahasa, ke_bahasa)
                print(f"{line} -> {line.replace(teks, terjemahan)}")
                contoh_diterjemahkan += 1
                time.sleep(DELAY_BETWEEN_REQUESTS)  # Delay untuk contoh juga
                continue
        
        matches = pola_umum.findall(line)
        if matches:
            for teks in matches:
                if teks.strip():
                    terjemahan = terjemahkan_teks(teks, dari_bahasa, ke_bahasa)
                    print(f'"{teks}" -> "{terjemahan}"')
                    contoh_diterjemahkan += 1
                    time.sleep(DELAY_BETWEEN_REQUESTS)  # Delay untuk contoh juga
    
    if contoh_diterjemahkan == 0:
        print(f"{COLOR['merah']}Tidak menemukan teks yang bisa diterjemahkan!{COLOR['reset']}")
        return False
    
    while True:
        print("\nPilihan:")
        print("1. Lanjutkan terjemahan seluruh file")
        print("2. Pilih ulang bahasa")
        print("3. Batalkan")
        
        pilihan = input("Pilihan Anda (1-3): ")
        
        if pilihan == '1':
            total = len(lines)
            for i, line in enumerate(lines, 1):
                line_original = line.rstrip()
                line_processed = line_original
                
                # Proses Ren'Py
                match = pola_rpy.search(line_original)
                if match:
                    tipe, teks = match.groups()
                    if tipe == 'new' and teks:
                        terjemahan = terjemahkan_teks(teks, dari_bahasa, ke_bahasa)
                        line_processed = line_original.replace(f'"{teks}"', f'"{terjemahan}"')
                        time.sleep(DELAY_BETWEEN_REQUESTS)
                
                # Proses teks umum
                else:
                    matches = pola_umum.findall(line_original)
                    for teks in matches:
                        if teks.strip():
                            terjemahan = terjemahkan_teks(teks, dari_bahasa, ke_bahasa)
                            line_processed = line_processed.replace(f'"{teks}"', f'"{terjemahan}"')
                            time.sleep(DELAY_BETWEEN_REQUESTS)
                
                hasil.append(line_processed + '\n')
                print(f"{COLOR['hijau']}[{i}/{total}] {COLOR['reset']}Diproses...")
            
            with open(nama_output, 'w', encoding='utf-8') as f:
                f.writelines(hasil)
            
            print(f"\n{COLOR['hijau']}File hasil disimpan sebagai: {nama_output}{COLOR['reset']}")
            return True
            
        elif pilihan == '2':
            return 'ubah_bahasa'
        elif pilihan == '3':
            return False
        else:
            print(f"{COLOR['merah']}Pilihan tidak valid!{COLOR['reset']}")

def main():
    bersihkan_layar()
    tampilkan_header()
    
    while True:
        file = pilih_file()
        if not file:
            break
        
        if not tampilkan_contoh(file):
            continue
        
        dari_bahasa, ke_bahasa = pilih_bahasa()
        nama_output = input_nama_output(file)
        
        while True:
            if file.endswith('.json'):
                result = proses_json(file, dari_bahasa, ke_bahasa, nama_output)
            else:
                result = proses_teks(file, dari_bahasa, ke_bahasa, nama_output)
            
            if result == 'ubah_bahasa':
                dari_bahasa, ke_bahasa = pilih_bahasa()
                continue
            else:
                break
        
        lagi = input("\nTerjemahkan file lain? (y/n): ").lower()
        if lagi != 'y':
            break
        
        bersihkan_layar()
        tampilkan_header()
    
    print(f"\n{COLOR['biru']}Program selesai. Terima kasih!{COLOR['reset']}")

if __name__ == "__main__":
    try:
        subprocess.run(["trans", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print(f"{COLOR['merah']}Error: translate-shell (trans) tidak ditemukan!")
        print("Silakan install dengan perintah:")
        print("sudo apt install translate-shell")
        exit(1)
    except subprocess.CalledProcessError:
        print(f"{COLOR['merah']}Error: translate-shell (trans) tidak berfungsi dengan baik!")
        print("Pastikan trans terinstall dengan benar.")
        exit(1)
    
    main()
