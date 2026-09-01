# capstone-project-1
Store Data Management

Program sederhana berbasis Python untuk mengelola data barang pada sebuah toko.

Project Overview
Program digunakan untuk menyimpan dan mengelola data barang toko yang terdiri dari:

Product ID
Nama barang
Harga
Stock

Data barang disimpan dalam bentuk list of dictionaries.

Program Flow
                    START
                      │
                      ▼
                 ┌─────────┐
                 │  LOGIN  │
                 └────┬────┘
                      │
              ┌───────┴────────┐
              │                │
          Login Berhasil    Login Gagal
              │                │
              │          Maks. 3 Percobaan
              ▼                │
        ┌──────────────┐       │
        │ MENU UTAMA   │◄──────┘
        └──────┬───────┘
               │
      ┌────────┼────────┬────────┬────────────┐
      ▼        ▼        ▼        ▼            ▼
    READ     CREATE   UPDATE   DELETE     RECYCLE BIN
      │        │        │        │            │
      │        │        │        │       ┌────┴────┐
      │        │        │        │       ▼         ▼
      │        │        │        │    RESTORE   DELETE
      │        │        │        │
      └────────┴────────┴────────┴──────────────┐
                                                │
                                                ▼
                                             EXIT

1. Login

Sebelum masuk ke program, user harus melakukan login.

Jika username atau password salah, user dapat mencoba kembali hingga 3 kali. Jika gagal sebanyak 3 kali, program akan berhenti.

2. Read Data

Menu Read digunakan untuk melihat data barang.

Terdapat dua pilihan:

Report Seluruh Data
Menampilkan seluruh barang yang tersedia.
Report Data Tertentu
Mencari barang berdasarkan:
Product ID
Nama barang

User juga dapat melakukan pencarian kembali jika diperlukan.

3. Create Data

Menu Create digunakan untuk menambahkan barang baru ke dalam data toko.

Sebelum data disimpan, program melakukan validasi terhadap:

Product ID harus berupa 3 digit angka positif.
Product ID tidak boleh duplikat.
Nama barang tidak boleh kosong.
Nama barang hanya boleh mengandung huruf.
Nama barang tidak boleh duplikat.
Harga harus berupa angka lebih dari 0.
Stock harus berupa angka lebih dari 0.

Setelah data diisi, user akan melihat ringkasan data dan melakukan konfirmasi sebelum menyimpan.

4. Update Data

Menu Update digunakan untuk mengubah data barang yang sudah tersedia.

User dapat mencari barang berdasarkan Product ID, kemudian memilih data yang ingin diubah:

Nama
Harga
Stock

Program juga melakukan validasi terhadap data baru sebelum perubahan disimpan.

5. Delete Data

Menu Delete digunakan untuk menghapus barang dari data utama.

Barang yang dihapus tidak langsung hilang secara permanen, tetapi dipindahkan terlebih dahulu ke Recycle Bin (Cart).

6. Recycle Bin

Recycle Bin digunakan untuk mengelola barang yang sudah dihapus.

Terdapat beberapa pilihan:

Lihat Barang Terhapus
Restore Barang
Hapus Barang Permanen
Kembali ke Menu Utama

Barang yang di-restore akan dikembalikan ke data utama, sedangkan barang yang dihapus dari Recycle Bin akan dihapus secara permanen.

Main Flow
Secara keseluruhan, flow program adalah:

Login → Menu Utama → Read / Create / Update / Delete / Recycle Bin → kembali ke Menu Utama → Exit
