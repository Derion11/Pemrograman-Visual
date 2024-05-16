# Ask askfloat (https://www.tutorialspoint.com/python/python_gui_programming.htm)
# Baris kode ini sedikit dimodifikasi untuk yaitu tombol exit
from tkinter.simpledialog import askfloat
from tkinter import *
import tkinter.messagebox
top = Tk()

top.geometry('500x500')
def show():
    num = askfloat("Input", "Input a floating point number")
    print(num)

def exit():
    result = tkinter.messagebox.askquestion("Konfirmasi", "Apakah Anda ingin keluar dari aplikasi?")
    if result == 'yes':
        top.quit()


A = Button(top, text= "Exit", bg='red', command= exit)
A.place(x=100, y=100)

B = Button(top, text="Click", command = show)
B.place(x=50, y=50)

top.mainloop()