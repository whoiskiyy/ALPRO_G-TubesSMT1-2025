
#            APLIKASI PENYEWAAN ALAT BERAT


data_alat = [
    ["Excavator", "Tambang", "tersedia", "-", 0],
    ["Bulldozer", "Jalan", "tersedia", "-", 0],
    ["Grader", "Jalan", "tersedia", "-", 0]
]

# paket_sewa menentukan lama sewa berdasarkan pilihan paket
paket_sewa = {1: 3, 2: 7, 3: 14}


ADMIN_PASSWORD = "admin123"

# Menampilkan satu item alat dalam format rapi
def tampilkan_item(item):
    print(
        f"Nama: {item[0]} | Kategori: {item[1]} | Status: {item[2]} | "
        f"Penyewa: {item[3]} | Durasi: {item[4]} hari"
    )



#FUNGSI ADMIN

# Memvalidasi password admin sebelum masuk menu admin
def admin_login():
    print("\n=== Login Admin ===")
    pw = input("Masukkan password: ").strip()

    if pw == ADMIN_PASSWORD:
        print("Login berhasil.\n")
        return True
    else:
        print("Password salah!\n")
        return False


# ---------- CRUD: CREATE ----------
# Menambahkan alat baru ke dalam data_alat
def create():
    print("\n=== Tambah Alat ===")
    nama = input("Nama alat: ").strip()

    while True:
        kategori = input("Kategori (Tambang/Jalan): ").strip().title()
        if kategori in ("Tambang", "Jalan"):
            break
        print("Kategori harus 'Tambang' atau 'Jalan'.")

    # Status default adalah 'tersedia'
    status = input("Status (tersedia/disewa) [default: tersedia]: ").strip().lower()
    if status == "":
        status = "tersedia"
    if status not in ("tersedia", "disewa"):
        print("Status tidak valid, di-set 'tersedia'.")
        status = "tersedia"

    penyewa = input("Nama penyewa (ketik '-' jika kosong): ").strip()
    if penyewa == "":
        penyewa = "-"

    # Validasi durasi harus angka
    while True:
        try:
            durasi_input = input("Durasi sewa (hari) [0 jika belum disewa]: ").strip()
            durasi = int(durasi_input) if durasi_input else 0
            break
        except ValueError:
            print("Durasi harus angka.")

    # Menambahkan data baru ke list utama
    data_alat.append([nama, kategori, status, penyewa, durasi])
    print("Data berhasil ditambahkan.\n")


# ---------- CRUD: READ ----------
# Menampilkan semua alat yang ada
def read_all():
    print("\n=== Semua Alat ===")
    if not data_alat:
        print("Data kosong.\n")
        return
    for item in data_alat:
        tampilkan_item(item)
    print()


# ---------- CRUD: UPDATE ----------
# Mengubah data alat berdasarkan nama
def update():
    print("\n=== Update Data Alat ===")
    nama_cari = input("Nama alat yang ingin diupdate: ").strip().lower()

    for item in data_alat:
        if item[0].lower() == nama_cari:
            print("Data ditemukan:")
            tampilkan_item(item)

            nama_baru = input("Nama baru (enter = lewati): ").strip()
            if nama_baru:
                item[0] = nama_baru

            kategori_baru = input("Kategori baru (Tambang/Jalan) (enter = lewati): ").strip().title()
            if kategori_baru:
                if kategori_baru in ("Tambang", "Jalan"):
                    item[1] = kategori_baru
                else:
                    print("Kategori tidak valid, tidak diubah.")

            status_baru = input("Status baru (tersedia/disewa) (enter = lewati): ").strip().lower()
            if status_baru:
                if status_baru in ("tersedia", "disewa"):
                    item[2] = status_baru
                else:
                    print("Status tidak valid, tidak diubah.")

            penyewa_baru = input("Penyewa baru (enter = lewati): ").strip()
            if penyewa_baru:
                item[3] = penyewa_baru

            while True:
                durasi_baru = input("Durasi baru (hari) (enter = lewati): ").strip()
                if durasi_baru == "":
                    break
                try:
                    item[4] = int(durasi_baru)
                    break
                except ValueError:
                    print("Durasi harus angka.")

            print("Data berhasil diupdate.\n")
            return

    print("Data tidak ditemukan.\n")    


# ---------- CRUD: DELETE ----------
# Menghapus alat berdasarkan nama
def delete():
    print("\n=== Hapus Data Alat ===")
    nama_hapus = input("Nama alat yang ingin dihapus: ").strip().lower()

    for item in data_alat:
        if item[0].lower() == nama_hapus:
            data_alat.remove(item)
            print("Data berhasil dihapus.\n")
            return

    print("Data tidak ditemukan.\n")


# ---------- SEARCH ----------
# Mencari alat berdasarkan nama
def search_by_name():
    print("\n=== Cari Alat (Nama) ===")
    nama_cari = input("Nama alat: ").strip().lower()

    found = False
    for item in data_alat:
        if item[0].lower() == nama_cari:
            tampilkan_item(item)
            found = True

    print() if found else print("Tidak ditemukan.\n")


# ---------- SORTING ----------
# Mengurutkan alat berdasarkan durasi sewa menggunakan bubble sort
def sort_by_durasi():
    print("\n=== Urutkan berdasarkan durasi (ascending) ===")

    # Konversi durasi agar semua pasti integer
    for item in data_alat:
        try:
            item[4] = int(item[4])
        except:
            item[4] = 0

    # Algoritma bubble sort
    n = len(data_alat)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_alat[j][4] > data_alat[j + 1][4]:
                data_alat[j], data_alat[j + 1] = data_alat[j + 1], data_alat[j]

    print("Data telah diurutkan.\n")
    read_all()

# Menampilkan hanya alat yang tersedia
def list_available():
    print("\n=== Alat Tersedia ===")
    found = False
    for item in data_alat:
        if item[2] == "tersedia":
            tampilkan_item(item)
            found = True
    print() if found else print("Tidak ada alat tersedia.\n")


# Menampilkan alat berdasarkan kategori tertentu
def list_by_category():
    print("\n=== Lihat berdasarkan Kategori ===")
    kategori = input("Pilih kategori (Tambang/Jalan): ").strip().title()

    if kategori not in ("Tambang", "Jalan"):
        print("Kategori tidak valid.\n")
        return

    found = False
    for item in data_alat:
        if item[1] == kategori:
            tampilkan_item(item)
            found = True

    print() if found else print("Tidak ada alat di kategori tersebut.\n")


# Buyer mencari alat berdasarkan nama
def buyer_search():
    print("\n=== Cari Alat (Buyer) ===")
    search_by_name()


# Proses penyewaan alat oleh buyer
def buyer_rent():
    print("\n=== Sewa Alat (Buyer) ===")
    print("1. 3 hari\n2. 7 hari\n3. 14 hari")

    try:
        pilihan_paket = int(input("Pilihan paket (1/2/3): ").strip())
        if pilihan_paket not in paket_sewa:
            raise ValueError
    except:
        print("Pilihan paket tidak valid.\n")
        return  

    nama_alat = input("Nama alat yang ingin disewa: ").strip().lower()

    for item in data_alat:
        if item[0].lower() == nama_alat:
            if item[2] != "tersedia":
                print("Maaf, alat sedang tidak tersedia.\n")
                return

            penyewa = input("Nama penyewa: ").strip()
            if penyewa == "":
                print("Nama penyewa tidak boleh kosong.\n")
                return

            # Mengubah status alat menjadi disewa
            item[2] = "disewa"
            item[3] = penyewa
            item[4] = paket_sewa[pilihan_paket]

            print(f"\nSewa berhasil!")
            print(f"Alat: {item[0]} | Durasi: {item[4]} hari | Penyewa: {item[3]}\n")
            return

    print("Alat tidak ditemukan.\n")

#kode untuk tampilan

def admin_menu():
    while True:
        print("""
=== MENU ADMIN ===
1. Tambah alat
2. Tampilkan semua alat
3. Update data alat
4. Hapus alat
5. Cari alat berdasarkan nama
6. Urutkan berdasarkan durasi
7. Kembali
""")

        pilihan = input("Pilih (1-7): ").strip()

        if pilihan == "1": create()
        elif pilihan == "2": read_all()
        elif pilihan == "3": update()
        elif pilihan == "4": delete()
        elif pilihan == "5": search_by_name()
        elif pilihan == "6": sort_by_durasi()
        elif pilihan == "7": break
        else: print("Pilihan tidak valid.\n")


# Menu buyer berisi fitur untuk melihat dan menyewa alat
def buyer_menu():
    while True:
        print("""
=== MENU BUYER ===
1. Lihat alat tersedia
2. Lihat berdasarkan kategori
3. Cari alat
4. Sewa alat
5. Kembali
""")

        pilihan = input("Pilih (1-5): ").strip()

        if pilihan == "1": list_available()
        elif pilihan == "2": list_by_category()
        elif pilihan == "3": buyer_search()
        elif pilihan == "4": buyer_rent()
        elif pilihan == "5": break
        else: print("Pilihan tidak valid.\n")


# Fungsi utama aplikasi
def main():
    print("=== Aplikasi Penyewaan Alat Berat ===")

    while True:
        print("""
=== MENU UTAMA ===
1. Mode Admin
2. Mode Buyer
3. Keluar
""")

        pilihan = input("Pilih (1-3): ").strip()

        if pilihan == "1":
            if admin_login():
                admin_menu()
        elif pilihan == "2": buyer_menu()
        elif pilihan == "3":
            print("Keluar. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.\n")


main()
