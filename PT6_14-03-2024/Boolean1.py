print("Latihan Boolean\n\n")

a = int(input("Masukkan nilai a = "))
b = int(input("Masukkan nilai b = "))
print(a)
print(b)

print("Jika a lebih besar dari b:")
print(a > b)

print("Jika b lebih besar dari a:")
print(a < b)

print("Jika a sama dengan b:")
if (a == b):
    print(True)
else:
    print(False)

if (a > 10000):
    a = a * 0.12
print("Nilai a jika lebih dari 10.000 akan diberi ppn sebesar 12%.\n Maka nilai a:", a)

if (b > 50000):
    b = b * 0.12
print("Nilai a jika lebih dari 10.000 akan diberi ppn sebesar 12%.\n Maka nilai a:", b)

c = a + b
print("Hasil a + b: ", c)

a = None
b = None
print("a = ",False)
print("b = ", False)