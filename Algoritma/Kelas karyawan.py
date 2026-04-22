# Kelas Induk
class Karyawan:
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan

    def hitung_gaji(self):
        raise NotImplementedError("Metode 'hitung_gaji' harus diimplementasikan oleh subclass.")

    def info_karyawan(self):
        return f"ID: {self.id_karyawan}, Nama: {self.nama}"


# Kelas Anak
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_bulanan, tunjangan=0):
        super().__init__(nama, id_karyawan)
        self.gaji_bulanan = gaji_bulanan
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_bulanan + self.tunjangan


class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, jam_kerja, tarif_per_jam):
        super().__init__(nama, id_karyawan)
        self.jam_kerja = jam_kerja
        self.tarif_per_jam = tarif_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.tarif_per_jam


# Contoh penggunaan
karyawan1 = KaryawanTetap("Budi Santoso", "K001", 7000000, 1000000)
karyawan2 = KaryawanKontrak("Citra Dewi", "K002", 160, 50000)

daftar_karyawan = [karyawan1, karyawan2]

print("--- Laporan Gaji Karyawan ---")
for karyawan in daftar_karyawan:
    print(karyawan.info_karyawan())
    print("Gaji Bersih:", karyawan.hitung_gaji())
    print()