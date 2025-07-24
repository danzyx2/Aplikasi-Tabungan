# 📝 Aplikasi Catatan Tabungan (TabunganKu) 💰

Jurnal keuangan saku Anda yang sederhana namun kuat! Catat setiap setoran dan penarikan, pantau saldo Anda, dan pastikan setiap rupiah tercatat dengan rapi.

---

## 🔗 Tujuan Projek Ini

* **Pelacakan Keuangan Mudah**: Memberikan solusi sederhana untuk mencatat transaksi tabungan harian.
* **Data Aman & Lokal**: Menyimpan riwayat keuangan Anda secara persisten dalam format CSV yang mudah diakses.
* **Ramah Mobile (via Termux)**: Dioptimalkan untuk berjalan lancar di perangkat Android melalui Termux.
* **Ringan & Cepat**: Aplikasi berbasis konsol tanpa overhead GUI yang berat.

---

## 📦 Isi Kotak Proyek Ini

* **Inti Aplikasi**: Kode Python yang mengatur logika pencatatan, perhitungan saldo, dan tampilan riwayat.
* **Penyimpanan CSV**: Mekanisme untuk membaca dan menulis data transaksi ke file .csv.
* **Utilitas Tanggal & Uang**: Fungsi bantu untuk memformat dan mengurai data numerik serta tanggal.
* **Dokumentasi Jelas**: Panduan komprehensif untuk instalasi dan penggunaan.

---

## ✨ Fitur-Fitur Kerennya

* **Pencatatan Transaksi Cepat** 💸
    * Mudah untuk **"Setor Tabungan"** atau **"Tarik Tabungan"** hanya dengan memasukkan jumlah.
    * Setiap transaksi dicatat dengan **tanggal otomatis** (hari ini) dan disimpan.

* **Tampilan Saldo Real-time** 📈
    * Pilih opsi **"Lihat Saldo"** untuk mendapatkan ringkasan instan.
    * Menampilkan **saldo tabungan Anda saat ini** yang telah diformat dengan baik.

* **Riwayat Transaksi Lengkap** 📜
    * Bersamaan dengan saldo, Anda akan melihat **daftar semua transaksi sebelumnya**, lengkap dengan tanggal, jenis (setor/tarik), dan jumlah.

* **Penyimpanan Data Otomatis & Persisten** 💾
    * Semua data Anda disimpan secara otomatis di file **`riwayat_tabungan.csv`** di penyimpanan eksternal Anda (`/sdcard/aplikasi/tabungan/`).
    * Tidak perlu khawatir data hilang saat aplikasi ditutup! Saat Anda membuka kembali, semua riwayat akan dimuat secara otomatis.

* **Format Uang & Tanggal Indonesia** 🇮🇩
    * Jumlah uang diformat menggunakan pemisah ribuan titik (`.`) seperti **`1.000.000`**.
    * Tanggal ditampilkan dalam format **`DD-MM-YYYY`**.

---

## 🛠️ Apa Yang Kamu Butuhkan (Software)

* **Python 3.x**
* **Termux** (Sangat direkomendasikan jika Anda ingin menjalankannya di perangkat Android Anda).

---

## ⚙️ Konfigurasi Lokasi Penyimpanan

Secara default, aplikasi akan mencoba menyimpan file `riwayat_tabungan.csv` di jalur ini:
`/sdcard/aplikasi/tabungan/riwayat_tabungan.csv`

Anda bisa mengubah lokasi penyimpanan ini di baris kode berikut pada `tabungan.py` jika diperlukan:

```python
PENYIMPANAN_EKSTERNAL = "/sdcard/aplikasi/tabungan" # Ubah path ini!
```

---

## 🚀 Langkah-Langkah Awal (Mulai Pakai)

### 1. Dapatkan Kodenya

Jika Anda mendapatkan file `tabungan.py` ini secara terpisah, Anda bisa langsung lompat ke langkah 2.

### 2. Siapkan Lingkungan Anda

#### a. Untuk Pengguna Desktop (Linux/macOS/Windows)

1.  **Instal Python 3**: Jika belum ada, unduh dan instal Python 3 dari [python.org](https://www.python.org/downloads/).
2.  **Buka Terminal/Command Prompt**: Navigasikan ke folder tempat Anda menyimpan `tabungan.py`.

#### b. Untuk Pengguna Android (via Termux)

1.  **Unduh Termux**: Instal aplikasi [Termux](https://termux.com/) dari Google Play Store atau F-Droid.
2.  **Perbarui Paket**: Setelah membuka Termux, jalankan:
    ```bash
    pkg update && pkg upgrade
    ```
3.  **Instal Python**:
    ```bash
    pkg install python
    ```
4.  **Berikan Izin Penyimpanan**:
    ```bash
    termux-setup-storage
    ```
    Ikuti prompt untuk memberikan izin. Ini akan membuat folder `storage` di direktori Termux Anda, dan Anda dapat mengakses penyimpanan internal Anda melalui `~/storage/shared`.
5.  **Pindahkan File**: Pindahkan file `tabungan.py` ke folder yang mudah diakses di Termux (misalnya, `~/storage/shared/Download/`).
6.  **Navigasi ke Folder File**:
    ```bash
    cd storage/shared/Download/ # Sesuaikan dengan lokasi file Anda
    ```

### 3. Jalankan Aplikasinya!

Setelah persiapan selesai, jalankan aplikasi dengan perintah:

```bash
python tabungan.py
```


## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE). Bebas untuk digunakan, dimodifikasi, dan disebarluaskan untuk keperluan apa pun.

---

## 👋 Tertarik untuk Kolaborasi?

Kami sangat terbuka untuk kontribusi dan ide-ide baru! Jika Anda menemukan bug, memiliki saran fitur, atau ingin berkontribusi dalam bentuk kode, silakan:

* Buka **Issues** untuk melaporkan masalah atau mengusulkan ide.
* Buat **Pull Request** jika Anda sudah memiliki kode yang siap untuk digabungkan.

Mari bersama-sama ciptakan alat-alat yang lebih bermanfaat!

