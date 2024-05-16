# The Complete Code (https://www.tutorialspoint.com/python/python_gui_programming.htm)
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()

data = [
    ["Garox",26,20000],
    ["Luis Beton",31,23000],
    ["Reza Kebab",18,19000],
    ["Asep Aspal",22,20500],

]
index = 0
def read_data():
    for index, line in enumerate(data):
        tree.insert('', tk.END, iid= index,
                    text = line[0], values = line [1:])
columns = ("age", "salary")

tree = ttk.Treeview(root, columns=columns, height=20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Name')
tree.heading('age', text='Age (yrs)')
tree.heading('salary', text='Salary (usd)')

read_data()
root.mainloop()