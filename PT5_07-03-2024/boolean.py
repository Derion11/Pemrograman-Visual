# Case 1
print("Case 1")
# Data yang bertipe boolean yang kita deklarasikan (Cara standar)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("================================================")

# Case 2
print("Case 2")
# Data bertipe boolean dalam berbagai konteks
# Tercatat dengan sendirinya oleh komputer tanpa deklarasi
print(3>2)
print(3 + 2 == 5)
print(3<2)
print("================================================")

# Case 3
print("Case 3")
# Data bertipe boolean dalam berbagai konteks
# Tercatat dengan sendirinya oleh komputer tanpa deklarasi
penghasilan = 20000000
penghasilantanpapajak = 4000000
if penghasilan <= penghasilantanpapajak:
    penghasilan = 0.1 * penghasilan

print("Pajak yang harus anda bayar: Rp ", penghasilan)

# Part 2
# Case 4
print("Case 2")
# Semua data yang tidak nol (kosong) memiliki nilai Boolean True
a = 3
b = "Ini data string."
c = ("laptop", "buku", "ballpen")
d = ["laptop", "buku", "ballpen"]
e = {"laptop":"asus", "buku":"buku_teks", "ballpen":"arrow"}
f = {1, 2, 3, 4, 5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("================================================")

# Part 3
# Case 5
print("Case 5")
# Variabel yang kosong memiliki nilai boolean false
a = 0
b = ""
c = ()
d = []
e = {}

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("================================================")

# Case 6
print("Case 6")
# Variabel yang panjangnya nol memiliki nilai boolean false
class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("================================================")
