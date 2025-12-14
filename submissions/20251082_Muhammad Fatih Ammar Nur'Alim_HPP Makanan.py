def hitung_harga_jual(total_modal):
    kompetitif = int(total_modal * 1.10)  # +10%
    normal = int(total_modal * 1.30)       # +30%
    ideal = int(total_modal * 1.70)        # +70%
    return kompetitif, normal, ideal


def create(data):
    print("\n=== Tambah Menu Makanan ===")
    nama = input("Nama makanan: ")

    # Input bahan utama (dengan harga)
    bahan_utama = []
    while True:
        print("\nTambahkan bahan utama (yang memiliki harga modal)")
        n = input("Nama bahan (kosongkan untuk selesai): ")
        if n == "":
            break
        try:
            qty = float(input("Jumlah (qty): "))
            harga = int(input("Harga satuan: "))
        except:
            print("Input tidak valid. Coba lagi.")
            continue

        bahan_utama.append({
            "nama": n,
            "qty": qty,
            "harga_satuan": harga
        })

    # Input bumbu (tanpa harga)
    bumbu = []
    print("\nTambahkan bumbu (tanpa harga)")
    while True:
        b = input("Bumbu (kosongkan untuk selesai): ")
        if b == "":
            break
        bumbu.append(b)

    # Hitung total modal
    total_modal = sum(b["qty"] * b["harga_satuan"] for b in bahan_utama)

    harga_kompetitif, harga_normal, harga_ideal = hitung_harga_jual(total_modal)

    menu = {
        "nama_makanan": nama,
        "bahan_utama": bahan_utama,
        "bumbu": bumbu,
        "total_modal": total_modal,
        "harga_kompetitif": harga_kompetitif,
        "harga_normal": harga_normal,
        "harga_ideal": harga_ideal
    }

    data.append(menu)
    print("\nMenu berhasil ditambahkan!\n")
    return data



def read(data):
    print("\n=== Lihat Menu Makanan ===")
    if len(data) == 0:
        print("Belum ada data!")
        return
    
    print("1. Tampilkan semua (sorted A-Z)")
    print("2. Cari makanan berdasarkan nama")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        sorted_data = sorted(data, key=lambda x: x["nama_makanan"])
        for i, d in enumerate(sorted_data):
            print(f"\n[{i+1}] {d['nama_makanan']}")
            print("  Total Modal:", d["total_modal"])
            print("  Harga Kompetitif:", d["harga_kompetitif"])
            print("  Harga Normal:", d["harga_normal"])
            print("  Harga Ideal:", d["harga_ideal"])
        return

    elif pilihan == "2":
        key = input("Masukkan nama makanan: ").lower()
        for d in data:
            if d["nama_makanan"].lower() == key:
                print("\nDitemukan!")
                print("Nama:", d["nama_makanan"])
                print("Bahan Utama:")
                for b in d["bahan_utama"]:
                    print(f"  - {b['nama']} ({b['qty']} x {b['harga_satuan']})")
                print("Bumbu:")
                for b in d["bumbu"]:
                    print(f"  - {b}")
                print("Total Modal:", d["total_modal"])
                print("Harga Kompetitif:", d["harga_kompetitif"])
                print("Harga Normal:", d["harga_normal"])
                print("Harga Ideal:", d["harga_ideal"])
                return
            
        print("Data tidak ditemukan.")
    else:
        print("Pilihan tidak valid!")



def update(data):
    print("\n=== Edit Menu ===")
    nama = input("Masukkan nama makanan yang ingin diedit: ").lower()

    for d in data:
        if d["nama_makanan"].lower() == nama:
            print("\nDitemukan:", d["nama_makanan"])

            # Edit nama makanan
            new_name = input("Nama baru (ENTER jika tidak diganti): ")
            if new_name != "":
                d["nama_makanan"] = new_name

            # ================== LOOP EDIT BAHAN UTAMA ==================
            while True:
                print("\n--- Bahan Utama (dengan harga) ---")
                for i, b in enumerate(d["bahan_utama"]):
                    print(f"{i+1}. {b['nama']} ({b['qty']} x {b['harga_satuan']})")

                print("\nPilihan edit bahan utama:")
                print("1. Hapus bahan")
                print("2. Tambah bahan baru")
                print("3. Selesai edit bahan utama")
                pilih_bahan = input("Pilih: ")

                if pilih_bahan == "1":
                    try:
                        hapus = int(input("Nomor bahan yang ingin dihapus: ")) - 1
                        if 0 <= hapus < len(d["bahan_utama"]):
                            d["bahan_utama"].pop(hapus)
                            print("Bahan berhasil dihapus!")
                        else:
                            print("Nomor tidak valid.")
                    except:
                        print("Input tidak valid.")

                elif pilih_bahan == "2":
                    print("\nTambahkan bahan baru:")
                    while True:
                        n = input("Nama bahan (ENTER untuk selesai): ")
                        if n == "":
                            break
                        try:
                            qty = float(input("Qty: "))
                            harga = int(input("Harga satuan: "))
                        except:
                            print("Input tidak valid.")
                            continue
                        d["bahan_utama"].append({
                            "nama": n,
                            "qty": qty,
                            "harga_satuan": harga
                        })
                        print("Bahan ditambahkan!")

                elif pilih_bahan == "3":
                    break

                else:
                    print("Pilihan tidak valid.")

            # ================== LOOP EDIT BUMBU ==================
            while True:
                print("\n--- Bumbu (tanpa harga) ---")
                for i, b in enumerate(d["bumbu"]):
                    print(f"{i+1}. {b}")

                print("\nPilihan edit bumbu:")
                print("1. Hapus bumbu")
                print("2. Tambah bumbu baru")
                print("3. Selesai edit bumbu")
                pilih_bumbu = input("Pilih: ")

                if pilih_bumbu == "1":
                    try:
                        hapus_b = int(input("Nomor bumbu yang ingin dihapus: ")) - 1
                        if 0 <= hapus_b < len(d["bumbu"]):
                            d["bumbu"].pop(hapus_b)
                            print("Bumbu berhasil dihapus!")
                        else:
                            print("Nomor tidak valid.")
                    except:
                        print("Input tidak valid.")

                elif pilih_bumbu == "2":
                    while True:
                        b = input("Masukkan bumbu (ENTER untuk selesai): ")
                        if b == "":
                            break
                        d["bumbu"].append(b)
                        print("Bumbu ditambahkan!")

                elif pilih_bumbu == "3":
                    break

                else:
                    print("Pilihan tidak valid.")

            # ================== HITUNG ULANG HARGA ==================
            total = sum(x["qty"] * x["harga_satuan"] for x in d["bahan_utama"])
            d["total_modal"] = total
            d["harga_kompetitif"], d["harga_normal"], d["harga_ideal"] = hitung_harga_jual(total)

            print("\nData berhasil diupdate!\n")
            return data

    print("Data tidak ditemukan.")
    return data




def delete(data):
    print("\n=== Hapus Menu ===")
    nama = input("Masukkan nama makanan: ").lower()

    for d in data:
        if d["nama_makanan"].lower() == nama:
            data.remove(d)
            print("Data berhasil dihapus.")
            return data

    print("Data tidak ditemukan.")
    return data



def menuUtama():
    print("===================================")
    print("===   Aplikasi Resep Makanan     ===")
    print("===      Hitung Harga Jual       ===")
    print("===================================")
    print("1. Tambah Menu")
    print("2. Lihat Menu")
    print("3. Edit Menu")
    print("4. Hapus Menu")
    print("5. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya 1-5.")
            input()
        else:
            return pilihan
    except:
        print("Input harus angka.")



##### PROGRAM UTAMA #####
pilihan = 0
data = []

while pilihan != 5:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
        input("\nTekan ENTER untuk kembali...")
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)

print("Terima kasih!")
