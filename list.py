#list
#kumpulan data
angka = 1
angka = 2
angka = 3
angka = 5
angka = [1, 2, 3, 4, 5]

sayuran = ["kangkung", "kol", "wortel", "bayam"]
print(sayuran)

#accessing list
print("======ACCESSING LIST======")
print(sayuran[1])
print(sayuran[-1])
print(sayuran[1], sayuran[3]) #[0, 1, 2]

#[start index:berapa banyak]
#item in list
print("====ITEM IN LIST=====")

#untuk mengecek apakah suatu item terdapat di dalam list
alat_tulis = ["buku", "pensil", "penghapus", "penggaris"]
if "buku" in alat_tulis:
    print("buku merupakan alat tulis")
else:
    print("buku tidak termasuk dalam alat tulis")
item = "pensil"

check_item = "pensil" in alat_tulis
print(f"apakah item {item} terdapat dalam lis alat tulis? {check_item}")
#changing item value

alat_tulis = ["buku", "pensil", "penghapus"]
#ubah index pertama
alat_tulis[0] = "penggaris"
print(alat_tulis)

alat_tulis[1:3] = ["pulpen", "spidol"]
print(alat_tulis)

#add and removing items
#append, insert (menggunakan indeks), extend
print("=====add items=====")

pet = ["kucing", "kelinci", "anjing"]
print(pet)

pet.append("kura-kura")
print(pet)

tambah_item = "burung"
pet.insert(1, tambah_item)
print(pet)

pet.extend(["ayan", "angsa"])
print(pet)

print("=====remove item======")
#remove, pop, clear, del

pet. remove("kucing")
print(pet)

ambil1_pet = pet.pop(1)
print(pet)
print(ambil1_pet)

del pet[0]
print(pet)

pet.clear()
print(pet)

#other operation
print("=====other operations=====")
#copy, count, index, reverse, sort
pet = ["kucing", "kelinci", "angsa", "burung"]
pet2 = pet.copy()

print(pet2)
print(pet.count("kelinci"))
print(pet.index("kucing"))
pet. reverse()
print(pet)
pet.sort()
print(pet)