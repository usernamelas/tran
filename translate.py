#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PENERJEMAH REN'PY OTOMATIS - VERSION IMPROVED
Fitur:
- Mempertahankan urutan kalimat asli
- Proteksi variabel [nama] dan tag {color} yang lebih baik
- Memisahkan dan menyatukan kalimat dengan benar
"""

import re
import os
import sys
import json
import time
import signal
import shutil
import subprocess
from datetime import datetime
from typing import Tuple, Dict, List, Optional

# ================= CONFIGURASI =================
INPUT_FILE = "x-script_nts.rpy"            # File input
OUTPUT_FILE = "x-script_nts_id.rpy"        # File output
LOG_TXT = "tl_log.txt"                     # Log readable
LOG_JSON = "tl_log.json"                   # Log terstruktur
BAHASA_ASAL = "en"                         # Bahasa sumber
BAHASA_TUJUAN = "id"                       # Bahasa target
JEDA_TERJEMAH = 0.5                        # Delay antar terjemahan (detik)
MAX_RETRY = 3                              # Percobaan ulang jika gagal
# ==============================================

class RenPyTranslator:
    def __init__(self):
        self.should_exit = False
        signal.signal(signal.SIGINT, self._handle_interrupt)
        
        # Verifikasi translate-shell terinstall
        if not self._check_dependencies():
            print("❌ Error: 'trans' (translate-shell) tidak ditemukan!")
            print("Instal dengan: brew install translate-shell")
            sys.exit(1)
            
        # Inisialisasi log
        self.log_data = {
            "start_time": datetime.now().isoformat(),
            "file_input": INPUT_FILE,
            "file_output": OUTPUT_FILE,
            "total_lines": 0,
            "translated": 0,
            "skipped": [],
            "errors": [],
            "end_time": None,
            "success": False
        }
        
        # Bersihkan log sebelumnya
        open(LOG_TXT, 'w').close()
        open(LOG_JSON, 'w').close()

    def _check_dependencies(self) -> bool:
        """Cek apakah translate-shell terinstall"""
        return shutil.which("trans") is not None

    def _handle_interrupt(self, signum, frame):
        """Tangani Ctrl+C untuk exit graceful"""
        print("\n🛑 Mempersiapkan penghentian... (Simpan progres...)")
        self.should_exit = True

    def _write_log(self, text: str, reason: str, line_num: int, is_skipped: bool = True) -> None:
        """Catat ke log file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        truncated_text = text[:200] + "..." if len(text) > 200 else text
        log_entry = {
            "time": timestamp,
            "text": truncated_text,
            "reason": reason,
            "line": line_num
        }
        
        # Log teks
        with open(LOG_TXT, 'a', encoding='utf-8') as f:
            status = "[SKIP]" if is_skipped else "[TRANSLATE]"
            f.write(f"[{timestamp}] {status} {reason} (Baris {line_num}): {truncated_text}\n")
        
        # Log JSON
        if is_skipped:
            self.log_data["skipped"].append(log_entry)
        elif "Error" in reason:
            self.log_data["errors"].append(log_entry)

    def _should_skip(self, text: str) -> bool:
        """Tentukan apakah teks harus dilewati"""
        text = text.strip()
        return (
            len(text) < 2 or
            text.startswith(('http://', 'https://')) or
            text.isdigit() or
            any(ext in text.lower() for ext in ['.png','.jpg','.webm','.mp3','.ogg','.wav'])
        )

    def _protect_special_content(self, text: str) -> Tuple[str, Dict[str, str]]:
        """
        Lindungi konten khusus dengan placeholder unik
        """
        protected_items = {}
        protected = text
        
        # Proteksi variabel [nama]
        for i, match in enumerate(re.finditer(r'(\[[^\]]+\])', text)):
            placeholder = f"__RENPY_VAR_{i}__"
            protected_items[placeholder] = match.group(1)
            protected = protected.replace(match.group(1), placeholder)
        
        # Proteksi tag {color=#fff}
        for i, match in enumerate(re.finditer(r'(\{[^\}]+\})', protected)):
            placeholder = f"__RENPY_TAG_{i}__"
            protected_items[placeholder] = match.group(1)
            protected = protected.replace(match.group(1), placeholder)
        
        # Proteksi escape character
        for i, match in enumerate(re.finditer(r'(\\.)', protected)):
            placeholder = f"__RENPY_ESC_{i}__"
            protected_items[placeholder] = match.group(1)
            protected = protected.replace(match.group(1), placeholder)
            
        return protected, protected_items

    def _restore_special_content(self, text: str, items: Dict[str, str]) -> str:
        """Kembalikan konten yang diproteksi"""
        restored = text
        for placeholder, original in items.items():
            restored = restored.replace(placeholder, original)
        return restored

    def _split_sentences(self, text: str) -> List[str]:
        """Pisahkan teks menjadi kalimat-kalimat"""
        # Gunakan regex untuk memisahkan kalimat namun tetap mempertahankan tanda baca
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]

    def _translate_sentence(self, sentence: str, retry_count: int = 0) -> Optional[str]:
        """Terjemahkan satu kalimat dengan proteksi"""
        if retry_count >= MAX_RETRY:
            self._write_log(sentence, f"Error: Maksimum percobaan terjemahan ({MAX_RETRY}x)", 0)
            return None
            
        try:
            # Proteksi konten khusus
            protected_text, protected_items = self._protect_special_content(sentence)
            
            # Proses terjemahan
            cmd = [
                'trans',
                '-b',
                f'{BAHASA_ASAL}:{BAHASA_TUJUAN}',
                f'"{protected_text}"'
            ]
            
            result = subprocess.run(
                ' '.join(cmd),
                shell=True,
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip() or "Unknown error"
                self._write_log(sentence, f"Translate Error: {error_msg}", 0)
                time.sleep(2)
                return self._translate_sentence(sentence, retry_count + 1)
                
            translated = result.stdout.strip()
            
            # Kembalikan konten yang diproteksi
            translated = self._restore_special_content(translated, protected_items)
            
            return translated
        except subprocess.TimeoutExpired:
            self._write_log(sentence, "Error: Timeout saat menerjemahkan", 0)
            time.sleep(3)
            return self._translate_sentence(sentence, retry_count + 1)
        except Exception as e:
            self._write_log(sentence, f"Error: {str(e)}", 0)
            return None

    def _translate_text(self, text: str) -> str:
        """Terjemahkan teks dengan mempertahankan urutan kalimat"""
        sentences = self._split_sentences(text)
        translated_sentences = []
        
        for sentence in sentences:
            if self._should_skip(sentence):
                translated_sentences.append(sentence)
                continue
                
            translated = self._translate_sentence(sentence)
            if translated:
                translated_sentences.append(translated)
                self.log_data["translated"] += 1
                self._write_log(sentence, f"Terjemahan sukses -> {translated[:50]}...", 0, False)
            else:
                translated_sentences.append(sentence)  # Jika gagal, gunakan teks asli
        
        # Gabungkan kembali dengan spasi
        return ' '.join(translated_sentences)

    def _process_line(self, line: str) -> str:
        """Proses satu baris untuk diterjemahkan"""
        # Pola untuk menangkap dialog dalam berbagai format Ren'Py
        pattern = r'(?P<prefix>[\w\s]*)(?P<quote>")(?P<content>[^"]+)(?P<endquote>")'
        
        def translate_match(match):
            prefix = match.group('prefix')
            content = match.group('content')
            quote = match.group('quote')
            endquote = match.group('endquote')
            
            if self._should_skip(content):
                self._write_log(content, "Teks sistem/dilewati", 0)
                return match.group(0)
                
            translated = self._translate_text(content)
            if translated and translated != content:
                return f'{prefix}{quote}{translated}{endquote}'
            return match.group(0)
        
        return re.sub(pattern, translate_match, line)

    def process_file(self) -> bool:
        """Proses utama penerjemahan"""
        print(f"🔍 Memulai penerjemahan: {INPUT_FILE}")
        print(f"ℹ️ Target bahasa: {BAHASA_ASAL} → {BAHASA_TUJUAN}")
        print("ℹ️ Tekan Ctrl+C untuk berhenti kapan saja\n")
        
        # Verifikasi file input
        if not os.path.exists(INPUT_FILE):
            print(f"❌ File input tidak ditemukan: {INPUT_FILE}")
            return False
            
        try:
            with open(INPUT_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"❌ Gagal membaca file: {e}")
            return False

        self.log_data["total_lines"] = len(lines)
        translated_lines = []
        start_time = time.time()
        
        try:
            for line_num, line in enumerate(lines, 1):
                if self.should_exit:
                    raise KeyboardInterrupt
                    
                # Skip baris kosong atau komentar
                if line.strip().startswith('#') or not line.strip():
                    translated_lines.append(line)
                    continue
                    
                # Proses baris
                processed_line = self._process_line(line)
                translated_lines.append(processed_line)
                
                # Update progress
                if line_num % 5 == 0 or line_num == len(lines):
                    elapsed = time.time() - start_time
                    percent = (line_num / len(lines)) * 100
                    remaining = (len(lines) - line_num) * JEDA_TERJEMAH
                    print(
                        f"\r🔄 Progress: {percent:.1f}% | "
                        f"Baris: {line_num}/{len(lines)} | "
                        f"Diterjemahkan: {self.log_data['translated']} | "
                        f"Sisa: ~{remaining:.0f} detik",
                        end=''
                    )
                
                time.sleep(JEDA_TERJEMAH)
                
        except KeyboardInterrupt:
            print("\n⚠️ Proses dihentikan manual oleh user")
        
        # Simpan hasil
        try:
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.writelines(translated_lines)
                
            self.log_data["end_time"] = datetime.now().isoformat()
            self.log_data["success"] = not self.should_exit
            
            with open(LOG_JSON, 'w', encoding='utf-8') as f:
                json.dump(self.log_data, f, indent=2, ensure_ascii=False)
                
            print(f"\n\n✅ Hasil tersimpan di: {OUTPUT_FILE}")
            print(f"📝 Log teks: {LOG_TXT}")
            print(f"📊 Log JSON: {LOG_JSON}")
            
            # Ringkasan
            print("\n=== RINGKASAN ===")
            print(f"Total baris: {self.log_data['total_lines']}")
            print(f"Teks diterjemahkan: {self.log_data['translated']}")
            print(f"Teks dilewati: {len(self.log_data['skipped'])}")
            print(f"Error: {len(self.log_data['errors'])}")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Gagal menyimpan hasil: {e}")
            return False

if __name__ == "__main__":
    print("\n=== PENERJEMAH REN'PY OTOMATIS ===")
    translator = RenPyTranslator()
    success = translator.process_file()
    
    if success:
        print("\n🎉 Penerjemahan selesai!")
    else:
        print("\n🔴 Penerjemahan gagal atau terhenti")
    print("====================================\n")