# cek_spek_pc.py
# Program kecil: menampilkan spesifikasi PC sendiri.
# Cocok buat kamu yang suka hardware tapi lagi belajar Python :)
# Cara jalanin:  python cek_spek_pc.py

import platform  # modul bawaan Python buat info sistem
import os        # modul bawaan Python buat info sistem operasi

print("=== Spesifikasi PC saya ===")
print("Sistem operasi :", platform.system(), platform.release())
print("Nama komputer  :", platform.node())
print("Prosesor       :", platform.processor() or "tidak terdeteksi")
print("Jumlah core    :", os.cpu_count())
print("Versi Python   :", platform.python_version())

# RAM butuh modul tambahan bernama psutil.
# Kalau belum ada, program tetap jalan, cuma info RAM yang dilewati.
try:
    import psutil
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    print(f"Total RAM      : {ram_gb:.1f} GB")
    disk = psutil.disk_usage("/")
    print(f"Total disk     : {disk.total / (1024 ** 3):.1f} GB")
    print(f"Disk terpakai  : {disk.percent}%")
except ImportError:
    print("Total RAM      : (belum tahu — install dulu: pip install psutil)")
    print("Info disk      : (butuh psutil juga)")

print("===========================")
print("Coba ubah: tambahkan info kartu grafis / kapasitas disk!")
