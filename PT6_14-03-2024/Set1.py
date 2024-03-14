'''
Latihan Set
Print      
Len         
Add         
Update      
Remove      
Discard     
Pop         
Clear       
Union
'''

# Stuffs
print("Dalam sebuah mall, Derion membeli satu keyboard dan mouse. Selain itu ia juga ingin membeli beberapa barang/gadgets yang lain.\nGadgets yang dimaksud adalah:")
set1 = {"Keyboard", "Mouse"}
item = input("Masukkan barang: ")
response = input("Apakah ingin menambahkan barang? (ya/tidak): ")
while response.lower() == "ya":
    item = input("Masukkan barang: ")
    if item not in set1:
        set1.add(item)
    else:
        print("Barang telah dibeli.")

    response = input("Apakah ingin menambahkan barang? (ya/tidak): ")

print(set1)

print("\nAdik Derion menyelipkan jam tangan dan gelangnya ke dalam tas...")         # Update
set1.update(["Jam Tangan", "Gelang"])
print("Isi dalam tas: ", set1)

print("\nTernyata ketika dalam perjalanan, keyboard yang dibeli tertinggal!")       # Remove
set1.remove("Keyboard")
print("Isi dalam tas: ", set1)

print("\nDi dalam mobil, Derion menghitung jumlah barang yang ada di dalam tasnya.")   # Len
print("Jumlah barang dalam tas: ", len(set1))

print("\nPada saat itu juga, Adik Derion mengeluarkan barang-barang yang ia selipkan dalam tas kakaknya dan memasukkan ke dalam tas miliknya.")   # Discard
set1.discard("Jam Tangan")
set1.discard("Gelang")
print("Isi dalam tas (Derion): ", set1)
set2 = {"Jam Tangan", "Gelang"}
print("Isi dalam tas (Adik): ", set2)

print("\nDua tas saudara tersebut digabungkan dalam sebuah kardus agar barang-barang mereka tidak tercecer.")   # Union
set3 = set1.union(set2)
print("Isi dalam tas (Derion): ", set1)
print("Isi dalam tas (Adik): ", set2)
print("Isi dalam kardus: ", set3)

print("\nSesampainya di rumah, Derion mengeluarkan barang yang paling terlihat dalam tas dan meletakkannya di atas meja.")   # Pop
set1.pop()
print("Isi dalam tas (Derion): ", set1)
print("Isi dalam tas (Adik): ", set2)

print("\nMelihat kakaknya yang mengeluarkan barang-barangnya dalam tas, sang adik ingin mencari barang-barang yang ia selipkan dalam tas. Sang adik mengeluarkan semua barang dalam tas tersebut")   # Clear
set1.clear()
print("Isi dalam tas: ", set1)

del set1    # Hapus set