#1
# black = input("Masuakan Nama Puisi: ")
# nama_file = 'puisi.txt'
# try:
#  with open(nama_file, 'r') as file:
#     print("Daftar Siswa (dibaca dengan 'with open'):")
#  for baris in file:
#     print(f"- {baris.strip()}")
# except FileNotFoundError:
#     print(f"Error: File '{nama_file}' tidak ditemukan. Mohon periksa kembali nama dan lokasi file.")

# black = input("Masukkan Nama Puisi: ")
# nama_file = 'puisi.txt'


# try:
#     with open('puisi.txt', 'r') as file:
#         print("seluruh text(dibaca dengan 'with open'):")
#         for baris in file:
#             print(f"- {baris.strip()}")
# except FileNotFoundError:
#     print(f"Error: File '{nama_file}' tidak ditemukan. Mohon periksa kembali nama dan lokasi file.")

# print()

#2
total_confidence = 0
jumlah_baris = 0
nama_file = input("masukan nama file: ")

try:
    with open('mbox-short.txt', 'r') as file:
        for baris in file:
            if baris.startswith('X-DSPAM-Confidence:'):
            # Mencari posisi titik dua
                titik_dua_pos = baris.find(':')
            # Memotong string dari posisi titik dua + 1 sampai akhir
                angka_string = baris[titik_dua_pos + 1:].strip()

        if jumlah_baris > 0:
            rata_rata = total_confidence / jumlah_baris
            print(f"Rata-rata Spam Confidence: {rata_rata}")
        else:
            print("Tidak ada baris 'X-DSPAM-Confidence:' yang ditemukan.")

except FileNotFoundError:
    print(f"Error:File '{nama_file}")


#3
# nama_file = input("Masukkan nama file: ")

# # Kondisi Easter Egg
# if nama_file.lower() == "na na boo boo":
#     print("NA NA BOO BOO TO YOU - You have been punk'd!")
# else:
#     try:
#         with open(nama_file, 'r') as file:
#             for baris in file:
#                 print(baris.upper(), end='')
#     except FileNotFoundError:
#         print(f"File '{nama_file}' tidak ditemukan.")