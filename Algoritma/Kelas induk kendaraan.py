# Kelas Induk
class Kendaraan:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def info(self):
        return f"{self.merek} {self.model} ({self.tahun})"

    def start(self):
        return "Mesin dinyalakan"

    def stop(self):
        return "Mesin dimatikan"


# Kelas Anak: Mobil
class Mobil(Kendaraan):
    def __init__(self, merek, model, tahun, jumlah_pintu):
        super().__init__(merek, model, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"{self.merek} {self.model}, {self.tahun}, Pintu: {self.jumlah_pintu}"

    def klakson(self):
        return "Tin Tin!"


# Kelas Anak: Motor
class Motor(Kendaraan):
    def __init__(self, merek, model, tahun, tipe):
        super().__init__(merek, model, tahun)
        self.tipe = tipe

    def info(self):
        return f"{self.merek} {self.model}, {self.tahun}, Tipe: {self.tipe}"

    def gas(self):
        return "Vroom Vroom!"


# Program utama
print("\n=== DATA KENDARAAN ===")

mobil1 = Mobil("Toyota", "Fortuner", 2022, 4)
motor1 = Motor("Honda", "Genio", 2021, "Matic")

print(mobil1.info())
print(mobil1.start())
print(mobil1.klakson())

print()

print(motor1.info())
print(motor1.start())
print(motor1.gas())