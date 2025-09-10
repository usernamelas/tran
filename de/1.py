#!/data/data/com.termux/files/usr/bin/env python3

import os
import sys
import subprocess
import glob

# Path ke skrip unrpyc.py di folder unrpyc
UNRPYC_PATH = os.path.expanduser("~/unrpyc/unrpyc.py")

# Direktori tempat bridge.py berada (dan file-file .rpyc)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def decompile_all_rpyc():
    # Periksa apakah unrpyc.py ada
    if not os.path.exists(UNRPYC_PATH):
        print(f"ERROR: File {UNRPYC_PATH} tidak ditemukan!")
        return False
    
    # Cari semua file .rpyc di direktori saat ini
    rpyc_files = glob.glob(os.path.join(CURRENT_DIR, "*.rpyc"))
    
    if not rpyc_files:
        print("Tidak ada file .rpyc yang ditemukan di direktori ini.")
        return True
    
    print(f"Menemukan {len(rpyc_files)} file .rpyc untuk didekompilasi.")
    
    # Dekompilasi setiap file
    success_count = 0
    for rpyc_file in rpyc_files:
        print(f"Memproses: {os.path.basename(rpyc_file)}")
        
        try:
            # Jalankan unrpyc.py untuk file ini
            result = subprocess.run([
                sys.executable,  # Python interpreter yang sedang digunakan
                UNRPYC_PATH,
                rpyc_file
            ], capture_output=True, text=True, cwd=CURRENT_DIR)
            
            if result.returncode == 0:
                print(f"✓ Berhasil: {os.path.basename(rpyc_file)}")
                success_count += 1
            else:
                print(f"✗ Gagal: {os.path.basename(rpyc_file)}")
                print(f"  Error: {result.stderr}")
                
        except Exception as e:
            print(f"✗ Exception saat memproses {os.path.basename(rpyc_file)}: {str(e)}")
    
    print(f"\nSelesai. Berhasil mendekompilasi {success_count} dari {len(rpyc_files)} file.")
    return success_count == len(rpyc_files)

if __name__ == "__main__":
    print("=== Bridge Dekompilasi unrpyc ===")
    print(f"Direktori kerja: {CURRENT_DIR}")
    print(f"Path unrpyc: {UNRPYC_PATH}")
    print()
    
    decompile_all_rpyc()