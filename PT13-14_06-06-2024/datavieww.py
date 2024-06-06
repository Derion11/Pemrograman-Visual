from tkinter import *
from tkinter.ttk import *
from plotdata import regression_plot
from stats import stats_columns

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Data View")

        self.label1 = Label(self.master, text="File Name")
        self.label2 = Label(self.master, text="X Label")
        self.label3 = Label(self.master, text="Y Label")

        self.label1.grid(row=0)
        self.label2.grid(row=1)
        self.label3.grid(row=2)

        self.eFname = Entry(self.master, width=48)
        self.ex = Entry(self.master, width=40)
        self.ey = Entry(self.master, width=40)

        self.eFname.grid(row=0, column=1, sticky=W)
        self.ex.grid(row=1, column=1, sticky=W)
        self.ey.grid(row=2, column=1, sticky=W)

        self.txtX = Text(self.master, width=30)
        self.txtY = Text(self.master, width=30)

        self.txtX.grid(row=3, column=0, sticky=W)
        self.txtY.grid(row=3, column=1, sticky=W)

        self.style = Style()
        self.style.map('D.TButton',
            foreground=[('pressed', 'red'), ('active', 'green')],
            background=[('pressed', 'black'), ('active', 'white')]
        )

        self.btn_show_graph = Button(self.master, text="Show Regression Graph", style="D.TButton", command=self.show_graph)
        self.btn_show_graph.grid(row=4, column=0, sticky=W)
        
        self.btn_show_stats = Button(self.master, text="Show Stats", style="D.TButton", command=self.show_stats)
        self.btn_show_stats.grid(row=4, column=1, sticky=W)
        
        self.btn_quit = Button(self.master, text="Quit", style="D.TButton", command=self.master.destroy)
        self.btn_quit.grid(row=4, column=2, sticky=E)
        
    def show_graph(self):
        regression_plot(self.eFname.get(), self.ex.get(), self.ey.get())
    
    def show_stats(self):
        xstats, ystats = stats_columns(self.eFname.get(), self.ex.get(), self.ey.get())
        self.txtX.insert(INSERT, xstats)
        self.txtY.insert(INSERT, ystats)
        
root = Tk()
app = Application(master=root)
app.mainloop()
