#!/usr/bin/env python3
import os
import re
import sys

def hitung_dialog_file(filepath):
    """Hitung jumlah dialog dalam satu file"""
    patterns = [
        r'^\s*[a-zA-Z0-9_]+\s+"[^"]+"',
        r'^\s*"[^"]+"',
        r'^\s*[a-zA-Z0-9_]+ "[^"]+"',
        r'^\s*[a-zA-Z0-9_]+\s+"""[^"]*"""',
    ]
    
    count = 0
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip().startswith('#'):
                    continue
                for pattern in patterns:
                    if re.search(pattern, line):
                        count += 1
                        break
    except:
        try:
            with open(filepath, 'r', encoding='latin-1') as file:
                for line in file:
                    if line.strip().startswith('#'):
                        continue
                    for pattern in patterns:
                        if re.search(pattern, line):
                            count += 1
                            break
        except Exception as e:
            print(f"Error membaca {filepath}: {e}")
            return 0
    
    return count

def gabungkan_file():
    """Menu 1: Gabungkan file berdasarkan jumlah dialog"""
    print("\n" + "="*50)
    print("GABUNGKAN FILE RPY")
    print("="*50)
    
    # Input maximal dialog
    try:
        max_dialog = int(input("Masukkan maximal dialog per file: "))
    except ValueError:
        print("Input harus angka!")
        return
    
    # Input nama output file
    output_file = input("Nama file output gabungan (tanpa .rpy): ").strip()
    if not output_file:
        output_file = "gabungan"
    
    output_rpy = f"{output_file}.rpy"
    output_log = f"{output_file}_log.txt"
    
    # Cari semua file .rpy
    files = [f for f in os.listdir('.') if f.endswith('.rpy') and f != output_rpy]
    
    if not files:
        print("Tidak ada file .rpy ditemukan!")
        return
    
    file_yang_digabung = []
    file_yang_diabaikan = []
    total_file_digabung = 0
    total_dialog_digabung = 0
    
    print(f"\nMemproses {len(files)} file...")
    
    with open(output_rpy, 'w', encoding='utf-8') as out_rpy, \
         open(output_log, 'w', encoding='utf-8') as out_log:
        
        out_log.write("FILE YANG DIGABUNGKAN:\n")
        out_log.write("="*40 + "\n")
        
        for filename in files:
            dialog_count = hitung_dialog_file(filename)
            
            if dialog_count <= max_dialog:
                # Gabungkan file dengan format yang dilindungi
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                except:
                    try:
                        with open(filename, 'r', encoding='latin-1') as f:
                            content = f.read()
                    except Exception as e:
                        print(f"Error membaca {filename}: {e}")
                        continue
                
                # FORMAT YANG DILINDUNGI DARI TRANSLATE
                out_rpy.write(f"\n\n{'='*60}\n")
                out_rpy.write(f"# ===== FILE: {filename} =====\n")
                out_rpy.write(f"{'='*60}\n\n")
                out_rpy.write(content)
                out_rpy.write(f"\n\n{'='*60}\n")
                out_rpy.write(f"# ===== END OF: {filename} =====\n")
                out_rpy.write(f"{'='*60}\n")
                
                out_log.write(f"{filename} ({dialog_count} dialog)\n")
                
                file_yang_digabung.append((filename, dialog_count))
                total_file_digabung += 1
                total_dialog_digabung += dialog_count
                
                print(f"✅ {filename} ({dialog_count} dialog) - DIGABUNG")
            else:
                file_yang_diabaikan.append((filename, dialog_count))
                print(f"❌ {filename} ({dialog_count} dialog) - DIABAIKAN")
        
        # Tulis summary di log
        out_log.write(f"\n{'='*40}\n")
        out_log.write("SUMMARY:\n")
        out_log.write(f"Total file digabung: {total_file_digabung}\n")
        out_log.write(f"Total dialog digabung: {total_dialog_digabung}\n")
        out_log.write(f"Maximal dialog: {max_dialog}\n")
        out_log.write(f"File output: {output_rpy}\n")
        
        # Tulis file yang diabaikan
        out_log.write(f"\n{'='*40}\n")
        out_log.write("FILE YANG DIABAIKAN (terlalu banyak dialog):\n")
        out_log.write("="*40 + "\n")
        for filename, count in file_yang_diabaikan:
            out_log.write(f"{filename} ({count} dialog)\n")
        
        out_log.write(f"\nTotal file diabaikan: {len(file_yang_diabaikan)}\n")
    
    print(f"\n✅ Selesai!")
    print(f"📁 File gabungan: {output_rpy}")
    print(f"📋 Log file: {output_log}")
    print(f"📊 Total file digabung: {total_file_digabung}")
    print(f"📊 Total file diabaikan: {len(file_yang_diabaikan)}")
    print(f"🎯 Total dialog: {total_dialog_digabung}")

def pisahkan_file():
    """Menu 2: Pisahkan file gabungan"""
    print("\n" + "="*50)
    print("PISAHKAN FILE GABUNGAN")
    print("="*50)
    
    # Cari file gabungan
    files = [f for f in os.listdir('.') if f.endswith('.rpy') and '_log.txt' not in f]
    
    if not files:
        print("Tidak ada file .rpy ditemukan!")
        return
    
    print("File yang ditemukan:")
    for i, filename in enumerate(files, 1):
        print(f"{i}. {filename}")
    
    try:
        pilihan = int(input("\nPilih file yang akan dipisah (nomor): "))
        if pilihan < 1 or pilihan > len(files):
            print("Pilihan tidak valid!")
            return
        
        file_gabungan = files[pilihan-1]
        
    except ValueError:
        print("Input harus angka!")
        return
    
    print(f"\nMemproses {file_gabungan}...")
    
    try:
        with open(file_gabungan, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        try:
            with open(file_gabungan, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f"Error membaca file: {e}")
            return
    
    # Pattern untuk menemukan setiap file (format yang dilindungi)
    pattern = r'={60}\s+# ===== FILE: (.*?) =====\s+={60}(.*?)={60}\s+# ===== END OF: \1 =====\s+={60}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    if not matches:
        print("Tidak ditemukan format file gabungan yang valid!")
        print("Mencoba pattern alternatif...")
        # Coba pattern alternatif
        pattern_alt = r'={60}\s+===== FILE: (.*?) =====\s+={60}(.*?)={60}\s+===== END OF: \1 =====\s+={60}'
        matches = re.findall(pattern_alt, content, re.DOTALL)
        if not matches:
            print("Format tidak dikenali! Pastikan file adalah hasil gabungan.")
            return
    
    # Buat folder untuk hasil pisah
    folder_pisah = f"hasil_pisah_{file_gabungan.replace('.rpy', '')}"
    os.makedirs(folder_pisah, exist_ok=True)
    
    total_dipisahkan = 0
    
    for filename, file_content in matches:
        filepath = os.path.join(folder_pisah, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content.strip())
        
        print(f"✅ {filename} berhasil dipisahkan")
        total_dipisahkan += 1
    
    print(f"\n🎉 Selesai! {total_dipisahkan} file berhasil dipisahkan")
    print(f"📁 File hasil disimpan di folder: {folder_pisah}")

def main():
    """Menu utama"""
    while True:
        print("\n" + "="*50)
        print("FILE MANAGER FOR REN'PY FILES")
        print("="*50)
        print("1. Gabungkan file")
        print("2. Pisahkan file") 
        print("3. Exit")
        print("="*50)
        
        pilihan = input("Pilih menu (1-3): ").strip()
        
        if pilihan == "1":
            gabungkan_file()
        elif pilihan == "2":
            pisahkan_file()
        elif pilihan == "3":
            print("Terima kasih! 👋")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-3")

if __name__ == "__main__":
    main()