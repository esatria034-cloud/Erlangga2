def hitung_jumlah_baris(nama_file):
    try:
        with open(nama_file, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return "File tidak ditemukan"


def tulis_daftar_nama(nama_file, daftar_nama):
    with open(nama_file, "w") as file:
        file.write(",".join(daftar_nama))
    print("Data berhasil disimpan.")


def tambah_catatan(nama_file, catatan):
    with open(nama_file, "a") as file:
        file.write(catatan + "\n")
    print("Catatan berhasil ditambahkan.")


def tampilkan_catatan(nama_file):
    try:
        with open(nama_file, "r") as file:
            print("\nIsi file:")
            for baris in file:
                print(baris.strip())
    except FileNotFoundError:
        print("File belum ada.")


def cari_data(nama_file, kata_kunci):
    try:
        with open(nama_file, "r") as file:
            ditemukan = False
            for baris in file:
                if kata_kunci.lower() in baris.lower():
                    print(baris.strip())
                    ditemukan = True
            if not ditemukan:
                print("Data tidak ditemukan.")
    except FileNotFoundError:
        print("File tidak ditemukan.")


# ===== MENU =====
while True:
    print("\n=== MENU FILE I/O ===")
    print("1. Hitung jumlah baris file")
    print("2. Tulis daftar nama ke file")
    print("3. Tambah & tampilkan catatan")
    print("4. Cari data dalam file")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama_file = input("Masukkan nama file: ")
        hasil = hitung_jumlah_baris(nama_file)
        print("Jumlah baris:", hasil)

    elif pilihan == "2":
        nama_file = input("Masukkan nama file: ")
        nama = input("Masukkan nama (pisahkan dengan koma): ")
        daftar_nama = nama.split(",")
        tulis_daftar_nama(nama_file, daftar_nama)

    elif pilihan == "3":
        nama_file = input("Masukkan nama file: ")
        catatan = input("Masukkan catatan: ")
        tambah_catatan(nama_file, catatan)
        tampilkan_catatan(nama_file)

    elif pilihan == "4":
        nama_file = input("Masukkan nama file: ")
        kata_kunci = input("Masukkan kata yang dicari: ")
        cari_data(nama_file, kata_kunci)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")