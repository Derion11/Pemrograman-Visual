#----------------------------------Button----------------------------------------
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("500x500")

def helloCallBack():
    msg=messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top,bg= 'yellow', text ="Press Here", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()

#---------------------------------Checkbox---------------------------------------
# from tkinter import *

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20)
C1.pack()
C2.pack()

top.mainloop()

#---------------------------------Frame------------------------------------------
# from tkinter import *

root = Tk()
#root.geometry("700x700")
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()

#---------------------------------Entry------------------------------------------
# from tkinter import *

top = Tk()

L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()

#---------------------------------Label------------------------------------------
# from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()