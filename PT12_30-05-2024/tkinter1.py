# Frameku (Slide 9)
# Tombol Entryku (Slide 10)
import tkinter as tk

root = tk.Tk()

#----------------------------Latihan-1: Membuat Widget Dasar#----------------------------
# WidgetDasarku = tk.Tk()
# WidgetDasarku.mainloop()

#----------------------------Latihan-2: Membuat Canvas-----------------------------------
# Kanvasku = tk.Canvas(root, height, = 1000, width = 1920)
# Kanvasku.pack()

#----------------------------Latihan-3: Membuat Canvas-----------------------------------
Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth= 0.8, relheight= 0.8)

#-------------------------Latihan-4a: Membuat Button di Root-------------------------
# Tombolku = tk.Button(root, text= "Tes Tombol", bg='gray', fg='red')
# Tombolku.pack()

#-------------------------Latihan-4b: Membuat Button di Frame-------------------------
Tombolku = tk.Button(Frameku, text= "Tes Tombol", bg='gray', fg= 'red')
Tombolku.pack()

#-------------------------Latihan-6: Membuat Entry------------------------------------
Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()




root.mainloop()