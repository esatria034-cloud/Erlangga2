def binary_search_suhu(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


data_suhu = [18.5, 19.0, 20.1, 21.5, 22.0, 22.8, 23.5, 24.0, 25.3, 26.0, 27.1, 28.5]

print("Data Suhu:", data_suhu)

suhu_dicari = [23.5, 21.0, 30.0, 18.5]

for s in suhu_dicari:
    hasil = binary_search_suhu(data_suhu, s)

    if hasil != -1:
        print(f"Suhu {s} ditemukan di indeks {hasil}")
    else:
        print(f"Suhu {s} tidak ditemukan")