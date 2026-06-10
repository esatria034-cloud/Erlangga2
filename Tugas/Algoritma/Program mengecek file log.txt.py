# Program untuk mengecek apakah file log.txt ada
# jika ada tampilkan isi, jika tidak buat file baru

import os

try:
    # Mengecek keberadaan file
    if os.path.exists("log.txt"):
        print("File log.txt ditemukan.\n")

        # Membuka dan membaca isi file
        file = open("log.txt", "r")
        isi_file = file.read()

        print("Isi file log:")
        print(isi_file)

        file.close()

    else:
        print("File log.txt tidak ditemukan.")
        print("Membuat file baru...")

        # Membuat file baru dan menulis isi awal
        file = open("log.txt", "w")
        file.write("Log dimulai")
        file.close()

        print("File log.txt berhasil dibuat.")

except Exception as e:
    print("Terjadi kesalahan:", e)