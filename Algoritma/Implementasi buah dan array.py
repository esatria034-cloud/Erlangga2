def linear_search(arr, target):
    """
    Melakukan pencarian linear pada sebuah list.
    Args:
        arr (list): List data yang akan dicari.
        target: Nilai yang ingin dicari.
    Returns:
        int: Indeks dari target jika ditemukan, -1 jika tidak ditemukan.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Data contoh
data_angka = [15, 22, 10, 30, 5, 88, 7]
daftar_buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

print("=" * 50)
print("PROGRAM LINEAR SEARCH - PENCARIAN ANGKA DAN BUAH")
print("=" * 50)

while True:
    print("\n" + "-" * 30)
    print("PILIH JENIS PENCARIAN:")
    print("1. Cari Angka")
    print("2. Cari Buah")
    print("3. Keluar")
    print("-" * 30)

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        # Pencarian angka
        print(f"\nData angka yang tersedia: {data_angka}")
        try:
            nilai_dicari = int(input("Masukkan angka yang ingin dicari: "))
            indeks = linear_search(data_angka, nilai_dicari)

            print("-" * 30)
            if indeks != -1:
                print(f"✓ Nilai {nilai_dicari} DITEMUKAN pada indeks: {indeks}")
            else:
                print(f"✗ Nilai {nilai_dicari} TIDAK DITEMUKAN.")
            print("-" * 30)
        except ValueError:
            print("✗ Input tidak valid! Masukkan angka yang benar.")

    elif pilihan == "2":
        # Pencarian buah
        print(f"\nDaftar buah yang tersedia: {daftar_buah}")
        buah_dicari = input("Masukkan nama buah yang ingin dicari: ").lower()
        indeks_buah = linear_search(daftar_buah, buah_dicari)

        print("-" * 30)
        if indeks_buah != -1:
            print(f"✓ Buah '{buah_dicari}' DITEMUKAN pada indeks: {indeks_buah}")
        else:
            print(f"✗ Buah '{buah_dicari}' TIDAK DITEMUKAN.")
        print("-" * 30)

    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program!")
        break

    else:
        print("\n✗ Pilihan tidak valid! Masukkan 1, 2, atau 3.")