#Mhammad Atsaal Hakim
#jawaban

#1

def salam_pembuka():
    print("===============================")
    print("Selamat Datang Di Program Saya!")
    print("===============================")


salam_pembuka()

#2

def info_cuaca(kota,cuaca):
    print(f"cuaca di kota {kota} hari ini {cuaca}.")


info_cuaca("jakarta", "berawan")

#3

def kubik(angka):
    return angka ** 3


hasil_kubik = kubik(4)
print(hasil_kubik) #output: 64


#4

def hitung_diskon(harga_awal, persen_diskon):
    jumlah_diskon = harga_awal * (persen_diskon / 100)
    harga_akhir = harga_awal - harga_akhir
    return harga_akhir

try:
    harga = float(input("masukan harga barang: "))
    diskon = float(input("masukan persentase diskon (%): "))

    harga_setelah_diskon = hitung_diskon(harga, diskon)
    print(f"harga akhir setelah diskon: Rp {harga_setelah_diskon:.2f}")
except ValueError:
    print("Error: Masuakan angka yang valid.")

#5

def fahrenheit_ke_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

# Panggil fungsi dengan 98.6 dan cetak hasilnya
hasil_celsius = fahrenheit_ke_celsius(98.6)
print(f"98.6 derajat Fahrenheit = {hasil_celsius:.2f} derajat Celsius")
