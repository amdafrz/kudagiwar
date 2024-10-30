def main():
    # Meminta nama user
    name = input("Masukkan nama Anda: ")
    print(f"Selamat datang di Toko Sepatu, {name}!\n")

    # Menu utama
    while True:
        print("Menu:")
        print("1. Lihat Semua Sepatu")
        print("2. Tutup")
        choice = input("Pilih menu: ")

        if choice == "1":
            view_shoes()
        elif choice == "2":
            print("Terima kasih telah berkunjung, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Fungsi untuk menampilkan daftar sepatu
def view_shoes():
    shoes = [
        "Sepatu Nike", "Sepatu Adidas", "Sepatu Puma",
        "Sepatu Reebok", "Sepatu Vans", "Sepatu Converse",
        "Sepatu New Balance", "Sepatu Skechers", "Sepatu Asics",
        "Sepatu Fila"
    ]

    while True:
        print("\nDaftar Sepatu:")
        for i, shoe in enumerate(shoes, start=1):
            print(f"{i}. {shoe}")
        choice = input("Pilih sepatu untuk melihat opsi pembelian (atau ketik 0 untuk kembali): ")

        if choice == "0":
            break

        # Memeriksa pilihan sepatu
        try:
            shoe_index = int(choice) - 1
            if 0 <= shoe_index < len(shoes):
                purchase_option(shoes[shoe_index])
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Input tidak valid, masukkan angka.")

# Fungsi untuk menampilkan opsi pembelian
def purchase_option(shoe):
    while True:
        print(f"\nAnda memilih: {shoe}")
        print("1. Beli")
        print("2. Kembali")
        choice = input("Pilih opsi: ")

        if choice == "1":
            print(f"Anda berhasil membeli {shoe}. Terima kasih!\n")
            break
        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
