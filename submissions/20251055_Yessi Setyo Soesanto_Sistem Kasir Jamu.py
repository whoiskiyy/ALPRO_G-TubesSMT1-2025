import datetime # Import modul untuk mendapatkan waktu dan tanggal transaksi.

# List untuk menyimpan data menu jamu (nama dan harga) 
menu_jamu = [
    {"nama": "Jamu Kunyit Asam Fresh 500ml", "harga": 25000},
    {"nama": "Jahe Merah Gula Jawa 500ml", "harga": 25000},
    {"nama": "Jamu Beras Kencur 500ml", "harga": 25000},
    {"nama": "Kunyit Putih 500ml", "harga": 30000},
    {"nama": "STMJ 500ml", "harga": 45000}
]

# ID unik untuk setiap transaksi yang selesai
id_transaksi_counter = 1

def tampilkan_menu_jamu():
    """Fungsi untuk menampilkan daftar menu jamu yang tersedia."""
    print("+===========================================+")
    print("|          MENU JAMU HERBAL MBAH            |")
    print("+===========================================+")
    for i, item in enumerate(menu_jamu): #Menggunakan enumerate() untuk mendapatkan Index (i) dan Item
        harga_rp = f"Rp {item['harga']:,}".replace(',', '.') # Memformat harga ke Rupiah 
        print(f"| {i+1}. {item['nama']:<32} | {harga_rp:>10} |") # Mencetak No Urut (i+1), Nama, dan Harga.
    print("+===========================================+")

# ================================================================= #
# FUNGSI-FUNGSI UNTUK MENGELOLA TRANSAKSI YANG SEDANG BERJALAN (KERANJANG)
# ================================================================= #

def tambah_item_ke_keranjang(keranjang): # fungsi ny utk menambah item ke keranjang
    """Menambahkan item baru ke keranjang belanja pembeli saat ini."""
    tampilkan_menu_jamu()
    try:
        pilihan_menu = int(input("Pilih menu jamu (nomor): "))
        if not (1 <= pilihan_menu <= len(menu_jamu)): # VALIDASI 1: Cek nomor menu valid (ada di list)
            print("Pilihan tidak valid.")
            return keranjang

        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
        if jumlah <= 0: # VALIDASI 2: Cek jumlah > 0.
            print("Jumlah harus lebih dari 0.")
            return keranjang

    except ValueError:
        print("Input tidak valid, harap masukkan angka.")
        return keranjang

    item_terpilih = menu_jamu[pilihan_menu - 1]
    # Struktur item di keranjang: [nama, harga, jumlah, subtotal]
    item_baru = [item_terpilih["nama"], item_terpilih["harga"], jumlah, item_terpilih["harga"] * jumlah]
    keranjang.append(item_baru)
    print(f">> Berhasil menambahkan '{item_terpilih['nama']}' ke keranjang.")
    return keranjang

def lihat_keranjang(keranjang):
    """Melihat item apa saja yang ada di keranjang pembeli saat ini."""
    if not keranjang:
        print("Keranjang belanja masih kosong.")
        return

    print("+======================================================================+")
    print("|                         KERANJANG BELANJA                          |")
    print("+======================================================================+")
    print("| No. | Nama Jamu                          | Jumlah | Subtotal       |")
    print("+======================================================================+")
    total_belanja = 0
    for i, item in enumerate(keranjang): #Menampilkan item di keranjang dengan nomor urut
        nama, _, jml, sub = item
        sub_rp = f"Rp {sub:,.0f}".replace(',', '.')
        print(f"| {i+1:<4}| {nama:<35}| {jml:<7}| {sub_rp:>15}|")
        total_belanja += sub #utk menghitung total belanja
    
    print("+======================================================================+")
    total_rp = f"Rp {total_belanja:,.0f}".replace(',', '.')
    print(f"| TOTAL BELANJA                                  | {total_rp:>15}|")
    print("+======================================================================+")

def hapus_item_dari_keranjang(keranjang):
    """Menghapus item dari keranjang belanja berdasarkan nomor urut."""
    lihat_keranjang(keranjang)
    if not keranjang:
        return keranjang
    
    try:
        nomor_hapus = int(input("Masukkan nomor item di keranjang yang ingin dihapus: "))
        if 1 <= nomor_hapus <= len(keranjang):
            item_dihapus = keranjang.pop(nomor_hapus - 1)
            print(f">> Item '{item_dihapus[0]}' berhasil dihapus dari keranjang.")
        else:
            print("Nomor item tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    
    return keranjang

def proses_pembayaran_dan_selesaikan_transaksi(keranjang): #fungsinya utk menyelesaikan transaksi & hitung kembalian.
    """Memproses pembayaran, menghitung kembalian, dan membuat catatan transaksi."""
    global id_transaksi_counter
    if not keranjang:
        print("Keranjang kosong, tidak ada yang bisa diproses.")
        return None

    total_belanja = sum(item[3] for item in keranjang)
    total_rp = f"Rp {total_belanja:,.0f}".replace(',', '.')
    print(f"Total belanja Anda adalah: {total_rp}") #menghitung Total Belanja dari semua subtotal

    while True: #Loop untuk memastikan uang bayar cukup.
        try:
            uang_bayar = int(input("Masukkan jumlah uang pembayaran: Rp "))
            if uang_bayar < total_belanja:
                print("Uang pembayaran kurang. Silakan coba lagi.")
            else:
                break
        except ValueError:
            print("Input pembayaran tidak valid.")
    
    kembalian = uang_bayar - total_belanja
    kembalian_rp = f"Rp {kembalian:,.0f}".replace(',', '.')
    print(f"Kembalian Anda: {kembalian_rp}")
    
    # Struktur data transaksi yang akan disimpan ke riwayat
    # [id, waktu, list_item, total, bayar, kembali]
    transaksi_selesai = [
        id_transaksi_counter,
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        keranjang,
        total_belanja,
        uang_bayar,
        kembalian
    ]
    id_transaksi_counter += 1
    print(">> Transaksi Selesai dan Disimpan. <<")
    return transaksi_selesai

# ================================================================= #
# FUNGSI-FUNGSI UTAMA (CRUD) UNTUK MENGELOLA RIWAYAT TRANSAKSI
# ================================================================= #

def create(data_riwayat, transaksi_baru):
    """CREATE: Menambahkan transaksi yang sudah selesai ke dalam riwayat."""
    if transaksi_baru:
        data_riwayat.append(transaksi_baru)
    return data_riwayat

def read(data_riwayat):
    """READ: Menampilkan semua riwayat transaksi yang pernah disimpan."""
    if not data_riwayat:
        print("Belum ada riwayat transaksi.")
        return

    print("+================================================================================+")
    print("|                               RIWAYAT TRANSAKSI                                |")
    print("+================================================================================+")
    print("| ID  | Waktu Transaksi     | Total Belanja      | Dibayar            | Kembalian          |")
    print("+================================================================================+")
    
    for trx in data_riwayat:
        id_trx, waktu, _, total, bayar, kembali = trx
        total_rp = f"Rp {total:,.0f}".replace(',', '.')
        bayar_rp = f"Rp {bayar:,.0f}".replace(',', '.')
        kembali_rp = f"Rp {kembali:,.0f}".replace(',', '.')
        print(f"| {id_trx:<4}| {waktu:<20}| {total_rp:>19}| {bayar_rp:>19}| {kembali_rp:>19}|")
    
    print("+================================================================================+")
    
    try:
        lihat_detail = input("Lihat detail item transaksi? (y/n) atau masukkan ID: ").lower()
        if lihat_detail == 'y':
            id_detail = int(input("Masukkan ID Transaksi untuk melihat detail: "))
            tampilkan_detail_transaksi(data_riwayat, id_detail)
        elif lihat_detail.isdigit():
            tampilkan_detail_transaksi(data_riwayat, int(lihat_detail))
    except (ValueError, TypeError):
        # Abaikan jika input tidak valid
        pass

def update(data_riwayat):
    """UPDATE: Mengubah master data menu jamu (nama dan harga)."""
    print("--- Edit Master Data Menu Jamu ---")
    tampilkan_menu_jamu()
    
    try:
        nomor_edit = int(input("Masukkan nomor menu yang ingin diubah: "))
        if not (1 <= nomor_edit <= len(menu_jamu)):
            print("Nomor menu tidak valid.")
            return data_riwayat
        
        index_edit = nomor_edit - 1
        item_lama = menu_jamu[index_edit]
        print(f"Anda akan mengubah: {item_lama['nama']} (Rp {item_lama['harga']})")

        nama_baru = input("Masukkan nama jamu baru (kosongkan jika tidak ingin diubah): ")
        harga_baru_str = input("Masukkan harga baru (kosongkan jika tidak ingin diubah): ")

        if nama_baru.strip():
            menu_jamu[index_edit]['nama'] = nama_baru.strip()
        
        if harga_baru_str.strip():
            harga_baru = int(harga_baru_str)
            if harga_baru < 0:
                print("Harga tidak boleh negatif.")
                return data_riwayat
            menu_jamu[index_edit]['harga'] = harga_baru

        print(">> Data menu berhasil diperbarui.")
        tampilkan_menu_jamu()

    except ValueError:
        print("Input harus berupa angka yang valid.")
    
    return data_riwayat

def delete(data_riwayat):
    """DELETE: Menghapus sebuah transaksi dari riwayat berdasarkan ID."""
    read(data_riwayat)
    if not data_riwayat:
        return data_riwayat

    try:
        id_delete = int(input("Masukkan ID Transaksi yang ingin dihapus dari riwayat: "))
    except ValueError:
        print("ID harus berupa angka.")
        return data_riwayat

    ditemukan = False
    for i, trx in enumerate(data_riwayat):
        if trx[0] == id_delete:
            data_riwayat.pop(i)
            print(f">> Riwayat transaksi dengan ID {id_delete} berhasil dihapus.")
            ditemukan = True
            break
    
    if not ditemukan:
        print(f"Riwayat transaksi dengan ID {id_delete} tidak ditemukan.")
    return data_riwayat

# ================================================================= #
# FUNGSI-FUNGSI TAMBAHAN (SEARCH, SORT, DETAIL)
# ================================================================= #

def tampilkan_detail_transaksi(data_riwayat, id_detail):
    """Menampilkan rincian item dari sebuah transaksi di riwayat."""
    ditemukan = False
    for trx in data_riwayat:
        if trx[0] == id_detail: #mencari transaksi berdasarkan ID.
            _, waktu, items, total, _, _ = trx
            print(f"--- Detail Transaksi ID: {id_detail} ({waktu}) ---")
            lihat_keranjang(items) # Gunakan fungsi lihat_keranjang untuk format
            ditemukan = True
            break
    if not ditemukan:
        print(f"Transaksi dengan ID {id_detail} tidak ditemukan.")

def search_riwayat(data_riwayat):
    """SEARCHING: Mencari transaksi di riwayat berdasarkan ID."""
    if not data_riwayat:
        print("Belum ada riwayat untuk dicari.")
        return
    try:
        id_cari = int(input("Masukkan ID transaksi yang dicari: "))
        tampilkan_detail_transaksi(data_riwayat, id_cari)
    except ValueError:
        print("Input ID harus angka.")

def sort_riwayat(data_riwayat):
    """SORTING: Mengurutkan riwayat transaksi berdasarkan total belanja."""
    if not data_riwayat:
        print("Belum ada riwayat untuk diurutkan.")
        return

    # Bubble Sort berdasarkan total belanja (elemen ke-3)
    data_sorted = data_riwayat.copy( )#membuat salinan data
    n = len(data_sorted)
    for i in range(n):
        for j in range(0, n-i-1):
            if data_sorted[j][3] > data_sorted[j+1][3]: # bandingkan total belanja
                data_sorted[j], data_sorted[j+1] = data_sorted[j+1], data_sorted[j] #tukar posisi
    
    print("Riwayat transaksi diurutkan dari total belanja terkecil ke terbesar:")
    read(data_sorted)

# ================================================================= #
# MENU DAN PROGRAM UTAMA
# ================================================================= #

def menu_transaksi(): # fungsinya utk mengatur alur transaksi per pelanggan
    """Menu khusus untuk pembeli yang sedang bertransaksi."""
    keranjang_pembeli = []
    while True:
        print("--- Menu Transaksi Pelanggan ---")
        lihat_keranjang(keranjang_pembeli)
        print("1. Tambah Item")
        print("2. Hapus Item dari Keranjang")
        print("3. Selesaikan & Bayar")
        print("4. Batalkan Transaksi")
        print("------------------------------")
        pilihan = input("Pilih aksi [1-4]: ")

        if pilihan == '1':
            keranjang_pembeli = tambah_item_ke_keranjang(keranjang_pembeli)
        elif pilihan == '2':
            keranjang_pembeli = hapus_item_dari_keranjang(keranjang_pembeli)
        elif pilihan == '3':
            transaksi_selesai = proses_pembayaran_dan_selesaikan_transaksi(keranjang_pembeli)
            if transaksi_selesai:
                return transaksi_selesai # Kembalikan data transaksi untuk disimpan
        elif pilihan == '4':
            print("Transaksi dibatalkan.")
            return None # Kembali ke menu utama tanpa menyimpan apapun
        else:
            print("Pilihan tidak valid.")

def menuUtama(): #fungsinya utk menampilkan menu utama aplikasi
    """Menu utama aplikasi kasir."""
    print("===================================")
    print("===   SISTEM KASIR TOKO JAMU    ===")
    print("===================================")
    print("1. Buat Transaksi Baru")
    print("2. Lihat Riwayat Transaksi")
    print("3. Update Master Data Menu")
    print("4. Hapus Riwayat Transaksi")
    print("5. Cari Riwayat Transaksi")
    print("6. Urutkan Riwayat Transaksi")
    print("7. Keluar")
    print("===================================")
    try:
        pilihan = int(input("Masukkan pilihan [1-7]: "))
        return pilihan
    except ValueError:
        return 0

##### PROGRAM UTAMA #####
riwayat_semua_transaksi = [] 
pilihan_utama = 0

while (pilihan_utama != 7):
    pilihan_utama = menuUtama()
    if pilihan_utama == 1:
        # Masuk ke alur transaksi baru per pelanggan
        transaksi_baru = menu_transaksi()
        # 'create' di sini berarti menyimpan transaksi yg sudah jadi ke dalam riwayat
        riwayat_semua_transaksi = create(riwayat_semua_transaksi, transaksi_baru)
        input("Tekan ENTER untuk kembali ke menu utama...")
    elif pilihan_utama == 2:
        read(riwayat_semua_transaksi)
        input("Tekan ENTER untuk kembali ke menu utama...")
    elif pilihan_utama == 3:
        update(riwayat_semua_transaksi)
        input("Tekan ENTER untuk kembali ke menu utama...")
    elif pilihan_utama == 4:
        riwayat_semua_transaksi = delete(riwayat_semua_transaksi)
        input("Tekan ENTER untuk kembali ke menu utama...")
    elif pilihan_utama == 5:
        search_riwayat(riwayat_semua_transaksi)
        input("Tekan ENTER untuk kembali ke menu utama...")
    elif pilihan_utama == 6:
        sort_riwayat(riwayat_semua_transaksi)
        input("Tekan ENTER untuk kembali ke menu utama...")
    elif pilihan_utama == 7:
        print("Terima kasih!")
    else:
        if pilihan_utama != 0:
            print("Pilihan tidak valid.")
            input("Tekan ENTER untuk kembali ke menu utama...")
