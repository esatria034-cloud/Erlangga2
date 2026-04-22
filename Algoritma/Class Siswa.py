class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"

def cari_mahasiswa_linear(daftar_mahasiswa, nim_target):
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.nim == nim_target:
            return mahasiswa
    return None

data_mahasiswa = [
    Mahasiswa("241011450391", "Satria Erlangga", "Teknik Informatika"),
    Mahasiswa("241011450392", "Siti Aminah", "Sistem Informasi"),
    Mahasiswa("241011450393", "Ahmad Fauzi", "Manajemen Bisnis"),
    Mahasiswa("241011450394", "Dewi Lestari", "Akuntansi"),
    Mahasiswa("241011450395", "Rina Susanti", "Teknik Elektro")
]

while True:
    print("\n===== SISTEM DATA MAHASISWA =====")
    print("1. Tampilkan Semua Data")
    print("2. Cari Mahasiswa berdasarkan NIM")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        print("\nDaftar Mahasiswa:")
        for mhs in data_mahasiswa:
            print(mhs)

    elif pilihan == "2":
        nim_input = input("\nMasukkan NIM yang dicari: ")
        hasil = cari_mahasiswa_linear(data_mahasiswa, nim_input)

        if hasil:
            print("\nData ditemukan:")
            print(hasil)
        else:
            print("\nMahasiswa tidak ditemukan")

    elif pilihan == "3":
        print("\nProgram selesai")
        break

    else:
        print("\nPilihan tidak valid, coba lagi")