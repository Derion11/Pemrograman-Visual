# Ask askstring (https://www.tutorialspoint.com/python/python_gui_programming.htm)
from tkinter.simpledialog import askstring
from tkinter import *
top = Tk()

top.geometry('100x100')
def show():
    num = askstring("Input", "Input a string value")
    print(num)

B = Button(top, text="Click", command = show)
B.place(x=50, y=50)

top.mainloop()