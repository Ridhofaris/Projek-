"""
Program Struk Belanja Sederhana
Tugas Python - Ridhofaris
"""

from datetime import datetime

def input_angka(prompt):
    while True:
        try:
            nilai = float(input(prompt).replace(".", "").replace(",", "."))
            if nilai < 0:
                print("Angka tidak boleh negatif, coba lagi.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.")

def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

def main():
    print("=" * 40)
    print("PROGRAM STRUK BELANJA".center(40))
    print("=" * 40)

    nama_toko = input("Nama toko (default: Toko Kapi): ") or "Toko Kapi"
    kasir = input("Nama kasir: ") or "-"

    items = []
    print("\nMasukkan barang (ketik 'selesai' untuk mengakhiri)")
    while True:
        nama = input("\nNama barang: ").strip()
        if nama.lower() == "selesai" or nama == "":
            if not items:
                print("Belum ada barang, tambahkan dulu ya.")
                continue
            break
        harga = input_angka(f"Harga '{nama}': Rp ")
        jumlah = input_angka(f"Jumlah '{nama}': ")
        total = harga * jumlah
        items.append({"nama": nama, "harga": harga, "jumlah": jumlah, "total": total})

    subtotal = sum(i["total"] for i in items)

    # Diskon sederhana: 5% jika belanja >= 100rb
    diskon = 0
    if subtotal >= 100000:
        diskon = subtotal * 0.05

    total_bayar = subtotal - diskon

    print(f"\nSubtotal: {rupiah(subtotal)}")
    if diskon > 0:
        print(f"Diskon 5%: -{rupiah(diskon)}")
    print(f"Total: {rupiah(total_bayar)}")

    bayar = input_angka("Uang bayar: Rp ")
    while bayar < total_bayar:
        print(f"Uang kurang {rupiah(total_bayar - bayar)}, masukkan lagi.")
        bayar = input_angka("Uang bayar: Rp ")

    kembalian = bayar - total_bayar

    # Cetak struk
    print("\n\n" + "=" * 40)
    print(nama_toko.center(40))
    print("Struk Belanja".center(40))
    print("-" * 40)
    print(f"Tanggal : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"Kasir   : {kasir}")
    print("-" * 40)

    for i in items:
        print(f"{i['nama']}")
        print(f"  {i['jumlah']:g} x {rupiah(i['harga']):>12} = {rupiah(i['total'])}")

    print("-" * 40)
    print(f"{'Subtotal':<20}: {rupiah(subtotal):>15}")
    if diskon > 0:
        print(f"{'Diskon 5%':<20}: -{rupiah(diskon):>14}")
    print(f"{'TOTAL':<20}: {rupiah(total_bayar):>15}")
    print(f"{'Bayar':<20}: {rupiah(bayar):>15}")
    print(f"{'Kembalian':<20}: {rupiah(kembalian):>15}")
    print("=" * 40)
    print("Terima kasih telah berbelanja!".center(40))
    print("=" * 40)

if __name__ == "__main__":
    main()
