# Latihan 1: Manajemen Daftar Belanja
# Buat sebuah list kosong bernama belanjaan.
# Gunakan .append() untuk menambahkan "Telur", "Susu", dan "Roti".
# Gunakan .insert() untuk menambahkan "Apel" di posisi paling awal.
# Gunakan .remove() untuk menghapus "Susu".
# Cetak list akhir.

belanjaan_makanan = []
belanjaan_makanan.append("Telur")
belanjaan_makanan.append("Susu")
belanjaan_makanan.append("Roti")

belanjaan_makanan.insert(0,"Apel")  
belanjaan_makanan.remove("Susu")

print("kebutuhan yang di beli", belanjaan_makanan) 

# hewan = ["kucing", "anjing", "burung", "kucing", "ikan"]
# hewan.remove("kucing")
# print(hewan) #

# huruf = ['a', 'b', 'd', 'e']
# print("Sebelum insert:", huruf)
# # Sisipkan 'c' di indeks ke-2
# huruf.insert(2, 'c')
# print("Setelah insert:", huruf) # Output: ['a', 'b', 'c', 'd', 'e']

# daftar_buah = ["Apel", "Jeruk", "Mangga"]
# print("List awal:", daftar_buah)
# daftar_buah.append("Durian")
# print("Setelah append 'Durian':", daftar_buah)
# daftar_buah.append("Semangka")
# print("Setelah append 'Semangka':", daftar_buah)