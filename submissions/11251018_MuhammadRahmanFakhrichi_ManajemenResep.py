def create(data):
    print("\n======= Tambah Resep Baru =======")
    
    print("Pilih Kategori Resep:")
    print("1. Makanan Berat")
    print("2. Cemilan")
    print("3. Minuman")
    print("4. Lainnya")

    try:
        p_kategori = int(input("Pilihan [1-4]: "))
        if p_kategori == 1:
            kategori = "Makanan Berat"
        elif p_kategori == 2:
            kategori = "Cemilan"
        elif p_kategori == 3:
            kategori = "Minuman"
        else:
            kategori = "Lainnya"
    except ValueError:
        kategori = "Lainnya"
    
    nama = input("Masukkan Nama Resep: ")
    new_id = generate_id(data, kategori)

    bahan = []
    print("Masukkan alat dan bahan (ketik 'selesai' untuk berhenti):")
    while True:
        b = input("- ")
        if b.lower() == 'selesai':
            break
        bahan.append(b)
         
    langkah = []
    print("Masukkan langkah-langkah (ketik 'selesai' untuk berhenti):")
    idx_langkah = 1
    while True:
        l = input(str(idx_langkah) + ".) ")
        if l.lower() == 'selesai':
            break
        langkah.append(str(idx_langkah) + ". " + l)
        idx_langkah += 1
        
    resep_baru = [new_id, nama, kategori, bahan, langkah]
    data.append(resep_baru) 
    print(f"\nResep '{nama}' berhasil ditambahkan dengan ID {new_id}!")
    return data 

def read(data):
    if len(data) == 0:
        print("\nKoleksi resep masih kosong.")
        return

    print("\n======== Lihat Koleksi Resep =======")
    print("1. Tampilkan Semua Resep")
    print("2. Cari Resep")
    
    try:
        pilihan_read = int(input("Pilihan [1-2]: "))
    except ValueError:
        print("Input salah.")
        return

    if pilihan_read == 1:
        print("\nUrutkan berdasarkan:")
        print("1. ID")
        print("2. Nama (A-Z)")
        try:
            pilihan_sort = int(input("Pilihan [1-2]: "))
            n = len(data)
            for i in range(n):
                for j in range(0, n - i - 1):
                    tukar = False
                    if pilihan_sort == 1: #membandingkan dngn id
                        if data[j][0] > data[j+1][0]:
                            tukar = True
                    elif pilihan_sort == 2: #membandingkan dngn nama
                        if data[j][1] > data[j+1][1]:
                            tukar = True
                    if tukar == True:
                        temp = data[j]
                        data[j] = data[j+1]
                        data[j+1] = temp
            print("\n======= Daftar Resep =======")
            for resep in data:
                detail_resep(resep)     
        except ValueError:
            print("Input salah.")
            return  
        
    elif pilihan_read == 2:
        kata_kunci = input("Masukkan nama resep atau bahan: ").lower()
        hasil_pencarian = []
        
        for resep in data: 
            ditemukan = False
            if kata_kunci in resep[1].lower():#cek dngn nama
                ditemukan = True
            if ditemukan == False: #cek dngn bahan
                for bahan in resep[3]: 
                    if kata_kunci in bahan.lower():
                        ditemukan = True
                        break 
            if ditemukan == True:
                hasil_pencarian.append(resep)     
        if len(hasil_pencarian) == 0:
            print(f"\nResep dengan kata kunci '{kata_kunci}' tidak ditemukan.")
        else:
            print(f"\n======= Hasil Pencarian '{kata_kunci}' =======")
            for resep in hasil_pencarian:
                print(f"- {resep[0]}: {resep[1]}")

            print("============================")
            id_pilih = input("Masukkan ID resep untuk detail: ")
            
            index_hasil = cari_index_id(hasil_pencarian, id_pilih)
            if index_hasil != -1:
                resep_dipilih = hasil_pencarian[index_hasil]
                print("\n======= Detail Resep Pilihan =======")
                detail_resep(resep_dipilih)
            else:
                print(f"ID '{id_pilih}' tidak ada di daftar hasil.")
    else:
        print("Pilihan tidak valid.")
    print()

def update(data):
    if len(data) == 0:
        print("\nKoleksi resep masih kosong.")
        return data

    print("\n======= Update Resep =======")
    print("Daftar Resep:")
    for resep in data:
        print(f"- {resep[0]}: {resep[1]} ({resep[2]})") 
        
    update_byid = input("\nMasukkan ID resep yang ingin diperbarui: ")
    index = cari_index_id(data, update_byid)
    
    if index == -1:
        print(f"Resep dengan ID '{update_byid}' tidak ditemukan.")
        return data
    
    print(f"\nAnda akan memperbarui '{data[index][1]}'")
    print(f"ID Saat Ini: {data[index][0]}")
    print(f"Kategori Saat Ini: {data[index][2]}")
    
    print("\nApa yang ingin diperbarui?")
    print("1. Nama")
    print("2. Kategori (mengubah id)")
    print("3. Alat dan bahan (tulis ulang alat dan bahan)")   
    print("4. Langkah (tulis ulang seluruh langkah)") 
        
    try:
        pilihan_update = int(input("Pilihan [1-4]: ")) 
    except ValueError:
        print("Input salah.")
        return data
        
    if pilihan_update == 1:
        nama_baru = input("Masukkan Nama Resep baru: ")
        data[index][1] = nama_baru
        print("Nama resep berhasil diperbarui.")
        
    elif pilihan_update == 2:
        print("\nPilih Kategori Resep Baru:")
        print("1. Makanan Berat")
        print("2. Cemilan")
        print("3. Minuman")
        print("4. Lainnya")
        try:
            p_kategori = int(input("Pilihan [1-4]: "))
            if p_kategori == 1:
                kategori_baru = "Makanan Berat"
            elif p_kategori == 2:
                kategori_baru = "Cemilan"
            elif p_kategori == 3:
                kategori_baru = "Minuman"
            else:
                kategori_baru = "Lainnya"
        except ValueError:
            kategori_baru = "Lainnya"
            
        if kategori_baru == data[index][2]:
            print("Kategori sama, tidak ada perubahan.")
            return data
            
        id_baru = generate_id(data, kategori_baru)
        id_lama = data[index][0]
        
        data[index][2] = kategori_baru
        data[index][0] = id_baru
        
        print("\nKategori dan ID resep berhasil diperbarui.")
        print(f"ID Resep lama : {id_lama}")
        print(f"ID Resep BARU : {id_baru}")

    elif pilihan_update == 3:
        print("\n======= Masukkan Daftar Bahan Baru =======")
        print("(Ketik 'selesai' untuk berhenti)")
        bahan_baru = [] 
        while True:
            b = input("- ")
            if b.lower() == 'selesai':
                break
            bahan_baru.append(b)

        data[index][3] = bahan_baru 
        print("Daftar bahan berhasil diperbarui.")

    elif pilihan_update == 4:
        print("\n======= Masukkan Daftar Langkah Baru =======")
        print("(Ketik 'selesai' untuk berhenti)")
        langkah_baru = [] 
        idx_langkah = 1
        while True:
            l = input(str(idx_langkah) + ". ")
            if l.lower() == 'selesai':
                break
            langkah_baru.append(str(idx_langkah) + ". " + l)
            idx_langkah += 1
            
        data[index][4] = langkah_baru
        print("Daftar langkah berhasil diperbarui.")
    
    else:
        print("Pilihan tidak valid.")
        
    return data

def delete(data): 
    if len(data) == 0:
        print("\nKoleksi resep masih kosong.")
        return data
        
    print("\n======= Hapus Resep =======")
    print("Daftar Resep:")
    for resep in data:
        print(f"- {resep[0]}: {resep[1]}")
        
    id_hapus = input("\nMasukkan ID resep yang ingin dihapus: ")
    index = cari_index_id(data, id_hapus)
    
    if index == -1:
        print(f"Resep dengan ID '{id_hapus}' tidak ditemukan.")
        return data
        
    nama_resep = data[index][1]
    print(f"Anda yakin ingin menghapus '{nama_resep}'?")
    
    try:
        print("1. Ya")
        print("2. Tidak")
        pilihan_konfirmasi = int(input("Pilihan [1-2]: ")) 
    except ValueError:
        print("Input salah.")
        return data
        
    if pilihan_konfirmasi == 1: 
        data.pop(index) 
        print(f"Resep '{nama_resep}' berhasil dihapus.")
    elif pilihan_konfirmasi == 2:
        print("Penghapusan dibatalkan.")
    else:
        print("Pilihan tidak valid.")
        
    return data

def generate_id(data, kategori):
    prefix = "LAIN"
    if kategori == "Makanan Berat": 
        prefix = "MB"
    elif kategori == "Cemilan":
        prefix = "CM"
    elif kategori == "Minuman":
        prefix = "MN"
        
    last_num = 0
    
    for resep in data:
        id_sekarang = resep[0]

        prefix_sekarang = id_sekarang[0:2]
        
        if prefix_sekarang == prefix: 
            try:
                num_string = id_sekarang[3:] 
                num = int(num_string)
                if num > last_num:
                    last_num = num
            except:
                pass 
                
    new_num = last_num + 1
    
    str_num = str(new_num)
    if new_num < 10:
        str_num = "00" + str_num
    elif new_num < 100:
        str_num = "0" + str_num
        
    new_id_string = prefix + "-" + str_num
    return new_id_string



# menampilkan detail resep
def detail_resep(resep):
    print("=================================")
    print(f"ID       : {resep[0]}")
    print(f"Nama     : {resep[1]}")
    print(f"Kategori : {resep[2]}")
    
    print("\nBahan-bahan:")
    for b in resep[3]:
        print(f"- {b}")
        
    print("\nLangkah-langkah:")
    for l in resep[4]:
        print(l)
    print("=================================")

# Fungsi mencari index resep menurut ID
def cari_index_id(data, id_cari):
    for i in range(len(data)):
        if data[i][0].lower() == id_cari.lower():
            return i 
    return -1 

def menuUtama():
    print("==================================")
    print("=========== Buku Resep ===========")
    print("=========== by Mas Siji ==========")
    print("==================================")
    print("1. Tambah Resep")
    print("2. Lihat Resep")
    print("3. Edit Resep")
    print("4. Hapus Resep")
    print("5. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya antara 1 sampai 5. Silakan coba lagi.")
            input()
        else:
            return pilihan
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        return 0
    
##### PROGRAM UTAMA #####

pilihan = 0
data = [] 

# Contoh Data Awal
data.append([
    "MB-001",               
    "Nasi Goreng",          
    "Makanan Berat",        
    ["Nasi", "Telur"],      
    ["1.) Goreng", "2.) Sajikan"] 
])

while (pilihan != 5):
    pilihan = menuUtama()
    if (pilihan == 1):
        data = create(data) 
        input("Tekan ENTER..")
    elif (pilihan == 2):
        read(data) 
        input("Tekan ENTER..")
    elif (pilihan == 3):
        data = update(data) 
        input("Tekan ENTER..")
    elif (pilihan == 4):
        data = delete(data) 
        input("Tekan ENTER..")
        
print("Terima kasih!")