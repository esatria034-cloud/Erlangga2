def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def cari_dan_cetak(arr, target):
    print(f"\nMencari angka: {target}")
    hasil = linear_search(arr, target)
    if hasil != -1:
        print(f"=> DITEMUKAN di indeks [{hasil}]")
    else:
        print("=> TIDAK DITEMUKAN dalam array")

data = [15, 32, 7, 49, 85, 23, 61, 4, 90, 38]

while True:
    print("\n=====================================")
    print("       MENU LINEAR SEARCH")
    print("=====================================")
    print("1. Tampilkan Array")
    print("2. Cari Angka")
    print("3. Ganti Data Array")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print("\nArray  :", end=" ")
        for i in range(len(data)):
            print(f"{i:3}", end=" ")

        print("\nIndeks :", end=" ")
        for x in data:
            print(f"{x:3}", end=" ")

        print()

    elif pilihan == "2":
        try:
            angka = int(input("\nMasukkan angka yang ingin dicari: "))
            cari_dan_cetak(data, angka)
        except ValueError:
            print("Input harus berupa angka!")

    elif pilihan == "3":
        try:
            jumlah = int(input("Masukkan jumlah data: "))
            data = []
            for i in range(jumlah):
                nilai = int(input(f"Masukkan nilai ke-{i}: "))
                data.append(nilai)
            print("Data berhasil diperbarui!")
        except ValueError:
            print("Input harus berupa angka!")

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")