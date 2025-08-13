# Memahami Aliasing
# Prediksikan output dari kode di bawah ini sebelum menjalankannya. Jelaskan mengapa outputnya seperti
# itu.
# a = [1, 2, 3, 4, 5]
# b = a
# c = a.copy()
# b[1] = 20
# c[1] = 30
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")

a = [1, 2, 3, 4, 5]  # list asli
b = a                # b menjadi alias dari a (mengacu ke list yang sama)
c = a.copy()         # c adalah salinan baru dari a (list terpisah)

b[1] = 20            # ubah elemen indeks 1 di b → karena b dan a sama, a ikut berubah
c[1] = 30            # ubah elemen indeks 1 di c → tidak memengaruhi a/b

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
      