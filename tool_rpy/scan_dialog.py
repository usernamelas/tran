#!/usr/bin/env python3
import os
import re
import sys

def cari_file_dengan_dialog(folder_path):
    """
    Mencari file .rpy yang mengandung dialog dengan pattern yang lebih spesifik
    """
    # Pattern untuk mendeteksi dialog Ren'Py yang lebih akurat
    patterns = [
        r'^\s*[a-zA-Z0-9_]+\s+"[^"]+"',  # character "dialog"
        r'^\s*"[^"]+"',                   # "dialog" (tanpa character)
        r'^\s*[a-zA-Z0-9_]+ "[^"]+"',     # character "dialog" (tanpa spasi setelah karakter)
        r'^\s*[a-zA-Z0-9_]+\s+"""[^"]*"""',  # Multi-line dialog
    ]
    
    file_dengan_dialog = []
    file_tanpa_dialog = []
    total_dialog_ditemukan = 0
    
    # Iterasi melalui semua file .rpy
    for filename in os.listdir(folder_path):
        if filename.endswith('.rpy'):
            filepath = os.path.join(folder_path, filename)
            dialog_di_file = 0
            
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    for line_num, line in enumerate(file, 1):
                        # Skip komentar
                        if line.strip().startswith('#'):
                            continue
                            
                        # Cek semua pattern dialog
                        for pattern in patterns:
                            if re.search(pattern, line):
                                dialog_di_file += 1
                                total_dialog_ditemukan += 1
                                break  # Hanya hitung sekali per line
                    
                # Tentukan apakah file mengandung dialog
                if dialog_di_file > 0:
                    file_dengan_dialog.append((filename, dialog_di_file))
                else:
                    file_tanpa_dialog.append(filename)
                        
            except UnicodeDecodeError:
                # Coba dengan encoding lain jika UTF-8 gagal
                try:
                    with open(filepath, 'r', encoding='latin-1') as file:
                        for line in file:
                            for pattern in patterns:
                                if re.search(pattern, line):
                                    dialog_di_file += 1
                                    total_dialog_ditemukan += 1
                                    break
                    
                    if dialog_di_file > 0:
                        file_dengan_dialog.append((filename, dialog_di_file))
                    else:
                        file_tanpa_dialog.append(filename)
                        
                except Exception as e:
                    print(f"Error membaca file {filename}: {e}")
                    
            except Exception as e:
                print(f"Error membaca file {filename}: {e}")
    
    return file_dengan_dialog, file_tanpa_dialog, total_dialog_ditemukan

def main():
    if len(sys.argv) != 2:
        print("Usage: python seleksi_dialog.py <folder_path>")
        print("Contoh: python seleksi_dialog.py .")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' tidak ditemukan!")
        sys.exit(1)
    
    print("🔍 Mencari file dengan dialog Ren'Py...")
    print("=" * 60)
    
    file_dengan_dialog, file_tanpa_dialog, total_dialog = cari_file_dengan_dialog(folder_path)
    
    # Urutkan file dengan dialog berdasarkan jumlah dialog (descending)
    file_dengan_dialog.sort(key=lambda x: x[1], reverse=True)
    
    # Tampilkan hasil
    print(f"📁 File dengan DIALOG ditemukan: {len(file_dengan_dialog)} file")
    print(f"📊 Total dialog terdeteksi: {total_dialog}")
    print("=" * 40)
    for file, count in file_dengan_dialog:
        print(f"✅ {file} ({count} dialog)")
    
    print(f"\n📁 File TANPA dialog: {len(file_tanpa_dialog)} file")
    print("=" * 40)
    for file in file_tanpa_dialog:
        print(f"❌ {file}")
    
    # Simpan ke file log
    with open('hasil_seleksi_dialog.txt', 'w', encoding='utf-8') as f:
        f.write("ANALISIS FILE RPY - DETEKSI DIALOG\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("FILE DENGAN DIALOG:\n")
        f.write("=" * 30 + "\n")
        for file, count in file_dengan_dialog:
            f.write(f"{file} ({count} dialog)\n")
        
        f.write(f"\nFILE TANPA DIALOG ({len(file_tanpa_dialog)} file):\n")
        f.write("=" * 30 + "\n")
        for file in file_tanpa_dialog:
            f.write(f"{file}\n")
        
        f.write(f"\n📊 TOTAL: {len(file_dengan_dialog)} file dengan dialog\n")
        f.write(f"📊 TOTAL: {len(file_tanpa_dialog)} file tanpa dialog\n")
        f.write(f"🎯 TOTAL DIALOG: {total_dialog}\n")
    
    print(f"\n📝 Hasil detail disimpan di: hasil_seleksi_dialog.txt")

if __name__ == "__main__":
    main()