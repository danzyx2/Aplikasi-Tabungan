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

Anda bisa mengubah lokasi penyimpanan ini di baris kode berikut pada `main.py` jika diperlukan:

```python
PENYIMPANAN_EKSTERNAL = "/sdcard/aplikasi/tabungan" # Ubah path ini!
