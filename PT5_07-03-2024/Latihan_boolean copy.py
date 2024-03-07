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
print(1>2)
print(1 + 1 == 2)
print(5<1)
print("================================================")

# Case 3
print("Case 3")
# Data bertipe boolean dalam berbagai konteks
# Tercatat dengan sendirinya oleh komputer tanpa deklarasi
penghasilan = 50000
pajak = 0.5
if penghasilan >= 40000 :
    penghasilan = pajak * penghasilan
print("Penghasilan")
print("Pajak yang harus anda bayar: Rp ", penghasilan)
print("================================================")


# Case 6
print("Case 6")
# Variabel yang panjangnya nol memiliki nilai boolean false
class myclass():
    def __len__(self):
        return 2
print(bool(myclass()))
print("================================================")
