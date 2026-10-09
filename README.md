# Projek Python Ridhofaris

Kumpulan program Python — tugas dan latihan mata kuliah Pemrograman (Sistem Informasi).

## 1. `struk_belanja.py` — Program Struk Belanja Sederhana

Program kasir dasar: input barang, hitung total, diskon 5% untuk belanja >= Rp 100.000, hitung kembalian, cetak struk.

```bash
python struk_belanja.py
```

## 2. `kasir_lengkap.py` — Sistem Kasir Lengkap

Versi lanjutan dengan fitur:

- **Menu utama** 5 pilihan (tambah barang, lihat stok, transaksi, laporan, keluar)
- **Manajemen stok**: tambah barang (kode, nama, harga, stok), data tersimpan di `barang.json` sehingga tidak hilang saat program ditutup
- **Transaksi penjualan**: pilih barang per kode, cek stok otomatis (tidak bisa jual melebihi stok), stok berkurang otomatis setelah pembayaran
- **Penyimpanan transaksi**: semua penjualan tercatat di `transaksi.csv`
- **Laporan harian**: total omzet, jumlah item terjual, dan barang terlaris hari ini

```bash
python kasir_lengkap.py
```

## 3. `tebak_angka.py` — Game Tebak Angka

Game sederhana: komputer memilih angka acak 1–100, pemain menebaknya dalam 7 kesempatan dengan petunjuk "terlalu besar" / "terlalu kecil". Latihan if-else, while loop, dan modul random.

```bash
python tebak_angka.py
```

## 4. `cek_spek_pc.py` — Cek Spesifikasi PC

Menampilkan spesifikasi komputer sendiri: sistem operasi, nama komputer, prosesor, jumlah core, versi Python, total RAM, dan info disk. Memakai modul bawaan `platform` dan `os`; info RAM/disk butuh `psutil` (`pip install psutil`).

```bash
python cek_spek_pc.py
```

## File data (dibuat otomatis saat program dijalankan)

- `barang.json` — daftar barang dan stok
- `transaksi.csv` — riwayat penjualan

Dibuat oleh Muhammad Ridho Alfaris.
