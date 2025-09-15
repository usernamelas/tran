import os
import re

def fix_translation_files(folder_path):
    """
    Mengubah semua translate english/indonesian menjadi translate id
    di semua file .rpy dalam folder
    """
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} tidak ditemukan!")
        return
    
    # Pattern untuk mencari translate english atau translate indonesian
    pattern = r'translate\s+(english|indonesian)\s+'
    replacement = r'translate id '
    
    files_processed = 0
    changes_made = 0
    
    # Loop semua file .rpy di folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.rpy'):
            filepath = os.path.join(folder_path, filename)
            
            try:
                # Baca file
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Hitung berapa kali akan diubah
                matches = re.findall(pattern, content)
                file_changes = len(matches)
                
                if file_changes > 0:
                    # Ubah translate english/indonesian menjadi translate id
                    new_content = re.sub(pattern, replacement, content)
                    
                    # Tulis kembali file
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    
                    print(f"✅ {filename}: {file_changes} perubahan")
                    files_processed += 1
                    changes_made += file_changes
                else:
                    print(f"⏭️  {filename}: tidak ada yang perlu diubah")
                    
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
    
    print(f"\n🎉 Selesai!")
    print(f"📁 File yang diproses: {files_processed}")
    print(f"🔄 Total perubahan: {changes_made}")

# CARA PAKAI:
if __name__ == "__main__":
    # Ganti path ini dengan folder tl/id/ Anda
    folder_path = input("Masukkan path folder tl/id/: ").strip()
    
    # Atau langsung set path:
    # folder_path = "C:/path/to/game/tl/id/"
    
    fix_translation_files(folder_path)