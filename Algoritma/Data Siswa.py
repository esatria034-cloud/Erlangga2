# Membuat list untuk menyimpan data siswa 
siswa = []

# Fungsi untuk menambahkan siswa 
def tambah_siswa(nama, nilai):
    siswa.append({"nama": nama, "nilai": nilai})

# Fungsi untuk menghapus siswa 
def hapus_siswa(nama):
    for s in siswa:
        if s["nama"] == nama:
            siswa.remove(s)
            print(f"Siswa {nama} telah dihapus.")
            return
    print(f"Siswa {nama} tidak ditemukan.")

# Fungsi untuk menghitung rata-rata nilai 
def hitung_rata_rata():
    if len(siswa) == 0:
        return 0
    total_nilai = sum(s["nilai"] for s in siswa)
    return total_nilai / len(siswa)

# Fungsi untuk mencetak daftar siswa 
def cetak_daftar_siswa():
    print("Daftar Siswa:")
    for s in siswa:
        print(f"Nama: {s['nama']}, Nilai: {s['nilai']}")

# Fungsi untuk mengurutkan siswa berdasarkan nilai 
def urutkan_siswa():
    siswa.sort(key=lambda x: x["nilai"])
    print("Siswa telah diurutkan berdasarkan nilai.")

# Menambahkan beberapa siswa 
tambah_siswa("Budi", 85) 
tambah_siswa("Sari", 90) 
tambah_siswa("Andi", 78)

# Mencetak daftar siswa 
cetak_daftar_siswa()

# Menghitung dan mencetak rata-rata nilai 
rata_rata = hitung_rata_rata()
print(f"Rata-rata nilai: {rata_rata}")

# Menghapus siswa 
hapus_siswa("Andi")

# Mencetak daftar siswa setelah penghapusan 
cetak_daftar_siswa()

# Mengurutkan siswa 
urutkan_siswa()

# Mencetak daftar siswa setelah diurutkan 
cetak_daftar_siswa()