class Buku:
    def __init__(self, id_buku, judul, penulis, tahun):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"ID: {self.id_buku}, Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"


def binary_search_buku(daftar, target):
    low = 0
    high = len(daftar) - 1

    while low <= high:
        mid = (low + high) // 2

        if daftar[mid].id_buku == target:
            return daftar[mid]
        elif daftar[mid].id_buku < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


daftar_buku = [
    Buku("A001", "Dasar Python", "Andi", 2021),
    Buku("A002", "Algoritma", "Budi", 2023),
    Buku("A003", "Struktur Data", "Citra", 2022),
    Buku("A004", "Machine Learning", "Dwi", 2024),
    Buku("A005", "Jaringan", "Eka", 2020),
    Buku("A006", "Sistem Operasi", "Fahmi", 2021),
    Buku("A007", "Basis Data", "Gita", 2023)
]

while True:
    print("\n===== MENU PENCARIAN BUKU =====")
    print("1. Tampilkan Buku")
    print("2. Cari Buku")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        for buku in daftar_buku:
            print(buku)

    elif pilih == "2":
        id_cari = input("Masukkan ID Buku: ")
        hasil = binary_search_buku(daftar_buku, id_cari)

        if hasil:
            print("Buku ditemukan:")
            print(hasil)
        else:
            print("Buku tidak ditemukan")

    elif pilih == "3":
        print("Selesai")
        break

    else:
        print("Pilihan salah")