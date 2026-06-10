# Program untuk membuat folder arsip
# dan memindahkan file data_mahasiswa.txt ke dalamnya

import os
import shutil

try:
    nama_folder = "arsip"

    # Mengecek apakah folder sudah ada
    if not os.path.exists(nama_folder):
        os.mkdir(nama_folder)
        print("Folder arsip berhasil dibuat.")
    else:
        print("Folder arsip sudah ada.")

    # Nama file yang akan dipindahkan
    nama_file = "data_mahasiswa.txt"

    # Mengecek apakah file ada
    if os.path.exists(nama_file):
        tujuan = os.path.join(nama_folder, nama_file)

        # Memindahkan file
        shutil.move(nama_file, tujuan)

        print("File berhasil dipindahkan ke folder arsip.")
    else:
        print("File data_mahasiswa.txt tidak ditemukan.")

except Exception as e:
    print("Terjadi kesalahan:", e)