# Program Kasir Cerdas Sederhana

print("="*44)
print("SELAMAT DATANG DI PROGRAM KASIR CERDAS!")
print("="*44)

# Input Barang 1
print("\n--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan: Rp "))
jumlah_1 = int(input("Jumlah: "))

# Input Barang 2
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan: Rp "))
jumlah_2 = int(input("Jumlah: "))

# Hitung total per barang
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2

# Hitung subtotal
subtotal = total_1 + total_2

# Hitung diskon
if subtotal > 200_000:
    persentase_diskon = 10
elif subtotal > 100_000:
    persentase_diskon = 5
else:
    persentase_diskon = 0

jumlah_diskon = subtotal * persentase_diskon / 100
total_akhir = subtotal - jumlah_diskon

# Cetak struk
print("\nMenghitung total...\n")

print("="*44)
print("         STRUK PEMBELIAN ANDA")
print("="*44)
print("Detail Belanja:")
print(f"1. {nama_barang_1:15} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2:15} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("-"*44)
print(f"Subtotal            : Rp {subtotal}")
print(f"Diskon ({persentase_diskon}%)       : - Rp {jumlah_diskon}")
print("-"*44)
print(f"Total yang harus dibayar: Rp {total_akhir}")
print("="*44)
print("     TERIMA KASIH TELAH BERBELANJA!")
print("="*44)
