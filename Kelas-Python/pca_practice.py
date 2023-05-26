# certified associate in python programming
print(5*"=", "soal soal contoh untuk certified associate in python programming", 5*"=")

#1
def f(n):
    if n == 1:
        return 1
    return n + f(n-1)
# print(f(2))

#2
def unclear(x):
    if x % 2 == 1:
        return 0
# print(unclear(1) + unclear(2))

#3
def f(n):
    for i in range(1, n+1):
        yield i #The Yield keyword in Python is similar to a 
        #return statement used for returning values or objects in Python.
for i in f(2):
    print(i, end=' ')
        