print("halo dunia 1234")

print("====VARIABLES====")
x = 2  #assignmetn direct
y = x + 4

x = 5

z = x #assignment indirect
print("nilai x = ", x)
print("nilai y = ", y)
print("nilai z = ", z)

print("====DATA TYPES====")
# integer: angka satuan yg tidak ada koma

print("====INTEGER====")
data_int = 7
tipe_data_int = type(data_int)
print("data: ", data_int, "tipe data: ", tipe_data_int)

#float: angka koma
print("====FLOAT====")
data_float = 5.6
print("data: ", data_float, "tipe data: ", type(data_float))

#boolean: tipe data biner => 0, 1 (true, false)
print("====BOOLEAN====")
data_bool = False
print("data: ", data_bool, "tipe data: ", type(data_bool))

#string: karakter, kumpulan karakter
print("====STRING====")
data_str = "hallo sekarang tanggal 18 may"
print("data: ", data_str, "tipe data: ", type(data_str))
print(f"data: {data_str}, tipe data: {type(data_str)}")
print("data: {}, tipe data: {}".format(data_str, type(data_str)))

dict_data = {"nama": "salsa", "kelas": "H"}
print("nama: {nama}, kelas: {kelas}".format_map(dict_data))

#list
print("====LIST====")
data_list = ['apple', 'banana', 'mango', 123]
print("data: ", data_list, "tipe data: ", type(data_list))
print(data_list[0]) #data pertama
print(data_list[3]) #data keempat
data_list[1] = 'grape'
print(data_list[1]) #data kedua
print("data: ", data_list, "tipe data: ", type(data_list))

#tuple
print("====TUPLE====")
pet = ('cat', 6, 'british shorthair')
print("data: ", pet, "tipe data: ", type(pet))
nama, umur, jenis = pet
print("jenis = ", jenis)

#set
print("==========SET==========")
colors = {'red', 'blue', 'yellow'}
print("data: ", colors, "tipe data: ", type(colors))
colors.add('black')
colors.remove('yellow')
print(colors)

#dictionaries teridiri dari key dan value
print("==========DICTIONARIES==========")
student = {
    'name': 'salsa',
    'age' : 17,
    'major' : 'math'
}
#keys: name, age, major
#value: 'salsa', 17, 'math'
print("data: ", student, "tipe data: ", type(student))
print(student['age'])
student['age'] = 20
print("data: ", student, "tipe data: ", type(student))

#datetime
print("==========DATETIME==========")
from datetime import datetime

datetime_now = datetime.now()
print("data date time: ", datetime_now, "tipe data: ", type(datetime_now))
date_now = datetime_now.date()
print("data tanggal saja: ", date_now, "tipe data: ", type(date_now))
time_now = datetime_now.time()
print("data waktu saja: ", time_now, "tipe data: ", type(time_now))
formatted_time = time_now.strftime('%H - %M')
print('data jam dan menit: ', formatted_time, "tipe data: ", type(formatted_time))

# casting data: merubah 1 tipe data ke tipe data lain
print("===========DATA CASTING==========")
#int
print("==data dari int==")
data_casting_int = 7
print(data_casting_int, type(data_casting_int))
casting_float = float(data_casting_int)
print(casting_float, type(casting_float))
casting_str = str(data_casting_int)
print(casting_str, type(casting_str))
casting_bool = bool(data_casting_int)
print(casting_bool, type(casting_bool))

#float
print("==data dari float==")
data_casting_float = 7.9
print(data_casting_float, type(data_casting_float))
casting_int = int(data_casting_float)
print(casting_int, type(casting_int))

#string
print("==data dari string==")
data_casting_string = "12345678"
print(data_casting_string, type(data_casting_string))
casting_int = int(data_casting_string)
print(casting_int, type(casting_int))
casting_bool = bool(data_casting_string)
print(casting_bool, type(casting_bool))

#aritmatika
print("==========ARITMATIKA==========")
from math import sqrt
a = 7
b = 6
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a ** b = ", a ** b)
print("a mod b = ", a % b)
print(sqrt(144))

alas  = 6
tinggi = 10
luas_segitiga = 0.5 * alas * tinggi
print("luas segitiga: ", luas_segitiga)

#operasi dasar text
print("==========OPERASI DASAR TEXT==========")
data_judul = "selamat pagi indonesia"
#upper, lower, capitalize, +, join, slicing, replace, split
data_upper = data_judul.upper()
print("data uppercase: ", data_upper)
data_lower = data_judul.lower()
print("data lowercase: ", data_lower)
data_capitalize = data_judul.capitalize()
print("data capitalize: ", data_capitalize)

#penggabungan
data1 = "halo"
data2 = "semua"
data_pengulangan = data1 * 2
print(data1 + " " + data2)
print(data_pengulangan)

#join
data = ['halo', 'selamat', 'malam']
data2 = ";".join(data)
print(data)
print(data2)

#slicing
halo = "ayo belajar python"
#[start word, banyaknya]
a = halo[4:11]
print(halo)
print(a)

#replace
a = "kentang goreng"
b = a.replace("goreng", "saus")
print(a)
print(b)

#split
data = "halo selamat malam"
z = data.split(" ")
print(z)

# if for, while, error handling

angka = 5
if angka ==5:
    print("lima")
elif angka == 10:
    print("sepuluh")
else:
    print(f"angka = {angka}")
    
#for
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print("")
    
#while
i = 1
while i <=5:
    print(i)
    i+=1 #i=I+1

data = 'halo'
try:
    data_int = int(data)
    print(int)
except:
    print("data tidak dapat dikonversi")