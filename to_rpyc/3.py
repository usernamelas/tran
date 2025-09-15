import os
import re

def fix_dash_in_old_new(filename):
    base, ext = os.path.splitext(filename)
    new_filename = f"{base}_edit{ext}"

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Deteksi old "..." baris
        m_old = re.match(r'^\s*old\s*"([–-])(.*)"\s*$', line)
        if m_old and (i+1) < len(lines):
            # Cek baris berikutnya apakah new
            next_line = lines[i+1]
            m_new = re.match(r'^\s*new\s*"([–-])(.*)"\s*$', next_line)
            if m_new:
                old_dash = m_old.group(1)
                new_dash = m_new.group(1)
                new_rest = m_new.group(2)
                # Jika dash berbeda, ubah dash di new agar sama dengan old
                if old_dash != new_dash:
                    fixed_new_line = re.sub(r'^(\s*new\s*")([–-])', r'\1' + old_dash, next_line)
                    output_lines.append(line)
                    output_lines.append(fixed_new_line)
                else:
                    output_lines.append(line)
                    output_lines.append(next_line)
                i += 2
                continue
        # Jika bukan pasangan old/new, copy apa adanya
        output_lines.append(line)
        i += 1

    with open(new_filename, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    print(f"Selesai! File hasil: {new_filename}")

# Contoh penggunaan:
fix_dash_in_old_new('x-prologue.rpy')