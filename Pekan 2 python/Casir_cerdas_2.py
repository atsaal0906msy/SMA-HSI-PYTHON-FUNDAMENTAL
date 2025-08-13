#Casir cerdas ke 2

def tampilkan_header():
    print("=" * 40)
    print("    SELAMAT DATANG DI TOKO SERBAGUNA") 
    print("=" * 40)
    print("\n--- Masukkan Detail Barang ---")
    print("(Ketik 'selesai' di nama barang untuk selesai)\n")


def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total


def hitung_diskon(subtotal):
    if subtotal >= 500_000:
        persen = 10
    elif subtotal >= 200_000:
        persen = 5
    else:
        persen = 0
    diskon = subtotal * persen / 100
    return diskon, persen


def tampilkan_struk(nama_barang, harga_barang, jumlah_barang, subtotal, total_diskon, persen_diskon):
    print("\nMenghitung total belanja Anda...\n")
    print("=" * 60)
    print("         STRUK PEMBELIAN ANDA")
    print("=" * 60)
    print("Detail Belanja:")

    for i in range(len(nama_barang)):
        nama = nama_barang[i]
        harga = harga_barang[i]
        jumlah = jumlah_barang[i]
        total = harga * jumlah
        print(f"{i+1}. {nama:<18} ({jumlah} x Rp {harga}) = Rp {total}")

    print("-" * 40)
    print(f"Subtotal            : Rp {subtotal}")
    print(f"Diskon ({persen_diskon}%)        : - Rp {total_diskon}")
    print("-" * 40)
    print(f"Total yang harus dibayar: Rp {subtotal - total_diskon}")
    print("=" * 40)
    print("      TERIMA KASIH TELAH BERBELANJA!")
    print("=" * 40)


daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []

tampilkan_header()

while True:
    nama = input("Nama Barang: ").strip()
    if nama.lower() == "selesai":
        break

    try:
        harga = float(input("Harga Satuan: Rp "))
        jumlah = int(input("Jumlah: "))
        if harga < 0 or jumlah <= 0:
            print("Harga dan jumlah harus positif.\n")
            continue
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.\n")
        continue

    daftar_nama_barang.append(nama)
    daftar_harga_barang.append(harga)
    daftar_jumlah_barang.append(jumlah)

    print("--- Barang berhasil ditambahkan! ---\n")


subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)
diskon, persen = hitung_diskon(subtotal)
tampilkan_struk(daftar_nama_barang, daftar_harga_barang, daftar_jumlah_barang, subtotal, diskon, persen)
