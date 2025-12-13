daftar_tugas = []
#untuk menambahkan tugas baru
def create_tugas():
    print("\n--- Tambah Tugas Baru ---")
    judul = input("Masukkan judul tugas: ")
    
    
    deadline = input("Masukkan deadline (Tekan Enter jika tidak ada): ")
    if deadline == "":
        deadline = "-"

    kategori = input("Masukkan kategori (Tekan Enter jika umum): ")
    if kategori == "":
        kategori = "-"

    while True:
        try:
            prioritas = int(input("Masukkan tingkat prioritas (1-10, 1 tertinggi): "))
            break
        except ValueError:
            print("Error Harap masukkan angka untuk prioritas!")

    status = "Belum Selesai"
    
    # [Judul, Prioritas, Status, Deadline, Kategori]
    tugas_baru = [judul, prioritas, status, deadline, kategori]
    daftar_tugas.append(tugas_baru)
    print("Berhasil menambahkan tugas!")
#untuk menampilkan daftar tugas
def read_tugas(data_list=None, is_pause=True):
    if data_list is None:
        data_list = daftar_tugas
    #menampilkan daftar tugas
    print("\n--- Daftar Tugas ---")
    kepala = f"{'No':<4} | {'Deadline':<12} | {'Kategori':<12} | {'Prioritas':<10} | {'Status':<15} | {'Judul'}"
    print(kepala)

    
    if len(data_list) == 0:
        print("Tidak ada data tugas.")
    else:
        for i in range(len(data_list)):
            tugas = data_list[i]
            print(f"{i+1:<4} | {tugas[3]:<12} | {tugas[4]:<12} | {tugas[1]:<10} | {tugas[2]:<15} | {tugas[0]}")
    
    if is_pause: 
        input("\nTekan Enter untuk kembali...")
#sub menu edit tugas
def edit_tugas():
    print("\n--- Menu Edit Tugas ---")
    print("1. Tandai Tugas Selesai")
    print("2. Hapus Tugas")
    print("3. Kembali ke Menu Utama")
    
    pilihan = input("Pilih sub-menu (1-3): ")

    if pilihan == '1':

        read_tugas(daftar_tugas, is_pause=False)
        if len(daftar_tugas) == 0: 
            input("Tekan Enter untuk kembali...")
            return

        print("\n--- Tandai Selesai ---")
        try:
            nomor = int(input("Masukkan nomor tugas yang sudah selesai: "))
            index = nomor - 1
            if 0 <= index < len(daftar_tugas):
                daftar_tugas[index][2] = "Selesai"
                print(f"Status tugas '{daftar_tugas[index][0]}' berubah menjadi Selesai.")
            else:
                print("Nomor tugas tidak ditemukan.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")
        input("Tekan Enter untuk kembali...")

    elif pilihan == '2':
        read_tugas(daftar_tugas, is_pause=False)
        if len(daftar_tugas) == 0: 
            input("Tekan Enter untuk kembali...")
            return

        print("\n--- Hapus Tugas ---")
        try:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            index = nomor - 1
            if 0 <= index < len(daftar_tugas):
                terhapus = daftar_tugas.pop(index)
                print(f"Tugas '{terhapus[0]}' berhasil dihapus.")
            else:
                print("Nomor tugas tidak ditemukan.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")
        input("Tekan Enter untuk kembali...")

    elif pilihan == '3':
        return
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter...")

#sorting tugas bubble sorting
def sorting_tugas():
    n = len(daftar_tugas)
    sorted_list = daftar_tugas.copy()

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j][1] > sorted_list[j + 1][1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    print("\n[Sorting dari terendah ke tertinggi]")
    read_tugas(sorted_list) 

#untuk tampilan menu
def tampilkan_menu():
    while True:
        print("\n=== TO-DO LIST ===")
        print("\n===By Muhammad Aurel Hayfa Putra Wahyudi===")
        print("1. Tambah Tugas ")
        print("2. Lihat Semua Tugas ")
        print("3. Edit Tugas")
        print("4. Urutkan Sesuai Prioritas ")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            create_tugas()
        elif pilihan == '2':
            read_tugas()
        elif pilihan == '3':
            edit_tugas()
        elif pilihan == '4':
            sorting_tugas()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            input("Pilihan tidak valid. Tekan Enter...")

if __name__ == "__main__":
    tampilkan_menu()