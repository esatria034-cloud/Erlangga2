# Program untuk membuat file data_mahasiswa.txt
# dan menuliskan tiga nama mahasiswa ke dalam file

try:
    # Membuka file dalam mode tulis (akan membuat file jika belum ada)
    file = open("data_mahasiswa.txt", "w")

    print("File berhasil dibuka / dibuat.")

    # Data nama mahasiswa
    nama1 = "Andi"
    nama2 = "Budi"
    nama3 = "Citra"

    # Menulis data ke file satu per satu
    file.write(nama1 + "\n")
    file.write(nama2 + "\n")
    file.write(nama3 + "\n")

    print("Data mahasiswa berhasil ditulis ke dalam file.")

except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    # Menutup file
    file.close()
    print("File telah ditutup.")