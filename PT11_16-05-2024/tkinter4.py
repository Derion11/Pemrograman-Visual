# DataInOut (Part 2 / Slide 14)
from tkinter import *
import tkinter.messagebox

class DataInOut:
    def __init__(self,root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')

        frame1 = Frame(self.root)
        frame1.grid()
        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)
        frame2 = Frame(frame1)
        frame2.grid(row=1, column=0)
        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)

        FirstNum = StringVar()
        SecondNum = StringVar()
        Hasil     = StringVar()
        
        self.lblFirstNum = Label(frame2, text='Masukkan bilangan pertama')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text= 'Masukkan bilangan kedua')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Entry(frame2, textvariable=Hasil)
        self.txtHasil.grid(row=2, column=1)

        def JUMLAHKAN():
            pertama = float(FirstNum.get())
            kedua = float(SecondNum.get())
            hasil = pertama + kedua
            Hasil.set(hasil)

        def RESET():
            # Logika reset angka
            Hasil.set(0)

        def KELUAR():
            result = tkinter.messagebox.askquestion("Konfirmasi", "Apakah Anda ingin keluar dari aplikasi?")
            if result == 'yes':
                root.quit()            
        
        self.btnJumlahkan = Button(frame3, command= JUMLAHKAN, text='Jumlahkan').grid(row=2, column=0)
        self.btnReset = Button(frame3, command= RESET, text='Reset').grid(row=2, column=1)
        self.btnKeluar = Button(frame3, command= KELUAR,text='Keluar').grid(row=2, column=2)



if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()