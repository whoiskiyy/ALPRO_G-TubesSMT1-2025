import datetime
import pandas as pd
from pathlib import Path

Deptops = [
    "Daily Officer", "External Relationship",
    "Entrepreneur Development", "Public Relation & Design (PRD)",
    "Academic and Project (AnP)", "Human Resource Development (HRD)"
]
Layops = ["Desain", "Video"]
PJ_PASS = "PRD2025"
BASE = Path(__file__).parent
DATA_DIR = BASE / "hasil"
DATA_DIR.mkdir(exist_ok=True)
file_path = DATA_DIR / "requests.xlsx"

def input_with_rule(prompt, rule="", error="Input tidak valid."):
    while True:
        val = input(prompt).strip()
        if rule == "digit" and not val.isdigit():
            print(error)
        elif rule == "phone" and not (val.isdigit() and 8 <= len(val) <= 15):
            print(error)
        elif rule == "url" and not (val.startswith("http://") or val.startswith("https://")):
            print(error)
        elif rule == "text" and len(val) < 3:
            print(error)
        else:
            return val

def pick_option(title, options):
    print(f"\n=== PILIHAN {title.upper()} ===")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    while True:
        pilihan = input_with_rule("Pilih nomor: ", "digit")
        pilihan = int(pilihan)
        if 1 <= pilihan <= len(options):
            return options[pilihan - 1]
        print("Nomor tidak valid, coba lagi.")

def valid_date():
    while True:
        try:
            d = input("Deadline (dd/mm/yyyy): ").strip()
            v = datetime.datetime.strptime(d, "%d/%m/%Y").date()
            if datetime.date.today() <= v <= datetime.date(2100, 1, 1):
                return d
            print("Tanggal tidak valid atau sudah lewat.")
        except:
            print("Format salah (contoh: 14/02/2025)")

def create(df):
    df.loc[len(df)] = {
        "Departemen": pick_option("Departemen", Deptops),
        "Layanan": pick_option("Layanan", Layops),
        "Nama Kegiatan": input_with_rule("Nama kegiatan: ", "text"),
        "Deskripsi Konten (Link GDocs)": input_with_rule("Deskripsi Konten (Link GDocs): ", "url"),
        "Deadline": valid_date(),
        "Nomor Telepon": input_with_rule("Nomor Telepon: ", "phone"),
        "Penanggung Jawab": "",
        "Status": ""
    }
    print("\nRequest berhasil ditambahkan.")

def read(df):
    if df.empty:
        return print("\nTidak ada Request")
    for i, r in df.reset_index(drop=True).iterrows():
        print(f"\n[{i + 1}] {r['Departemen']} - {r['Layanan']}")
        for k, v in r.items():
            print(f"  {k:25}: {v if v else '-'}")

def update(df):
    read(df)
    idx = int(input_with_rule("\nPilih yang ingin diupdate (nomor data): ", "digit")) - 1
    cols = list(df.columns)
    print("\n=== PILIH KOLOM ===")
    for i in range(len(cols)):
        print(f"{i+1}. {cols[i]}")
    col_idx = int(input_with_rule("\nKolom update: ", "digit")) - 1
    col = cols[col_idx]
    if col == "Departemen":
        df.at[idx, col] = pick_option("Departemen", Deptops)
    elif col == "Layanan":
        df.at[idx, col] = pick_option("Layanan", Layops)
    elif col == "Deadline":
        df.at[idx, col] = valid_date()
    elif col in ["Status", "Penanggung Jawab"]:
        pwd = input("Masukkan password PJ: ")
        if pwd != PJ_PASS:
            return print("Password salah")
        df.at[idx, col] = input(f"{col} baru: ").strip()
    else:
        df.at[idx, col] = input(f"Update {col}: ").strip()
    print("\nRequest diperbarui.")

def delete(df):
    read(df)
    idx = int(input_with_rule("\n Pilih yang ingin dihapus (nomor data): ", "digit")) - 1
    df.drop(idx, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print("\nRequest dihapus")

def add_pj(df):
    if input("Password PJ: ") != PJ_PASS:
        return print("Akses ditolak")
    kosong = df[df["Penanggung Jawab"].fillna("").str.strip() == ""]
    if kosong.empty:
        return print("Semua request sudah punya PJ")
    kosong = kosong.reset_index()
    read(kosong.drop(columns=["index"]))
    idx = int(input_with_rule("\nPilih Request: ", "digit")) - 1
    df_idx = kosong.at[idx, "index"]
    df.at[df_idx, "Penanggung Jawab"] = input("Nama PJ: ").strip()
    df.at[df_idx, "Status"] = "Proses"
    print("\nPenanggung jawab ditambahkan")

def sort_data(df):
    if df.empty:
        return print("\nTidak ada Request")
    print("\n🔧 Sorting berdasarkan deadline...")
    df["d"] = pd.to_datetime(df["Deadline"], format="%d/%m/%Y")
    n = len(df)
    for i in range(n):
        for j in range(n - i - 1):
            if df.at[j, "d"] > df.at[j + 1, "d"]:
                df.iloc[[j, j+1]] = df.iloc[[j+1, j]].values
    df.drop(columns="d", inplace=True)
    df.reset_index(drop=True, inplace=True)
    print("Selesai")

def search(df):
    q = input("Nama kegiatan: ").lower()
    data = df.sort_values("Nama Kegiatan").to_dict("records")
    l, r = 0, len(data) - 1
    while l <= r:
        m = (l + r) // 2
        name = data[m]["Nama Kegiatan"].lower()
        if name == q:
            print("\n Data ditemukan:\n")
            for d in data:
                if d["Nama Kegiatan"].lower() == q:
                    for k, v in d.items():
                        print(f"{k:25}: {v if v else '-'}")
                    print("-" * 40)
            return
        l, r = (m + 1, r) if name < q else (l, m - 1)
    print("Tidak ditemukan")

def main():
    Path("hasil").mkdir(exist_ok=True)
    df = pd.read_excel(file_path) if file_path.exists() else pd.DataFrame(columns=[
        "Departemen","Layanan","Nama Kegiatan",
        "Deskripsi Konten (Link GDocs)","Deadline",
        "Nomor Telepon","Penanggung Jawab","Status"
    ])
    MENU = {
        "1": ("Tambah Request", create),
        "2": ("Lihat Request", read),
        "3": ("Update Request", update),
        "4": ("Hapus Request", delete),
        "5": ("Tambah Penanggung Jawab", add_pj),
        "6": ("Sort Request", sort_data),
        "7": ("Cari Request", search),
        "8": ("Keluar", None)
    }
    while True:
        print("\n=== Request Layanan Design/Video ===")
        for k, (t, _) in MENU.items():
            print(f"{k}. {t}")
        pilih = input("Pilih menu: ").strip()
        if pilih in MENU:
            if pilih == "8":
                print("\nSelamat Tinggal, Terimakasih")
                exit()
            MENU[pilih][1](df)
            df.to_excel(file_path, index=False)
        else:
            print("Pilihan tidak valid")

main()
