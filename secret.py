#!/usr/bin/env python3
import base64
import os
import sys
import time

SUPPORTED_LANGUAGES = {
    "py": "Python",
    "sh": "Bash",
    "html": "HTML",
    "js": "JavaScript",
    "php": "PHP",
}

def is_valid_encoding(content):
    """Periksa apakah file dapat di-encode dengan UTF-8."""
    try:
        content.encode("utf-8")  # Pastikan dapat di-encode UTF-8
        return True
    except UnicodeEncodeError:
        return False

def obfuscate_python(content):
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    obfuscated_code = f"""# Obfuscated by Wanz Xploit
import base64
exec(base64.b64decode('{encoded_content}').decode('utf-8'))
"""
    return obfuscated_code

def obfuscate_bash(content):
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    obfuscated_code = f"""#!/bin/bash
# Obfuscated by Wanz Xploit
bash <(echo '{encoded_content}' | base64 -d)
"""
    return obfuscated_code

def obfuscate_html(content):
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    obfuscated_script = f"""<script>
<!-- Obfuscated by Wanz Xploit -->
document.write(atob("{encoded_content}"));
</script>"""
    return obfuscated_script

def obfuscate_javascript(content):
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    return f"""// Obfuscated by Wanz Xploit
eval(atob("{encoded_content}"));
"""

def obfuscate_php(content):
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    return f"""<?php
/* Obfuscated by Wanz Xploit */

// Decode base64 dan simpan ke file sementara
$decoded = base64_decode("{encoded_content}");
$temp_file = tempnam(sys_get_temp_dir(), 'obf_');
file_put_contents($temp_file, $decoded);

// Menjalankan file PHP sementara
include($temp_file);
unlink($temp_file); // Hapus file sementara setelah dieksekusi
?>
"""

def obfuscate_content(content, language):
    if language == "Python":
        return obfuscate_python(content)
    elif language == "Bash":
        return obfuscate_bash(content)
    elif language == "HTML":
        return obfuscate_html(content)
    elif language == "JavaScript":
        return obfuscate_javascript(content)
    elif language == "PHP":
        return obfuscate_php(content)
    else:
        raise ValueError(f"Unsupported language: {language}")

def obfuscate_file(file_path):
    ext = file_path.split(".")[-1]
    if ext not in SUPPORTED_LANGUAGES:
        print(f"Error: File extension '.{ext}' not supported!")
        sys.exit(1)

    language = SUPPORTED_LANGUAGES[ext]
    try:
        with open(file_path, "r", encoding="utf-8") as f:  # Baca file dengan encoding UTF-8
            content = f.read()

        # Pemeriksaan apakah file bisa di-encode dengan UTF-8
        if not is_valid_encoding(content):
            raise ValueError("File contains non-UTF-8 characters or unsupported encoding.")

        obfuscated_content = obfuscate_content(content, language)
        output_file = f"{os.path.splitext(file_path)[0]}_secret.{ext}"
        with open(output_file, "w", encoding="utf-8") as f:  # Tulis file dengan encoding UTF-8
            f.write(obfuscated_content)

        # Tampilkan hasil sukses dengan warna hijau
        print(f"\033[92m{' '*1}╔════════════════════════════════════════╗")
        print(f"{'   '*1}Status: Success")
        print(f"{'   '*1}Original File: {file_path}")
        print(f"{'   '*1}Obfuscated File: {output_file}")
        print(f"{' '*1}╚════════════════════════════════════════╝\033[0m")
    except Exception as e:
        # Tampilkan hasil gagal dengan warna merah
        print(f"\033[91m{' '*1}╔════════════════════════════════════════╗")
        print(f"{'   '*1}Status: Failed By Wanz Xploit")
        print(f"{'   '*1}Original File: {file_path}")
        print(f"{'   '*1}Obfuscated File: Unknown")
        print(f"{'   '*1}English: {str(e)}")
        print(f"{'   '*1}Suggestion: Check if the file contains valid UTF-8 characters.")
        print(f"{'   '*1}Indonesia: File mengandung karakter non-UTF-8 atau encoding tidak didukung.")
        print(f"{'   '*1}Saran: Pastikan file menggunakan encoding UTF-8 yang valid.")
        print(f"{' '*1}╚════════════════════════════════════════╝\033[0m")

        time.sleep(1)  # Delay 1 detik untuk menghindari spam

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 secret.py <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found!")
        sys.exit(1)

    obfuscate_file(input_file)
