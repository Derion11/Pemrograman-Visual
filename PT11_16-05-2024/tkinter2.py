# Cetak Data (Slide 12)
from tkinter import *

root = Tk()
root.geometry('400x200')

def CetakData():
    teks = entry1.get()
    print(teks)
    return None

entry1 = Entry(root, width= 20)
entry1.pack()
Button(root, text='Cetak Data', bg='yellow', command= CetakData).pack()

root.mainloop()