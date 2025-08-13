# print("selamat pagi, indonesia.".capitalize()) # Output: Selamat pagi

# kalimat = "Python sangat mudah, Python itu keren."
# posisi1 = kalimat.find("Python")
# posisi2 = kalimat.find("mudah")
# posisi3 = kalimat.find("Java")
# print(f"'Python' ditemukan di indeks: {posisi1}") # Output: 0
# print(f"'mudah' ditemukan di indeks: {posisi2}") # Output: 14
# print(f"'Java' ditemukan di indeks: {posisi3}") # Output: -1

# filename = "laporan_keuangan.pdf"
# if filename.endswith(".pdf"):
#  print("Ini adalah file PDF.")

#1
# Standarisasi Judul
# Buat program yang meminta pengguna memasukkan judul buku yang mungkin diketik dengan huruf
# besar/kecil yang acak (misal: "aLaDiN dan LaMPu aJAib"). Programmu harus membersihkan spasi ekstra di
# awal/akhir dan mengubahnya ke format Title Case yang benar.

judul_buku = input("Masukan Judul Buku: ")
perbaikan = judul_buku.title()
sepasi = perbaikan.strip( )

print(sepasi)

#2
# Validasi Email Sederhana
# Buat program yang meminta pengguna memasukkan alamat email. Program harus melakukan dua
# pengecekan sederhana:
# Apakah email mengandung karakter @? (Gunakan find() atau operator in).
# Apakah email diakhiri dengan .com atau .co.id? (Gunakan .endswith()).
# Cetak pesan "Email valid" atau "Email tidak valid" berdasarkan hasil pengecekan

# buat_email = input("Masukana Email Anda: ")
# if "@" in buat_email:
#     print("Email Valid")
# else:
#     print("Email Tidak Valid")

# #3
# Latihan 3: Sensor Kata
# Buat program yang memiliki sebuah kalimat dan sebuah kata yang ingin disensor. Program harus mengganti
# semua kemunculan kata terlarang itu dengan tanda bintang ***.
# Contoh: kalimat = "Harga tiketnya sangat mahal.", kata_sensor = "mahal".
# Output yang diharapkan: "Harga tiketnya sangat ***.

# def kata_sensor(kalimat, sensor):
#     kalimat_sensor = kalimat.replace(sensor, "***")
#     return kalimat_sensor


# kalimat = "SMA HSI sangat jelek"
# kata_yang_disensor = "jelek"

# hasil = kata_sensor(kalimat, kata_yang_disensor)
# print(hasil)

#4
# Akronim Generator
# Buat program yang meminta pengguna memasukkan sebuah nama organisasi yang panjang (misal: "Badan
# Usaha Milik Negara"). Program harus:
# Memecah input menjadi list kata-kata.
# Mengambil huruf pertama dari setiap kata.
# Menggabungkan huruf-huruf pertama tersebut menjadi satu string akronim dalam huruf kapital.
# Output yang diharapkan: "BUMN"

# nama = input("Masukan Nama Organisasi kamu: ")
# nama_lengkap = nama.split()

# akronim = ""
# for kata in nama_lengkap:
#     akronim += kata[0].upper()

# print("Singkatannya: ", akronim)

#5

# import re  

# judul = input("Masukkan judul artikel: ")

# judul = judul.lower()
# judul = judul.replace(" ", "-")

# slug = re.sub(r'[^a-z0-9\-]', '', judul)
# print("Slug:", slug)
