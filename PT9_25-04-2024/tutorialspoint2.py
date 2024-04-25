from tkinter.colorchooser import askcolor
from tkinter import *

def donothing():
    pass

def change_font_color():
    color = askcolor(title="Choose Font Color")[1]
    label.config(fg=color)

def change_font_background_color():
    color = askcolor(title="Choose Background Font Color")[1]
    label.config(bg=color)

root = Tk()
root.title("Main Frame")

main_frame = Frame(root)
main_frame.pack()

#----------------------------------Listbox---------------------------------
Lb1 = Listbox(main_frame)
Lb1.insert(1, "Bakuryu")
Lb1.insert(2, "Alice")
Lb1.insert(3, "Busuzima")
Lb1.insert(4, "Jin Long")
Lb1.insert(5, "Jenny")
Lb1.insert(6, "Xion")
Lb1.pack(side=LEFT)

#---------------------------------Menubutton-------------------------------
mb = Menubutton(main_frame, text="condiments", relief=RAISED)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)
mb.pack(side=LEFT)

#------------------------------------Menu----------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#------------------------------------Message-----------------------------------
var = StringVar()
label = Message(root, textvariable=var, relief=RAISED)
var.set("Hey!? How are you doing?")
label.pack()

#----------------------------------Radio Button--------------------------------
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack( anchor = W)
label = Label(root)
label.pack()

#-------------------------------------Scale-----------------------------------
def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()


# Button1
button1 = Button(root, text="Change Font Color", command=change_font_color)
button1.pack()

# Button2
button2 = Button(root, text="Change Font Background Color", command=change_font_background_color)
button2.pack()

root.mainloop()