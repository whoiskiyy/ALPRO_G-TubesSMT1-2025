data_transport = []

def tambah(data):
    print("\nTambah Catatan Transportasi")

    tanggal = input("Tanggal (dd/mm/yyyy): ")
    jenis = input("Jenis transportasi: ")
    rute = input("Rute atau tujuan: ")

    try:
        biaya = int(input("Biaya (Rp): "))
    except:
        print("\033[31m Biaya harus angka \033[0m\n")
        return data

    data.append([tanggal, jenis, rute, biaya])
    print("\033[32m Yeay catatan berhasil ditambahkan \033[0m\n")
    return data


def lihat(data):
    print("\nDaftar Catatan Transportasi")

    if len(data) == 0:
        print("\033[31m Belum ada catatan \033[0m\n")
        return

    nomor = 1
    for catatan in data:
        print(f"{nomor}. Tanggal : {catatan[0]}")
        print(f"   Jenis   : {catatan[1]}")
        print(f"   Rute    : {catatan[2]}")
        print(f"   Biaya   : Rp{catatan[3]}\n")
        nomor += 1


def edit(data):
    lihat(data)
    if len(data) == 0:
        return data

    try:
        pilih = int(input("Pilih nomor catatan: "))
    except:
        print("\033[31m Masukkan angka \033[0m\n")
        return data

    posisi = pilih - 1
    if posisi < 0 or posisi >= len(data):
        print("\033[31m Nomor tidak ditemukan \033[0m\n")
        return data

    print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")

    tanggal = input("Tanggal yang diperbarui: ")
    jenis = input("Jenis transportasi yang diperbarui: ")
    rute = input("Rute yang diperbarui: ")
    biaya = input("Biaya yang diperbarui: ")
    if tanggal != "":
        data[posisi][0] = tanggal
    if jenis != "":
        data[posisi][1] = jenis
    if rute != "":
        data[posisi][2] = rute
    if biaya != "":
        try:
            data[posisi][3] = int(biaya)
        except:
            print("\033[31mBiaya harus berupa angka\033[0m\n")

    print("\033[32mCatatan berhasil diperbarui\033[0m\n")
    return data


def hapus(data):
    lihat(data)
    if len(data) == 0:
        return data

    try:
        pilih = int(input("Nomor yang ingin dihapus: "))
    except:
        print("Masukkan angka.")
        return data

    posisi = pilih - 1
    if posisi < 0 or posisi >= len(data):
        print("\033[31mNomor tidak valid\033[0m\n")
        return data

    del data[posisi]
    print("\033[32mCatatan berhasil dihapus\033[0m\n")
    return data


def cari_catatan(data):
    print("\nPencarian Catatan Transportasi\n")
    lihat(data)

    kolom_dicari = input("Cari berdasarkan (tanggal/jenis/rute/biaya): ").lower()
    kata = input("Masukkan kata pencarian: ").lower()

    posisi_kolom = {
        "tanggal": 0,
        "jenis": 1,
        "rute": 2,
        "biaya": 3
    }

    if kolom_dicari not in posisi_kolom:
        print("\033[31mKolom tidak tersedia\033[0m\n")
        return data

    kolom = posisi_kolom[kolom_dicari]
    hasil = []

    for c in data:
        nilai = str(c[kolom]).lower()

        if kolom_dicari == "biaya":
            if nilai == kata:
                hasil.append(c)
        else:
            if kata in nilai:
                hasil.append(c)

    if len(hasil) == 0:
        print("\033[31mData tidak ditemukan\033[0m\n")
        return data

    print("\nHasil Pencarian:\n")
    nomor = 1
    for c in hasil:
        print(f"{nomor}. Tanggal : {c[0]}")
        print(f"   Jenis   : {c[1]}")
        print(f"   Rute    : {c[2]}")
        print(f"   Biaya   : Rp{c[3]}\n")
        nomor += 1

    return data


def bubble_sort_transport(data, key):
    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if key == "tanggal":
                d1, m1, y1 = data[j][0].split("/")
                d2, m2, y2 = data[j+1][0].split("/")

                y1 = int(y1)
                y2 = int(y2)
                m1 = int(m1)
                m2 = int(m2)
                d1 = int(d1)
                d2 = int(d2)

                if (y1 > y2) or (y1 == y2 and m1 > m2) or (y1 == y2 and m1 == m2 and d1 > d2):
                    data[j], data[j+1] = data[j+1], data[j]

            elif key == "jenis":
                if data[j][1].lower() > data[j+1][1].lower():
                    data[j], data[j+1] = data[j+1], data[j]

            elif key == "rute":
                if data[j][2].lower() > data[j+1][2].lower():
                    data[j], data[j+1] = data[j+1], data[j]

            elif key == "biaya":
                if data[j][3] > data[j+1][3]:
                    data[j], data[j+1] = data[j+1], data[j]

    print("\033[32mData berhasil diurutkan\033[0m\n")
    return data


def menu():
    print("\033[34m⋆｡°✩ Catatan Transportasi Harian ✩°｡⋆\033[0m")
    print("\033[34m--------------------------------------\033[0m")
    print("\033[35m 1.\033[37m Tambah Catatan")
    print("\033[35m 2. \033[37m Lihat Catatan")
    print("\033[35m 3. \033[37m Edit Catatan")
    print("\033[35m 4. \033[37m Hapus Catatan")
    print("\033[35m 5. \033[37m Cari Catatan")
    print("\033[35m 6. \033[37m Urutkan Data")
    print("\033[35m 7. \033[37m Keluar")
    print("\033[34m ｡☆✼★━━━━━━━━━━━━━━━━★✼☆｡ \033[0m")

    try:
        pilihan = int(input("Pilih menu: "))
    except:
        print("Input harus angka.")
        pilihan = 0
    return pilihan


while True:
    pilihan = menu()

    if pilihan == 1:
        data_transport = tambah(data_transport)
    elif pilihan == 2:
        lihat(data_transport)
    elif pilihan == 3:
        data_transport = edit(data_transport)
    elif pilihan == 4:
        data_transport = hapus(data_transport)
    elif pilihan == 5:
        data_transport = cari_catatan(data_transport)
    elif pilihan == 6:
        k = input("Urutkan berdasarkan (tanggal/jenis/rute/biaya): ").lower()
        data_transport = bubble_sort_transport(data_transport, k)
    elif pilihan == 7:
        print("\033[32mProgram selesai\033[0m")
        break
    else:
        print("\033[91mPilihan tidak tersedia\033[0m\n")
