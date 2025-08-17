# **Tran**  
Tools untuk manipulasi file `.rpy`, `.rpyc`, dan `.json` (konversi, split/merge, penerjemahan otomatis dengan proteksi tag/variabel).  

### 🔧 **Fitur**  
1. **Konversi `.rpy` → `.rpyc`**  
2. **Split/Merge file** berdasarkan line count.  
3. **Auto-translate `.rpy`** dengan proteksi `{tag}` dan `[variabel]`.  
4. **Restore tag/variabel** setelah translate.  
5. **Translate `.json`/file teks** dengan struktur tertentu.  

---

### 🚀 **Cara Penggunaan**  
#### 1. Konversi `.rpy` → `.rpyc`  
- Letakkan file `.rpy` di folder `to_rpyc`.  
- Jalankan **GitHub Actions** (`workflows/complete_rpy_to_rpyc`).  

#### 2. Split/Merge File  
- Jalankan `spliter.py`:  
  ```bash
  python spliter.py
  ```  
  **Catatan**:  
  - Untuk file `.json`, pastikan teks diawali `{` dan diakhiri `}`.  
  - Hapus koma (`,`) di akhir line sebelum merge.  

#### 3. Translate `.rpy`  
- Jalankan `translate_rpy.py`:  
  ```bash
  python translate_rpy.py
  ```  
  **Struktur Teks yang Didukung**:  
  ```text
  # Format dasar Ren'Py
  dialog "Teks yang akan diterjemahkan {tag} [variabel]."
  ```  
  - **Proteksi otomatis**:  
    - `{tag_apa_pun}` dan `[variabel_apa_pun]` tidak akan diterjemahkan.  

#### 4. Restore Tag/Variabel  
- Setelah translate, jalankan:  
  ```bash
  python restored.py
  ```  

#### 5. Translate `.json`/File Teks  
- Jalankan `all_translate.py`:  
  ```bash
  python all_translate.py
  ```  
  **Struktur Teks yang Didukung**:  
  ```json
  {
    "key": "Teks yang akan diterjemahkan",
    "nested": { "key": "Teks bersarang" }
  }
  ```  
  atau  
  ```text
  Teks standar per baris (1 baris = 1 terjemahan).
  ```  

---

### 📂 **Contoh Hasil**  dari tes_rpy.rpy & tes_json.json

1. Hasil `translate_rpy.py` → `tes_id.rpy`
2. Hasil `restored.py` → `tes_restored.rpy`  
3. Hasil `all_translate.py` → `tes_all.json`  

---

### ⚠️ **Peringatan**  
1. **Bebas digunakan**, tetapi penulis **tidak bertanggung jawab** untuk penyalahgunaan.  
2. Jika mengembangkan/memodifikasi, **wajib cantumkan nama penulis asli**.  
3. Dibuat untuk kepentingan pribadi, tetapi boleh dipakai selama **beretika**.  

---

### 📜 **Lisensi**  
- **Boleh**: Gunakan, modifikasi, distribusi.  
- **Wajib**: Credit ke [@usernamelas](https://github.com/usernamelas).  
- **Dilarang**: Klaim sebagai karya sendiri atau penggunaan ilegal.  

🔗 **Repositori**: [github.com/usernamelas/tran](https://github.com/usernamelas/tran)  

---  

### 💡 **Catatan Penting**  
- **File `.rpy`**:  
  - Hanya teks dalam `dialog "..."` atau `label:` yang akan diterjemahkan.  
- **File `.json`**:  
  - Hanya nilai (*value*) dari *key* yang diterjemahkan.  
- **Gunakan Python 3.10+** dan backup file sebelum proses!