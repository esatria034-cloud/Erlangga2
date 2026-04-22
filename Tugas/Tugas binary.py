def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, high, key)
    else:
        return binary_search_recursive(arr, low, mid - 1, key)


data = []

while True:
    print("\n===== MENU TUGAS BINARY SEARCH =====")
    print("1. Input Data (20 Angka)")
    print("2. Tampilkan Data (Sudah Diurutkan)")
    print("3. Cari Data (Iterative)")
    print("4. Cari Data (Recursive)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        data = []
        print("Masukkan 20 angka:")

        for i in range(20):
            try:
                angka = int(input(f"Data ke-{i+1}: "))
                data.append(angka)
            except ValueError:
                print("Harus angka!")
                break

        data.sort()
        print("Data berhasil diinput dan diurutkan")

    elif pilihan == "2":
        if len(data) == 0:
            print("Data kosong")
        else:
            print("Data:", data)

    elif pilihan == "3":
        if len(data) == 0:
            print("Isi data dulu")
        else:
            try:
                key = int(input("Masukkan angka yang dicari: "))
                hasil = binary_search_iterative(data, key)

                if hasil != -1:
                    print(f"Data ditemukan di indeks ke-{hasil}")
                else:
                    print("Data tidak ditemukan")
            except ValueError:
                print("Input harus angka")

    elif pilihan == "4":
        if len(data) == 0:
            print("Isi data dulu")
        else:
            try:
                key = int(input("Masukkan angka yang dicari: "))
                hasil = binary_search_recursive(data, 0, len(data)-1, key)

                if hasil != -1:
                    print(f"Data ditemukan di indeks ke-{hasil}")
                else:
                    print("Data tidak ditemukan")
            except ValueError:
                print("Input harus angka")

    elif pilihan == "5":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")