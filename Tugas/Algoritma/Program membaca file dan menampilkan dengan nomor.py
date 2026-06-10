# Program untuk membaca isi file data_mahasiswa.txt
# dan menampilkan dengan nomor urut

try:
    # Membuka file dalam mode baca
    file = open("data_mahasiswa.txt", "r")

    print("Isi data mahasiswa:\n")

    # Membaca semua isi file
    baris_data = file.readlines()

    # Inisialisasi nomor
    nomor = 1

    # Perulangan untuk menampilkan isi file
    for data in baris_data:
        data_bersih = data.strip()  # Menghapus spasi dan newline
        print("Nomor", nomor, ":", data_bersih)
        nomor = nomor + 1

except FileNotFoundError:
    print("File tidak ditemukan, pastikan file sudah dibuat.")

except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    try:
        file.close()
        print("\nFile berhasil ditutup.")
    except:
        pass