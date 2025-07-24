import datetime
import csv
import os

# Tentukan path ke penyimpanan eksternal
PENYIMPANAN_EKSTERNAL = "/sdcard/aplikasi/tabungan"  # Atau coba "/storage/emulated/0/" jika /sdcard tidak berfungsi
NAMA_FILE = os.path.join(PENYIMPANAN_EKSTERNAL, "riwayat_tabungan.csv")

def format_uang(jumlah):
    """Memformat angka menjadi string dengan pemisah ribuan."""
    return "{:,.0f}".format(jumlah).replace(",", "_TEMP_").replace(".", ",").replace("_TEMP_", ".")

def parse_uang(jumlah_str):
    """Mengubah string berformat uang kembali menjadi float."""
    return float(jumlah_str.replace(".", ""))

def format_tanggal(tanggal_str):
    """Memformat string tanggal YYYY-MM-DD menjadi DD-MM-YYYY."""
    if tanggal_str:
        tahun, bulan, hari = tanggal_str.split('-')
        return f"{hari}-{bulan}-{tahun}"
    return ""

def catat_transaksi(riwayat_tabungan, jenis, jumlah):
    """Mencatat transaksi tabungan baru dan menyimpannya ke file."""
    tanggal = datetime.date.today()
    jumlah_format = format_uang(jumlah)
    riwayat_tabungan.append({"tanggal": tanggal, "jenis": jenis, "jumlah": jumlah_format})
    simpan_riwayat(riwayat_tabungan)
    print(f"Transaksi {jenis} sebesar Rp. {jumlah_format} berhasil dicatat pada tanggal {format_tanggal(str(tanggal))}.")

def lihat_saldo(riwayat_tabungan):
    """Menghitung dan menampilkan saldo tabungan beserta riwayat transaksi."""
    saldo = 0

    print("\n--- Riwayat Transaksi ---")
    if not riwayat_tabungan:
        print("Belum ada transaksi.")
    else:
        print("{:<12} {:<10} {:<15}".format("Tanggal", "Jenis", "Jumlah"))
        print("-" * 37)
        for transaksi in riwayat_tabungan:
            tanggal_str = transaksi["tanggal"]
            jenis = transaksi["jenis"]
            jumlah_str = transaksi["jumlah"]
            jumlah = parse_uang(jumlah_str)
            print("{:<12} {:<10} Rp. {:<15}".format(format_tanggal(tanggal_str), jenis, jumlah_str))
            if jenis == "setor":
                saldo += jumlah
            elif jenis == "tarik":
                saldo -= jumlah

    print("\n--- Saldo Tabungan ---")
    print(f"Saldo Tabungan Saat Ini: Rp. {format_uang(saldo)}")

def simpan_riwayat(riwayat_tabungan):
    """Menyimpan riwayat tabungan ke file CSV."""
    try:
        with open(NAMA_FILE, 'w', newline='') as csvfile:
            fieldnames = ['tanggal', 'jenis', 'jumlah']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for transaksi in riwayat_tabungan:
                writer.writerow(transaksi)
        print(f"Riwayat tabungan berhasil disimpan ke: {NAMA_FILE}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan riwayat: {e}")
        print("Pastikan Termux memiliki izin untuk menulis ke penyimpanan eksternal.")

def muat_riwayat():
    """Memuat riwayat tabungan dari file CSV."""
    riwayat_tabungan = []
    if os.path.exists(NAMA_FILE):
        try:
            with open(NAMA_FILE, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    riwayat_tabungan.append(row)
            print(f"Riwayat tabungan berhasil dimuat dari: {NAMA_FILE}")
        except Exception as e:
            print(f"Terjadi kesalahan saat memuat riwayat: {e}")
            print("Pastikan file riwayat tabungan ada dan dapat diakses.")
    else:
        print(f"File riwayat tabungan tidak ditemukan di: {NAMA_FILE}. Membuat file baru.")
    return riwayat_tabungan

def main():
    """Fungsi utama aplikasi."""
    riwayat_tabungan = muat_riwayat()

    while True:
        print("\n--- Aplikasi Catatan Tabungan ---")
        print("1. Setor Tabungan")
        print("2. Tarik Tabungan")
        print("3. Lihat Saldo")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            try:
                jumlah_input = float(input("Masukkan jumlah setoran: "))
                catat_transaksi(riwayat_tabungan, "setor", jumlah_input)
            except ValueError:
                print("Jumlah yang Anda masukkan tidak valid.")
        elif pilihan == "2":
            try:
                jumlah_input = float(input("Masukkan jumlah penarikan: "))
                catat_transaksi(riwayat_tabungan, "tarik", jumlah_input)
            except ValueError:
                print("Jumlah yang Anda masukkan tidak valid.")
        elif pilihan == "3":
            lihat_saldo(riwayat_tabungan)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
