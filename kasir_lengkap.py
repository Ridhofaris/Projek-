"""
Sistem Kasir Lengkap
- Kelola stok barang (tambah, lihat)
- Transaksi penjualan dengan cek stok otomatis
- Simpan semua transaksi ke file CSV
- Laporan harian: omzet, item terjual, barang terlaris

Data tersimpan di:
- barang.json   -> daftar barang + stok
- transaksi.csv  -> riwayat penjualan
"""

import json
import csv
import os
from datetime import datetime

FILE_BARANG = "barang.json"
FILE_TRANSAKSI = "transaksi.csv"


# ---------- Helper ----------
def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")


def input_angka(prompt):
    """Minta input angka, ulangi sampai valid dan > 0."""
    while True:
        try:
            teks = input(prompt).replace(".", "").replace(",", ".").strip()
            nilai = float(teks)
            if nilai <= 0:
                print("Masukkan angka lebih dari 0.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid, masukkan angka.")


# ---------- Data barang (JSON) ----------
def muat_barang():
    if not os.path.exists(FILE_BARANG):
        return {}
    with open(FILE_BARANG, "r") as f:
        return json.load(f)


def simpan_barang(data):
    with open(FILE_BARANG, "w") as f:
        json.dump(data, f, indent=2)


# ---------- Menu barang ----------
def tambah_barang(barang):
    kode = input("Kode barang (mis. MIE01): ").strip().upper()
    if not kode:
        print("Kode tidak boleh kosong.")
        return
    if kode in barang:
        print("Kode sudah dipakai, gunakan kode lain.")
        return
    nama = input("Nama barang: ").strip()
    if not nama:
        print("Nama tidak boleh kosong.")
        return
    harga = input_angka("Harga (Rp): ")
    stok = int(input_angka("Stok awal: "))
    barang[kode] = {"nama": nama, "harga": harga, "stok": stok}
    simpan_barang(barang)
    print(f"Barang '{nama}' berhasil ditambahkan.")


def lihat_barang(barang):
    if not barang:
        print("Belum ada barang. Tambahkan dulu lewat menu 1.")
        return
    print(f"\n{'Kode':<8} {'Nama':<20} {'Harga':>14} {'Stok':>6}")
    print("-" * 52)
    for kode, b in barang.items():
        print(f"{kode:<8} {b['nama']:<20} {rupiah(b['harga']):>14} {b['stok']:>6}")


# ---------- Transaksi ----------
def simpan_transaksi(baris):
    """Simpan satu baris transaksi ke CSV (buat header jika file baru)."""
    baru = not os.path.exists(FILE_TRANSAKSI)
    with open(FILE_TRANSAKSI, "a", newline="") as f:
        w = csv.writer(f)
        if baru:
            w.writerow(["tanggal", "kode", "nama", "jumlah", "harga", "total"])
        w.writerow(baris)


def transaksi(barang):
    if not barang:
        print("Belum ada barang. Tambahkan dulu lewat menu 1.")
        return
    lihat_barang(barang)
    keranjang = []
    while True:
        kode = input("\nKode barang (ketik 'selesai' untuk bayar): ").strip().upper()
        if kode == "SELESAI":
            break
        if kode not in barang:
            print("Kode tidak ditemukan.")
            continue
        b = barang[kode]
        if b["stok"] <= 0:
            print(f"Stok '{b['nama']}' habis!")
            continue
        jumlah = int(input_angka(f"Jumlah '{b['nama']}' (stok: {b['stok']}): "))
        if jumlah > b["stok"]:
            print(f"Stok tidak cukup, sisa {b['stok']}.")
            continue
        keranjang.append({
            "kode": kode, "nama": b["nama"],
            "harga": b["harga"], "jumlah": jumlah,
        })
        print(f"Ditambahkan: {jumlah} x {b['nama']}")

    if not keranjang:
        print("Transaksi dibatalkan.")
        return

    subtotal = sum(i["harga"] * i["jumlah"] for i in keranjang)
    diskon = subtotal * 0.05 if subtotal >= 100000 else 0
    total = subtotal - diskon

    print(f"\nSubtotal: {rupiah(subtotal)}")
    if diskon:
        print(f"Diskon 5%: -{rupiah(diskon)}")
    print(f"Total: {rupiah(total)}")

    bayar = input_angka("Uang bayar: Rp ")
    while bayar < total:
        print(f"Uang kurang {rupiah(total - bayar)}, masukkan lagi.")
        bayar = input_angka("Uang bayar: Rp ")
    kembalian = bayar - total

    # Kurangi stok & catat transaksi
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in keranjang:
        barang[i["kode"]]["stok"] -= i["jumlah"]
        simpan_transaksi([waktu, i["kode"], i["nama"],
                          i["jumlah"], i["harga"], i["harga"] * i["jumlah"]])
    simpan_barang(barang)

    # Cetak struk
    print("\n" + "=" * 40)
    print("STRUK BELANJA".center(40))
    print(f"Tanggal: {waktu}".center(40))
    print("-" * 40)
    for i in keranjang:
        print(f"{i['nama']}")
        print(f"  {i['jumlah']} x {rupiah(i['harga']):>12} = {rupiah(i['harga'] * i['jumlah'])}")
    print("-" * 40)
    print(f"TOTAL: {rupiah(total)}")
    print(f"Bayar: {rupiah(bayar)} | Kembali: {rupiah(kembalian)}")
    print("=" * 40)
    print("Terima kasih telah berbelanja!".center(40))
    print("=" * 40)


# ---------- Laporan harian ----------
def laporan_harian():
    if not os.path.exists(FILE_TRANSAKSI):
        print("Belum ada transaksi tercatat.")
        return
    hari_ini = datetime.now().strftime("%Y-%m-%d")
    total_omzet = 0
    jumlah_item = 0
    per_barang = {}
    with open(FILE_TRANSAKSI, newline="") as f:
        for row in csv.DictReader(f):
            if row["tanggal"].startswith(hari_ini):
                jumlah_item += 1
                total_omzet += float(row["total"])
                nama = row["nama"]
                per_barang[nama] = per_barang.get(nama, 0) + int(float(row["jumlah"]))
    if jumlah_item == 0:
        print("Belum ada transaksi hari ini.")
        return
    print(f"\nLAPORAN PENJUALAN {hari_ini}")
    print(f"Item terjual : {jumlah_item}")
    print(f"Total omzet  : {rupiah(total_omzet)}")
    print("\nBarang terlaris:")
    for nama, jml in sorted(per_barang.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  - {nama}: {jml} pcs")


# ---------- Menu utama ----------
def main():
    barang = muat_barang()
    while True:
        print("\n=== SISTEM KASIR ===")
        print("1. Tambah barang")
        print("2. Lihat stok barang")
        print("3. Transaksi penjualan")
        print("4. Laporan harian")
        print("5. Keluar")
        pilih = input("Pilih (1-5): ").strip()
        if pilih == "1":
            tambah_barang(barang)
        elif pilih == "2":
            lihat_barang(barang)
        elif pilih == "3":
            transaksi(barang)
        elif pilih == "4":
            laporan_harian()
        elif pilih == "5":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
