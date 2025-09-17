def ganti_translate(filename):
    # Hitung berapa kali teks "translate english" muncul
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("translate english"):
                count += 1

    print(f"Total 'translate english' ditemukan: {count}")

    # Buat nama file baru tambah "_edit" sebelum ekstensi
    if '.' in filename:
        base, ext = filename.rsplit('.', 1)
        new_filename = f"{base}_edit.{ext}"
    else:
        new_filename = f"{filename}_edit"

    # Tulis ulang isi file ke file baru dengan ganti teks
    with open(new_filename, 'w', encoding='utf-8') as newfile:
        for line in lines:
            if line.startswith("translate english"):
                # Ganti 'translate english' dengan 'translate id' tapi sisanya tetap
                line = line.replace("translate english", "translate id", 1)
            newfile.write(line)

    print(f"File baru tersimpan dengan nama: {new_filename}")

# Contoh pakai:
ganti_translate('GABUNGAN.rpy')