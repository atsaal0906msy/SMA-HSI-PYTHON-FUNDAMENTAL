#1
def buat_email(nama_pengguna, domain="coding.com"):
    return f"{nama_pengguna.lower()}@{domain.lower()}"

print(buat_email("budi"))
print(buat_email("ani", "belajar.id"))

#2

def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan} ({berat_kg} kg), express: {express}, asuransi: {asuransi}")

kirim_paket(barang="Sepatu_running", tujuan="Tangerang", berat_kg=3, express=True)


#3

def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah = len(daftar_angka)
    rata_rata = total / jumlah if jumlah != 0 else 0
    return total, jumlah, rata_rata

data = [10, 20, 30, 40, 50]
total, jumlah, rata_rata = analisis_daftar(data)
print("Total:", total)
print("Jumlah:", jumlah)
print("Rata-rata:", rata_rata)

#4
def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka untuk menghitung total, jumlah elemen, dan rata-rata.

    Args:
        daftar_angka (list of numbers): Daftar yang berisi angka-angka (int atau float).

    Returns:
        tuple: Tiga nilai yang dikembalikan secara berurutan:
            - Total jumlah semua angka (int/float),
            - Jumlah elemen dalam daftar (int),
            - Nilai rata-rata dari angka-angka tersebut (float).
    """
    total = sum(daftar_angka)
    jumlah = len(daftar_angka)
    rata_rata = total / jumlah if jumlah != 0 else 0
    return total, jumlah, rata_rata

help(analisis_daftar)

#5
 
def get_luas_lingkaran(radius):
    return 3.14159 * (radius ** 2)

luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)

print("Luas lingkaran (r=7):", luas_lingkaran_lambda(7))
