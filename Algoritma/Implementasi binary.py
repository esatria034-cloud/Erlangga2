def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        print(f"\nLow: {low}, High: {high}, Mid: {mid}, Nilai Tengah: {mid_value}")

        if mid_value == key:
            return mid
        elif mid_value < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


data_array = [10, 20, 30, 40, 50, 60, 70]

while True:
    print("\n===== MENU BINARY SEARCH =====")
    print("1. Tampilkan Data")
    print("2. Cari Angka")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        print("Data:", data_array)

    elif pilihan == "2":
        try:
            key = int(input("Masukkan angka yang dicari: "))
            hasil = binary_search(data_array, key)

            if hasil != -1:
                print(f"Angka ditemukan di indeks ke-{hasil}")
            else:
                print("Angka tidak ditemukan")
        except ValueError:
            print("Input harus angka")

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")