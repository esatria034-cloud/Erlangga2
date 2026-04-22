class Produk:
    def __init__(self, sku, nama_produk, stok):
        self.sku = sku
        self.nama_produk = nama_produk
        self.stok = stok

    def __str__(self):
        return f"SKU: {self.sku}, Nama Produk: {self.nama_produk}, Stok: {self.stok}"

def cari_produk_linear(daftar_produk, sku_target):
    for produk in daftar_produk:
        if produk.sku == sku_target:
            return produk
    return None

data_produk = [
    Produk("ELC-001", "Laptop Gaming X", 5),
    Produk("ELC-002", "Smartphone Pro", 12),
    Produk("ELC-003", "Monitor UltraWide", 3),
    Produk("ELC-004", "Keyboard Mekanik", 20),
    Produk("ELC-005", "Mouse Wireless", 35)
]

while True:
    print("\n===== SISTEM PENCARIAN PRODUK =====")
    print("1. Tampilkan Semua Produk")
    print("2. Cari Produk berdasarkan SKU")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        print("\nDaftar Produk:")
        for produk in data_produk:
            print(produk)

    elif pilihan == "2":
        sku_input = input("\nMasukkan SKU produk yang ingin dicari: ")
        hasil = cari_produk_linear(data_produk, sku_input)

        if hasil:
            print("\nProduk ditemukan:")
            print(hasil)
        else:
            print("\nProduk tidak ditemukan")

    elif pilihan == "3":
        print("\nProgram selesai")
        break

    else:
        print("\nPilihan tidak valid, coba lagi")