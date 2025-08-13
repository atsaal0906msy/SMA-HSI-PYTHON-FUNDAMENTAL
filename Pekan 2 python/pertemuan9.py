'''
kalimat = "saya belajar python"

kararakter_pertama = kalimat
print(f"karakter di indeks 0 adalah: '{kararakter_pertama}'")
'''
'''
kalimat = "Saya Belajar Python"
# Mengambil karakter pertama
karakter_pertama = kalimat [5:12]
print(f"Karakter di indeks 0 adalah: '{karakter_pertama}'") # Output: 'S'
# Mengambil karakter kelima
karakter_kelima = kalimat [:4]
print(f"Karakter di indeks 4 adalah: '{karakter_kelima}'") # Output: ' '

# Mengambil karakter di indeks 13
karakter_ke_14 = kalimat [4:]
print(f"Karakter di indeks 13 adalah: '{karakter_ke_14}'") # Output: 'y'
'''
'''
nama = "Budi"
# Cara yang benar untuk "mengubah" nama
nama_baru = "J" + nama[1:] # Gabungkan "J" dengan potongan "udi" dari nama
print("Nama lama:", nama)
print("Nama baru:", nama_baru)
'''
#1
'''
s = "ngentod itu menyenangkan"

karakter_pertama = s [0]
print(f"ngentod luuu: '{karakter_pertama}'")
'''
#2
#Master Slicing Masih menggunakan string s = "Belajar Python itu Menyenangkan".
#Tulis kode slicing untuk mendapatkan dan mencetak substring berikut:
#"Python"
#6 / 6
#"Menyenangkan"
#"Belajar"
'''
s = "belajar python itu menyenangkan"

kaliamat_pertama = s [7:14]
print(f"index ke 7 sampai 14 adalah: '{kaliamat_pertama}'")

kaliamat_kedua = s [18:31]
print(f"index ke 18 sampai 31 adalah: '{kaliamat_kedua}'")

kaliamat_ketiga = s [0:7]
print(f"index ke 0 sampai 7 adalah: '{kaliamat_ketiga}'")
'''
#3
#Membalik Kata Buatlah sebuah program yang:
#Meminta pengguna memasukkan sebuah kata.
#Menggunakan slicing untuk membalik kata tersebut.
#Mencetak kata yang sudah dibalik.
#Menggunakan if untuk mengecek apakah kata tersebut adalah palindrom (kata yang sama jika
#dibaca dari depan maupun belakang, contoh: "kasur rusak"). Cetak pesan yang sesuai.

# while True:
#     data_input = input("Masukan kata: ")
    
#     if data_input.lower() == "done":
#         break
#     kata_terbalik = data_input[::-1]

#     print(f"kata terbalik: {kata_terbalik}")

# #mengecek apakah sindrom apa bukan

#     if data_input.lower() == kata_terbalik.lower():
#         print("kata ini adalah sindrom")
#     else:
#         print("ini bukan kata sindrom")

#4
# Kode Rahasia Buatlah sebuah program yang mengambil "kode rahasia" dari sebuah kalimat
# panjang. Aturannya adalah: ambil setiap karakter ketiga dari kalimat tersebut. Gunakan slicing dengan step
# untuk mengekstrak dan mencetak kode rahasia dari kalimat:
# "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

# kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
# # Ambil dari awal sampai akhir, dengan lompatan 3 
# lompat_3 = kalimat[::3]
# print(lompat_3)

#5
# Memperbaiki Nama Diberikan sebuah nama yang salah ketik: nama_salah = "dUDI
# sANTOSO". Kamu belum belajar string methods seperti .title() atau .upper(). Gunakan hanya
# indexing, slicing, dan penggabungan string (+) untuk memperbaiki nama tersebut menjadi "Budi
# Santoso". Cetak hasilnya.

nama_salah = "dUDI sANTOSO"
nama_benar = "Budi Santoso"
nama_perbaikan = 'B' + 'u' + 'd' + 'i' + '' + 'S' + 'a' + 'n' + 't' + 'o' + 's' + 'o'
print("nama_perbaikan:", nama_benar)