# Latihan 3: Analisis Kata
# Buat program yang:
# Meminta pengguna memasukkan sebuah kalimat.
# Gunakan .split() untuk mengubah kalimat tersebut menjadi sebuah list kata-kata.
# Gunakan len() untuk menghitung dan mencetak jumlah kata dalam kalimat.
# Gunakan .sort() pada list tersebut untuk mengurutkan kata-kata berdasarkan abjad, lalu cetak
# list yang sudah terurut.

# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Mengubah kalimat menjadi list kata-kata
kata_kata = kalimat.split()

# Menghitung jumlah kata
jumlah_kata = len(kata_kata)
print(f"Jumlah kata dalam kalimat: {jumlah_kata}")

# Mengurutkan kata-kata berdasarkan abjad
kata_kata.sort()     

# Mencetak list yang sudah terurut
print("Kata-kata yang sudah terurut berdasarkan abjad:")
print(kata_kata)
