"""
Batu-Gunting-Kertas - Game melawan komputer
Konsep yang dipakai: input, if-else, while loop, random, f-string.
Aturan: batu mengalahkan gunting, gunting mengalahkan kertas, kertas mengalahkan batu.
"""

import random

PILIHAN = ["batu", "gunting", "kertas"]

print("=" * 40)
print("   GAME BATU-GUNTING-KERTAS")
print("=" * 40)
print("Ketik: batu / gunting / kertas")
print("Ketik 'keluar' untuk berhenti.\n")

menang = 0
kalah = 0
seri = 0

while True:
    pemain = input("Pilihanmu: ").lower().strip()

    if pemain == "keluar":
        break

    if pemain not in PILIHAN:
        print("Pilih yang benar: batu, gunting, atau kertas.\n")
        continue

    komputer = random.choice(PILIHAN)
    print(f"Komputer memilih: {komputer}")

    if pemain == komputer:
        print("Seri!\n")
        seri += 1
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        print("Kamu menang!\n")
        menang += 1
    else:
        print("Kamu kalah!\n")
        kalah += 1

print("=" * 40)
print("   HASIL AKHIR")
print("=" * 40)
print(f"Menang : {menang}")
print(f"Kalah  : {kalah}")
print(f"Seri   : {seri}")

if menang > kalah:
    print("Hebat, kamu mengalahkan komputer!")
elif kalah > menang:
    print("Komputer menang kali ini, coba lagi!")
else:
    print("Seimbang! Pertandingan yang seru.")

print("Terima kasih sudah bermain!")
