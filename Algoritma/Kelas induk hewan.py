# Kelas Induk
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara."

    def bergerak(self):
        return f"{self.nama} sedang bergerak."


# Kelas Anak: Anjing
class Anjing(Hewan):
    def __init__(self, nama, umur, ras):
        super().__init__(nama, umur)
        self.ras = ras

    def bersuara(self):  # Override
        return f"{self.nama} si {self.ras} menggonggong: Guk Guk!"

    def gonggong(self):
        return f"{self.nama} sedang menggonggong."


# Kelas Anak: Kucing
class Kucing(Hewan):
    def __init__(self, nama, umur, warna_bulu):
        super().__init__(nama, umur)
        self.warna_bulu = warna_bulu

    def bersuara(self):  # Override
        return f"{self.nama} si kucing berkata: Meong!"

    def meong(self):
        return f"{self.nama} sedang mengeong."


# Program utama
print("=== DATA HEWAN ===")

anjing1 = Anjing("Buddy", 3, "Golden Retriever")
kucing1 = Kucing("Milo", 2, "Putih")

print(anjing1.bersuara())
print(anjing1.bergerak())
print(anjing1.gonggong())

print()

print(kucing1.bersuara())
print(kucing1.bergerak())
print(kucing1.meong())