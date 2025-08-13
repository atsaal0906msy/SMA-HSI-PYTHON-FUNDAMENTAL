#Muhammmad Atsaal Hakim
#jawaban pertemuan ke8

#1
'''
print("Bilangan ganjil dari 7 sampai 70:")
for i in range(0, 71, 7):
    print(i)
'''
#"Python". Gunakan for loop untuk membangun string baru yang merupakan kebalikan dari string
#Latihan 2: Pola Akumulator dengan String Buat program yang memiliki sebuah string: kalimat =
#tersebut.
#Petunjuk: Inisialisasi string kosong kalimat_terbalik = "". Di dalam loop, tambahkan setiap
#huruf ke depan kalimat_terbalik (kalimat_terbalik = huruf + kalimat_terbalik).
#Output yang diharapkan: "nohtyP"

#2

kalimat = "python"
kalimat_terbalik = ""
print("kalimat terbalik dari python adalah:")

for huruf in reversed(kalimat):
 kalimat_terbalik = kalimat_terbalik + huruf 

print(kalimat_terbalik)

#3
'''
jumlah = 0

for angka in range(1, 51):
    if angka % 3 == 0 and angka % 5 == 0:
        jumlah += 1

print("jumlah angka dari 1 sampai 51 yang habis dibagi 3 dan 5 adalah:", jumlah)
'''
#4
'''
for i in range(10, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
'''
#5

'''
n = int(input("masukan sebuah bilangan positif!!"))
hasil_faktorial = 1

for i in range(1, n, +1):
    hasil_faktorial *= i 

print(f"hasil faktorian dari {n} adalah {hasil_faktorial} ")
'''