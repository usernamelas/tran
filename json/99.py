#!/usr/bin/env python3
import os
import re
import json
import subprocess
import time
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

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
DELAY_BETWEEN_REQUESTS = 0.5
DELAY_FOR_SHORT_TEXT = 0.1
MAX_RETRIES = 3
MAX_WORKERS = 2

# Global mapping dictionaries
TAG_MAP = {}
VARIABLE_MAP = {}
PAREN_MAP = {}
ANGLE_MAP = {}
mapping_counter = 1

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

def scan_dan_buat_mapping(nama_file):
    """
    Memindai file untuk mencari tag, variable, dan struktur khusus
    lalu membuat mapping untuk dilindungi
    """
    global TAG_MAP, VARIABLE_MAP, PAREN_MAP, ANGLE_MAP, mapping_counter
    
    # Reset mapping
    TAG_MAP = {}
    VARIABLE_MAP = {}
    PAREN_MAP = {}
    ANGLE_MAP = {}
    mapping_counter = 1
    
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"{COLOR['merah']}Tidak bisa memindai file!{COLOR['reset']}")
        return False
    
    # Pattern untuk berbagai jenis struktur
    patterns = {
        'TAG': r'\{[^{}]*\}',          # {tag}, {/tag}, {tag=value}
        'VARIABLE': r'\[[^\[\]]*\]',    # [variable], [variable=value]
        'PAREN': r'\([^()]*\)',         # (text in parentheses)
        'ANGLE': r'<[^<>]*>',           # <text in angle brackets>
    }
    
    print(f"{COLOR['kuning']}Memindai file untuk struktur khusus...{COLOR['reset']}")
    
    # Scan untuk setiap pattern
    for pattern_type, pattern in patterns.items():
        matches = re.findall(pattern, content)
        unique_matches = set(matches)
        
        for match in unique_matches:
            if pattern_type == 'TAG' and match not in TAG_MAP:
                TAG_MAP[match] = f"{{{mapping_counter}}}"
                mapping_counter += 1
            elif pattern_type == 'VARIABLE' and match not in VARIABLE_MAP:
                VARIABLE_MAP[match] = f"[{mapping_counter}]"
                mapping_counter += 1
            elif pattern_type == 'PAREN' and match not in PAREN_MAP:
                PAREN_MAP[match] = f"({mapping_counter})"
                mapping_counter += 1
            elif pattern_type == 'ANGLE' and match not in ANGLE_MAP:
                ANGLE_MAP[match] = f"<{mapping_counter}>"
                mapping_counter += 1
    
    # Simpan mapping ke file
    nama_mapping = f"mapping_{os.path.splitext(nama_file)[0]}.txt"
    with open(nama_mapping, 'w', encoding='utf-8') as f:
        f.write("=== TAG MAPPING ===\n")
        for original, mapped in TAG_MAP.items():
            f.write(f"{mapped} = {original}\n")
        
        f.write("\n=== VARIABLE MAPPING ===\n")
        for original, mapped in VARIABLE_MAP.items():
            f.write(f"{mapped} = {original}\n")
        
        f.write("\n=== PARENTHESES MAPPING ===\n")
        for original, mapped in PAREN_MAP.items():
            f.write(f"{mapped} = {original}\n")
        
        f.write("\n=== ANGLE BRACKETS MAPPING ===\n")
        for original, mapped in ANGLE_MAP.items():
            f.write(f"{mapped} = {original}\n")
    
    print(f"{COLOR['hijau']}Mapping disimpan di: {nama_mapping}{COLOR['reset']}")
    print(f"Ditemukan: {len(TAG_MAP)} tag, {len(VARIABLE_MAP)} variable, "
          f"{len(PAREN_MAP)} parentheses, {len(ANGLE_MAP)} angle brackets")
    
    return True

def lindungi_teks_dengan_mapping(teks):
    """
    Mengganti struktur khusus dengan mapping yang sudah dibuat
    """
    # Urutan penting: yang lebih kompleks dulu
    protected_teks = teks
    
    # Ganti semua struktur dengan mapping
    for original, mapped in ANGLE_MAP.items():
        protected_teks = protected_teks.replace(original, mapped)
    
    for original, mapped in PAREN_MAP.items():
        protected_teks = protected_teks.replace(original, mapped)
    
    for original, mapped in VARIABLE_MAP.items():
        protected_teks = protected_teks.replace(original, mapped)
    
    for original, mapped in TAG_MAP.items():
        protected_teks = protected_teks.replace(original, mapped)
    
    return protected_teks

def kembalikan_teks_dari_mapping(teks):
    """
    Mengembalikan struktur khusus dari mapping ke bentuk asli
    """
    restored_teks = teks
    
    # Urutan penting: yang lebih sederhana dulu
    for original, mapped in TAG_MAP.items():
        restored_teks = restored_teks.replace(mapped, original)
    
    for original, mapped in VARIABLE_MAP.items():
        restored_teks = restored_teks.replace(mapped, original)
    
    for original, mapped in PAREN_MAP.items():
        restored_teks = restored_teks.replace(mapped, original)
    
    for original, mapped in ANGLE_MAP.items():
        restored_teks = restored_teks.replace(mapped, original)
    
    return restored_teks

def terjemahkan_teks(teks, dari_bahasa, ke_bahasa, retry_count=0):
    try:
        # Skip jika teks kosong atau hanya spasi
        if not teks or teks.isspace():
            return teks
        
        # Lindungi teks dengan mapping
        teks_protected = lindungi_teks_dengan_mapping(teks)
            
        hasil = subprocess.run(
            ["trans", "-b", f"{dari_bahasa}:{ke_bahasa}", teks_protected],
            capture_output=True,
            text=True,
            timeout=30,
            check=True
        )
        
        # Kembalikan teks dari mapping
        hasil_terjemahan = hasil.stdout.strip()
        hasil_terjemahan = kembalikan_teks_dari_mapping(hasil_terjemahan)
        
        return hasil_terjemahan
    except subprocess.CalledProcessError as e:
        if retry_count < MAX_RETRIES:
            print(f"{COLOR['kuning']}Percobaan ulang {retry_count+1}/{MAX_RETRIES} untuk: {teks[:50]}...{COLOR['reset']}")
            time.sleep(DELAY_BETWEEN_REQUESTS * 2)
            return terjemahkan_teks(teks, dari_bahasa, ke_bahasa, retry_count + 1)
        print(f"{COLOR['merah']}Error menerjemahkan setelah {MAX_RETRIES} percobaan: {teks[:50]}...{COLOR['reset']}")
        return teks
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

def bagi_file(nama_file, jumlah_bagian):
    """
    Membagi file menjadi beberapa bagian untuk diproses secara paralel
    """
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"{COLOR['merah']}File tidak bisa dibaca sebagai teks!{COLOR['reset']}")
        return None
    
    total_baris = len(lines)
    ukuran_bagian = total_baris // jumlah_bagian
    bagian_bagian = []
    
    for i in range(jumlah_bagian):
        start = i * ukuran_bagian
        if i == jumlah_bagian - 1:
            end = total_baris
        else:
            end = (i + 1) * ukuran_bagian
        bagian_bagian.append((i, lines[start:end]))
    
    return bagian_bagian

def terjemahkan_bagian(bagian_data, dari_bahasa, ke_bahasa):
    """
    Menerjemahkan satu bagian file (dijalankan di thread terpisah)
    """
    nomor_bagian, lines = bagian_data
    hasil_bagian = []
    
    pola_rpy = re.compile(r'(old|new) "(.+)"')
    pola_umum = re.compile(r'"(.*?)"')
    
    for line in lines:
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
        
        hasil_bagian.append(line_processed + '\n')
    
    return nomor_bagian, hasil_bagian

def proses_teks_paralel(nama_file, dari_bahasa, ke_bahasa, nama_output):
    """
    Memproses file teks dengan parallel processing
    """
    # Scan dan buat mapping terlebih dahulu
    if not scan_dan_buat_mapping(nama_file):
        return False
    
    # Bagi file menjadi beberapa bagian
    bagian_bagian = bagi_file(nama_file, MAX_WORKERS)
    if not bagian_bagian:
        return False
    
    hasil_threads = []
    
    print(f"{COLOR['hijau']}Memproses {len(bagian_bagian)} bagian secara paralel...{COLOR['reset']}")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_bagian = {
            executor.submit(terjemahkan_bagian, bagian, dari_bahasa, ke_bahasa): bagian[0]
            for bagian in bagian_bagian
        }
        
        for future in as_completed(future_to_bagian):
            try:
                nomor_bagian, hasil = future.result()
                hasil_threads.append((nomor_bagian, hasil))
                print(f"{COLOR['hijau']}Bagian {nomor_bagian + 1} selesai{COLOR['reset']}")
            except Exception as e:
                print(f"{COLOR['merah']}Error di bagian {future_to_bagian[future]}: {e}{COLOR['reset']}")
    
    # Urutkan hasil berdasarkan nomor bagian
    hasil_threads.sort(key=lambda x: x[0])
    
    # Gabungkan semua bagian
    hasil_akhir = []
    for nomor_bagian, bagian_hasil in hasil_threads:
        hasil_akhir.extend(bagian_hasil)
    
    # Simpan hasil
    with open(nama_output, 'w', encoding='utf-8') as f:
        f.writelines(hasil_akhir)
    
    print(f"\n{COLOR['hijau']}File hasil disimpan sebagai: {nama_output}{COLOR['reset']}")
    return True

def proses_json(nama_file, dari_bahasa, ke_bahasa, nama_output):
    # Scan dan buat mapping terlebih dahulu
    if not scan_dan_buat_mapping(nama_file):
        return False
    
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
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
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
                    time.sleep(DELAY_BETWEEN_REQUESTS)
                else:
                    hasil[k] = v
            
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
    return proses_teks_paralel(nama_file, dari_bahasa, ke_bahasa, nama_output)

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