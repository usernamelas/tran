#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RESTORASI VARIABEL REN'PY
Fitur:
- Mengubah placeholder __renpy_var_X__ kembali ke variabel asli [variabel]
- Support multiple variabel dalam satu file
- Backup file original sebelum modifikasi
"""

import re
import os
import shutil
from datetime import datetime

# ================= CONFIGURASI =================
INPUT_FILE = "x-script_nts_id.rpy"    # File yang akan diproses
BACKUP_EXT = ".backup"                # Ekstensi file backup
VARIABLE_MAP = {
    "__renpy_var_0__": "[fname]",
    "__renpy_var_1__": "[name]",
    # Tambahkan mapping lainnya di sini
}
# ==============================================

class VariableRestorer:
    def __init__(self):
        self.backup_path = f"{INPUT_FILE}{BACKUP_EXT}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
    def create_backup(self):
        """Buat backup file sebelum modifikasi"""
        try:
            shutil.copy2(INPUT_FILE, self.backup_path)
            print(f"✅ Backup created: {self.backup_path}")
            return True
        except Exception as e:
            print(f"❌ Gagal membuat backup: {e}")
            return False

    def restore_variables(self):
        """Proses utama restorasi variabel"""
        if not os.path.exists(INPUT_FILE):
            print(f"❌ File tidak ditemukan: {INPUT_FILE}")
            return False

        if not self.create_backup():
            return False

        try:
            with open(INPUT_FILE, 'r', encoding='utf-8') as f:
                content = f.read()

            # Restorasi menggunakan mapping yang telah ditentukan
            restored_content = content
            for placeholder, variable in VARIABLE_MAP.items():
                restored_content = restored_content.replace(placeholder, variable)

            # Restorasi otomatis untuk pola __renpy_var_X__ tanpa mapping
            def replace_unmapped(match):
                var_num = match.group(1)
                return f"[unknown_var_{var_num}]"  # Atau bisa diubah ke variabel default

            restored_content = re.sub(
                r'__renpy_var_(\d+)__', 
                replace_unmapped, 
                restored_content
            )

            # Simpan hasil
            with open(INPUT_FILE, 'w', encoding='utf-8') as f:
                f.write(restored_content)

            print("✅ Variabel berhasil direstorasi!")
            print(f"🔁 Variabel yang diubah: {len(VARIABLE_MAP)}")
            return True

        except Exception as e:
            print(f"❌ Error saat memproses file: {e}")
            return False

if __name__ == "__main__":
    print("\n=== RESTORASI VARIABEL REN'PY ===")
    restorer = VariableRestorer()
    
    # Otomatis deteksi variabel yang perlu di-restore
    if not VARIABLE_MAP:
        print("⚠️ VARIABLE_MAP kosong, tambahkan mapping variabel di config")
    
    success = restorer.restore_variables()
    
    if success:
        print("\n🎉 Proses selesai! File telah diperbarui.")
    else:
        print("\n🔴 Proses gagal, file original tidak diubah.")
    print("==================================\n")