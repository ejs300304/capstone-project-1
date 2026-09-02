product = [
{"product_id": 101, "name": "LAPTOP", "price": 15000000, "stock": 5},
{"product_id": 102, "name": "MOUSE", "price": 100000, "stock": 10},
{"product_id": 103, "name": "KEYBOARD", "price": 300000, "stock": 8},
{"product_id": 104, "name": "MONITOR", "price": 2000000, "stock": 3},
{"product_id": 105, "name": "HEADPHONE", "price": 500000, "stock": 12},
{"product_id": 106, "name": "LAPTOP GAMING", "price": 2000000, "stock": 15}
]

# Code untuk mendapatkan product by ID
def find_product(product_id):
    for p in product:
        if p["product_id"] == product_id:
            return p
    return None

# Code untuk login
def login():
    no_coba = 0
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == "Elbert" and password == "1234e": # Hardcode username dan password
            print("Login berhasil!")
            return True
        else:
            print("Username atau password salah!")
            no_coba += 1
            if no_coba == 3: # Max 3 percobaan
                print("Anda telah mencoba login sebanyak 3 kali. Program akan berhenti.")
                exit()

# Code untuk menu read
def menu_read():
    while True:
        print("\n Menu Read")
        print("1. Report Seluruh Data")
        print("2. Report Data Tertentu")
        print("3. Kembali")
        opsi_read = input("Pilih menu: ")

        if opsi_read == "1":
            if len(product) == 0:
                print("Belum ada data barang.")
            else:
                print("-" * 60)
                print(f"{'Product ID':<5}{'Name':<20}{'Price':<20}{'Stock':<10}")
                print("-" * 60)
                for item in product:
                    print(f"{item['product_id']:<5}{item['name']:<20}Rp{item['price']:<10,}{item['stock']:<4}")
                print("-" * 60)
        elif opsi_read == "2":
            # Menu untuk mencari data tertentu
            while True:
                print("\n Pilih Kriteria Pencarian:")
                print("1. Berdasarkan Product ID")
                print("2. Berdasarkan Nama Barang")
                no_criteria = input("Pilihan: ")
                # Mencari data Dengan ID
                if no_criteria == "1":
                    product_id_input = input("Masukkan Product ID : ")
                    if not product_id_input.isdigit() or len(product_id_input) != 3 or int(product_id_input) <= 0:
                        print("Product ID harus berupa 3 digit angka positif!")
                        continue

                    product_id = int(product_id_input)
                    found_product = find_product(product_id)

                    # Menampilkan hasil pencarian
                    if found_product:
                        print(f"\nID    : {found_product['product_id']}")
                        print(f"Nama  : {found_product['name']}")
                        print(f"Harga : Rp{found_product['price']:,}")
                        print(f"Stock  : {found_product['stock']}")
                    else:
                        print("Product ID tidak ditemukan.")
                # Mencari data dengan nama
                elif no_criteria == "2":
                    name_input = input("Masukkan Nama Barang : ").upper()
                    search_result = [p for p in product if name_input in p["name"]]
                    if len(search_result) > 0:
                        print("\n Hasil Pencarian:")
                        print("-" * 60)
                        print(f"{'Product ID':<5}{'Name':<20}{'Price':<20}{'Stock':<10}")
                        print("-" * 60)
                        for item in search_result:
                            print(f"{item['product_id']:<5}{item['name']:<20}Rp{item['price']:<10,}{item['stock']:<4}")
                        print("-" * 60)
                    else:
                        print("Barang dengan nama tersebut tidak ditemukan.")
                else:
                    print("Kriteria pencarian tidak valid.")
                    continue

                search_again = input("Cari lagi? (Y/N): ").upper()
                if search_again != "Y":
                    break
        elif opsi_read == "3":
            break
        else:
            print("Pilihan tidak valid.")

# Code untuk menu create
def menu_create():
    while True:
        print("\n MENU CREATE")
        print("1. Tambah Data")
        print("2. Kembali")
        opsi_create = input("Pilih menu: ")
        if opsi_create == "1":
            while True:
                # Validasi Product ID harus berupa 3 digit angka positif dan tidak boleh duplikat
                product_id_input = input("Masukkan Product ID : ")
                if not product_id_input.isdigit() or len(product_id_input) != 3 or int(product_id_input) <= 0:
                    print("Product ID harus berupa 3 digit angka positif!")
                elif any(p["product_id"] == int(product_id_input) for p in product):
                    print(f"Product ID {product_id_input} sudah terdaftar.")
                else:
                    product_id = int(product_id_input)
                    break

            while True:
                name = input("Masukkan Nama Product : ")
                # Validasi nama product hanya boleh mengandung huruf dan tidak boleh kosong
                if name == "" or not name.replace(" ", "").isalpha():
                    print("Nama product hanya boleh mengandung huruf dan tidak boleh kosong!")
                else:
                    name = name.upper()
                    # Fitur Validasi Nama Duplikat
                    if any(p["name"] == name for p in product):
                        print(f"Barang dengan nama '{name}' sudah ada di dalam database. Gunakan nama yang berbeda")
                    else:
                        break

            while True:
                # Validasi harga harus berupa angka lebih besar dari 0
                price_input = input("Masukkan Harga Product : ")
                if not price_input.isdigit() or int(price_input) <= 0:
                    print("Harga harus berupa angka lebih besar dari 0!")
                else:
                    price = int(price_input)
                    break

            while True:
                # Validasi stock harus berupa angka lebih besar dari 0
                stock_input = input("Masukkan Stock Product : ")
                if not stock_input.isdigit() or int(stock_input) <= 0:
                    print("Stock harus berupa angka lebih besar dari 0!")
                else:
                    stock = int(stock_input)
                    break

            print("\n Ringkasan Data")
            print(f"ID    : {product_id}")
            print(f"Nama  : {name}")
            print(f"Harga : Rp{price:,}")
            print(f"Stock  : {stock}")
            simpan = input("Simpan data? (Y/N): ").upper()
            if simpan == "Y":
                product.append({"product_id": product_id, "name": name, "price": price, "stock": stock})
                print(f"Data product '{name}' berhasil disimpan")
            else:
                print("Data batal disimpan.")
        elif opsi_create == "2":
            break
        else:
            print("Pilihan tidak valid.")

def menu_update():
    while True:
        print("\n Menu Update")
        print("1. Ubah Data")
        print("2. Kembali")
        opsi_update = input("Pilih menu: ")
        if opsi_update == "1":
            while True:
                # Validasi Product ID harus berupa 3 digit angka positif
                product_id_input = input("Masukkan Product ID : ")
                if not product_id_input.isdigit() or len(product_id_input) != 3 or int(product_id_input) <= 0:
                    print("Product ID harus berupa 3 digit angka!")
                    continue
                product_id = int(product_id_input)
                found_product = find_product(product_id)
                if not found_product:
                    print("Product ID tidak ditemukan.")
                    search_again = input("Cari lagi? (Y/N): ").upper()
                    if search_again != "Y":
                        break
                    continue

                print(f"\n Data barang saat ini:")
                print(f"Nama  : {found_product['name']}")
                print(f"Harga : Rp{found_product['price']:,}")
                print(f"Stock  : {found_product['stock']}")

                lanjut = input("Lanjut update? (Y/N): ").upper()
                if lanjut != "Y":
                    break
                while True:
                    print("\nPilih kolom yang akan diubah:")
                    print("1. Nama")
                    print("2. Harga")
                    print("3. Stock")
                    kolom = input("Pilih (1-3): ")

                    if kolom == "1":
                        while True:
                            new_val = input("Masukkan Nama baru: ")
                            if new_val == "" or not new_val.replace(" ", "").isalpha():
                                print("Nama hanya boleh mengandung huruf dan tidak boleh kosong!")
                            else:
                                new_val = new_val.upper()
                                # Validasi duplikat nama saat update (mengabaikan barang ini sendiri)
                                if any(p["name"] == new_val for p in product if p["product_id"] != product_id):
                                    print(f"Barang dengan nama '{new_val}' sudah digunakan barang lain!")
                                else:
                                    field_name = "name"
                                    break
                        break
                    elif kolom == "2":
                        while True:
                            price_input = input("Masukkan Harga baru: ")
                            if not price_input.isdigit() or int(price_input) <= 0:
                                print("Harga harus berupa angka lebih besar dari 0!")
                            else:
                                new_val = int(price_input)
                                field_name = "price"
                                break
                        break
                    elif kolom == "3":
                        while True:
                            stock_input = input("Masukkan Stock baru: ")
                            if not stock_input.isdigit() or int(stock_input) < 0:
                                print("Stock tidak boleh negatif!")
                            else:
                                new_val = int(stock_input)
                                field_name = "stock"
                                break
                        break
                    else:
                        print("Kolom tidak valid.")
                print("\n Perubahan Data")
                print(f"Kolom : {field_name.upper()}")
                print(f"Lama  : {found_product[field_name]}")
                print(f"Baru  : {new_val}")

                confirm = input("Update data? (Y/N): ").upper()
                if confirm == "Y":
                    found_product[field_name] = new_val
                    print("Update berhasil")
                else:
                    print("Update dibatalkan.")
                break
        elif opsi_update == "2":
            break
        else:
            print("Pilihan tidak valid.")

# Code untuk menu delete
def menu_delete():
    while True:
        print("\n Menu Delete")
        print("1. Hapus Data")
        print("2. Kembali")
        opsi_delete = input("Pilih menu: ")
        if opsi_delete == "1":
            while True:
                product_id_input = input("Masukkan Product ID : ")
                if not product_id_input.isdigit() or len(product_id_input) != 3 or int(product_id_input) <= 0:
                    print("Product ID harus berupa 3 digit angka positif!")
                    continue

                product_id = int(product_id_input)
                found_product = find_product(product_id)

                if not found_product:
                    print("Product ID tidak ditemukan.")
                    search_again = input("Cari lagi? (Y/N): ").upper()
                    if search_again != "Y":
                        break
                    continue

                print("\n Data yang akan dihapus:")
                print(f"ID    : {found_product['product_id']}")
                print(f"Nama  : {found_product['name']}")
                print(f"Harga : Rp{found_product['price']:,}")
                print(f"Stock  : {found_product['stock']}")

                confirm = input("Hapus data? (Y/N): ").upper()
                if confirm == "Y":
                    cart.append(found_product)
                    product.remove(found_product)
                    print(f"Product ID {product_id} berhasil dipindahkan ke Cart Hapus")
                else:
                    print("Penghapusan dibatalkan.")
                break
        elif opsi_delete == "2":
            break
        else:
            print("Pilihan tidak valid.")

# Code untuk menu recycle bin (cart)
cart = []
def trash_cart():
    while True:
        print("\n Menu Recycle Bin (Cart)")
        print("1. Lihat Barang Terhapus")
        print("2. Restore Barang")
        print("3. Hapus Barang")
        print("4. Kembali")
        opsi_trash = input("Pilih menu: ")
        if opsi_trash == "1":
            if len(cart) == 0:
                print("Cart kosong.")
            else:
                print("-" * 60)
                print(f"{'Product ID':<5}{'Name':<20}{'Price':<20}{'Stock':<10}")
                print("-" * 60)
                for item in cart:
                    print(f"{item['product_id']:<5}{item['name']:<20}Rp{item['price']:<10,}{item['stock']:<4}")
                print("-" * 60)
        elif opsi_trash == "2":
            if len(cart) == 0:
                print("Cart kosong.")
                continue

            input_id = input("Masukkan Product ID yang ingin di restore: ")
            if not input_id.isdigit():
                print("ID harus berupa angka!")
                continue

            found_trash = None
            for p in cart:
                if p["product_id"] == int(input_id):
                    found_trash = p
                    break

            if found_trash:
                product.append(found_trash)
                cart.remove(found_trash)
                print(f"Product '{found_trash['name']}' berhasil dikembalikan ke list utama")
            else:
                print("Product ID tidak ditemukan di dalam Cart.")

        elif opsi_trash == "3":
            if len(cart) == 0:
                print("Cart kosong.")
                continue

            input_id = input("Masukkan Product ID yang ingin dihapus: ")
            if not input_id.isdigit():
                print("ID harus berupa angka")
                continue
            found_trash = None
            for p in cart:
                if p["product_id"] == int(input_id):
                    found_trash = p
                    break

            if found_trash:
                confirm = input(f"Yakin ingin menghapus {found_trash['name']} permanen? (Y/N): ").upper()
                if confirm == "Y":
                    cart.remove(found_trash)
                    print("Barang berhasil dihapus permanen!")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print("Product ID tidak ditemukan di dalam Cart.")
        elif opsi_trash == "4":
            break
        else:
            print("Pilihan tidak valid.")

def menu_utama():
    if not login():
        return
    while True:
        print("\n Menu Utama")
        print("1. Baca Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Recycle Bin (Cart)")
        print("6. Exit")
        opsi = input("Pilih menu: ")
        if opsi == "1":
            menu_read()
        elif opsi == "2":
            menu_create()
        elif opsi == "3":
            menu_update()
        elif opsi == "4":
            menu_delete()
        elif opsi == "5":
            trash_cart()
        elif opsi == "6":
            print("Program selesai.")
            break
        else:
            print("Opsi Tidak valid")

menu_utama()
