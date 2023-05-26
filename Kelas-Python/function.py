'''FUNCTION WITH RETURN'''

#template fungsi dengan kembalian
#supaya bisa dikembalikan ke sebuah variabel

# def nama_fungsi(parameter):
#     badan fungsi
#     return hasil

# y = nama_fungsi(x):
# print(y) #y bisa disebut juga argumen

# def f(x):
#    for i in x:
#        print()

# f([])


# def f(n):
#  if n==1:
#   return 1
#  return n+f(n-1)
# print(f(2))

# def faktorial(n):
#    if n <= 1:
#        return 1
#    else:
#        return n * faktorial(n-1)

# print(faktorial(5))

kali2 = lambda a : a * 2
print(kali2(2))

tambah = lambda a, b : a + b
print(tambah(1, 2))

faktorial = lambda n : n * faktorial(n - 1) if n > 1 else 1

print(faktorial(5))