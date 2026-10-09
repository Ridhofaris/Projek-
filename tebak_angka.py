"""
Tebak Angka - Game sederhana untuk belajar Python
Cara main: komputer memilih angka acak 1-100, kamu menebaknya dalam 7 kesempatan.
Konsep yang dipakai: input, if-else, while loop, random, f-string.
"""

import random

print("=" * 40)
print("   GAME TEBAK ANGKA (1 - 100)")
print("=" * 40)
print("Komputer sudah memilih angka rahasia.")
print("Kamu punya 7 kesempatan untuk menebaknya.\n")

angka_rahasia = random.randint(1, 100)
kesempatan = 7
menang = False

while kesempatan > 0:
    print(f"Sisa kesempatan: {kesempatan}")
    tebakan = input("Tebakanmu: ")

    # Pastikan input berupa angka
    if not tebakan.isdigit():
        print("Masukkan angka saja ya!\n")
        continue

    tebakan = int(tebakan)
    kesempatan -= 1

    if tebakan == angka_rahasia:
        print(f"\nBenar! Angkanya memang {angka_rahasia}. Kamu menang!")
        menang = True
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil, coba angka yang lebih besar.\n")
    else:
        print("Terlalu besar, coba angka yang lebih kecil.\n")

if not menang:
    print(f"\nKesempatan habis! Angka rahasianya adalah {angka_rahasia}.")
    print("Coba lagi, pasti bisa!")

print("Terima kasih sudah bermain!")
