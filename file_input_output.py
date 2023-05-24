f = open("file contoh.txt", mode="w")
f.write("Penambahan data baru\n")
f.close()

f = open("file contoh.txt", mode="a")
f.write("penambahan data\n")
f.close()

f = open("file contoh.txt", mode="a")
f.write("penambahan data lagi")

print(f"apakah file sudah diclose? {f.closed}")

f.close()

print(f"apakah file sudah diclose? {f.closed}")


print(5*"=", "pembacaan file", 5*"=")
read_file = open("file contoh.txt","r")
# print(read_file.read())
# print(read_file.readline(), end="")
print(read_file.readlines())

print(5*"=", "teknik pembacaan file dengan with", 5*"=")

with(open("new_file.txt", "r")) as file:
    content = file.readline()
    print(content)
    print(f"apakah file sudah diclose? {f.closed}")

print(8*"=", "membuat file excel", 8*"=")
