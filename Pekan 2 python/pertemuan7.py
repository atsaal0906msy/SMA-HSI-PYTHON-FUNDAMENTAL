#muhammad atsaal hakim
#jawaban pertemuan 2 pekan 2

#1 

x = 10

while x >= 0:
    print(x)
    x -=1

print("Blastoff!")

#2
'''
angka_rahasia = 7
while True:
    angka_rahasia = int(input(">"))
    if (angka_rahasia == 7):
        print('Selamat anda,pinter!')
        break
    else:
        print('Makanya rajin belajar!')

print('Terimakasih sudah bermain!!')
'''
#3
'''

total = 0
count = 0

while True:
    data_input = input("(:")
    
    if data_input.lower() == "done":
        break

    try:
        angka = float(data_input)
        total += angka
        count += 1
    except ValueError:
        print("Input tidak valid")
        continue

if count > 0:
    rata_rata = total / count
    print(f"\nTotal: {total}")
    print(f"Jumlah angka: {count}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("\nTidak ada angka yang dimasukkan.")
'''
'''
latihan_kata = "poke"
for huruf in latihan_kata:
    print(f"karakter saat ini {huruf}")
'''

# Membuat tabel perkalian sederhana
# Loop luar untuk baris (angka 1 sampai 3)
for i in range(1, 4):
 # Loop dalam untuk kolom (angka 1 sampai 3)
 for j in range(1, 4):
 # end='\t' membuat print tidak ganti baris, tapi memberi tab
    print(f"{i}x{j}={i*j}", end='\t')
 # Setelah loop dalam selesai, ganti baris
 print() # print kosong akan membuat baris baru
teman_teman = ["Budi", "Ani", "Charlie", "Dian"]
for teman in teman_teman:
 print(f"Selamat Tahun Baru, {teman}!")

 print("Selesai!")

# Membuat tabel perkalian sederhana
# Loop luar untuk baris (angka 1 sampai 3)
for i in range(1, 4):
 # Loop dalam untuk kolom (angka 1 sampai 3)
 for j in range(1, 4):
 # end='\t' membuat print tidak ganti baris, tapi memberi tab
    print(f"{i}x{j}={i*j}", end='\t')
 # Setelah loop dalam selesai, ganti baris
 print() # print kosong akan membuat baris baru