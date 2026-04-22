# Fungsi format rupiah Indonesia
def format_uang(angka):
    return "Rp {:,}".format(angka).replace(",", ".")


# ======================
# KELAS INDUK
# ======================
class Pegawai:
    def __init__(self, nama, id_pegawai, gaji_pokok):
        self.nama = nama
        self.id_pegawai = id_pegawai
        self.gaji_pokok = gaji_pokok

    def info_pegawai(self):
        return f"{self.nama} ({self.id_pegawai})"

    def hitung_gaji_kotor(self):
        return self.gaji_pokok

    def hitung_pajak(self):
        return int(self.hitung_gaji_kotor() * 0.05)

    def hitung_gaji_bersih(self):
        return self.hitung_gaji_kotor() - self.hitung_pajak()

    def jabatan(self):
        return "Pegawai"


# ======================
# KELAS MANAJER
# ======================
class Manajer(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, id_pegawai, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    def hitung_gaji_kotor(self):
        return self.gaji_pokok + self.tunjangan_jabatan

    def jabatan(self):
        return "Manajer"

    def kelola_tim(self):
        return f"Manajer {self.nama} sedang mengelola tim."


# ======================
# KELAS KARYAWAN STAF
# ======================
class KaryawanStaf(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_pokok, jam_lembur, tarif_lembur_per_jam):
        super().__init__(nama, id_pegawai, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur_per_jam = tarif_lembur_per_jam

    def hitung_gaji_kotor(self):
        return self.gaji_pokok + (self.jam_lembur * self.tarif_lembur_per_jam)

    def jabatan(self):
        return "Karyawan Staf"

    def kerjakan_tugas(self):
        return f"Karyawan {self.nama} sedang mengerjakan tugas."


# ======================
# DATA / OBJEK
# ======================
pegawai1 = Pegawai("Satria Erlangga", "PG01", 4000000)
manajer1 = Manajer("Hafiz Danu Pratama", "MN01", 7000000, 2000000)
staf1 = KaryawanStaf("Fauzi Abimanyu", "ST01", 3500000, 10, 50000)

data_pegawai = [pegawai1, manajer1, staf1]


# ======================
# OUTPUT
# ======================
print("=" * 50)
print("SISTEM PERSONALIA PERUSAHAAN")
print("=" * 50)

for i, p in enumerate(data_pegawai, start=1):
    print(f"\nData Pegawai ke-{i}")
    print("-" * 50)

    print("Nama dan ID     :", p.info_pegawai())
    print("Jabatan         :", p.jabatan())

    gaji_kotor = p.hitung_gaji_kotor()
    pajak = p.hitung_pajak()
    gaji_bersih = p.hitung_gaji_bersih()

    print("Gaji Kotor      :", format_uang(gaji_kotor))
    print("Pajak (5%)      :", format_uang(pajak))
    print("Gaji Bersih     :", format_uang(gaji_bersih))

    if isinstance(p, Manajer):
        print("Keterangan      :", p.kelola_tim())
    elif isinstance(p, KaryawanStaf):
        print("Keterangan      :", p.kerjakan_tugas())

print("\n" + "=" * 50)
print("Data selesai ditampilkan")
print("=" * 50)