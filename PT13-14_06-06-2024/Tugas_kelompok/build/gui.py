from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Kuliah\Semester 4\Pemrograman Visual\PT13-14_06-06-2024\Tugas_kelompok\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("File selected:", file_path)


window = Tk()

window.geometry("855x481")
window.configure(bg = "#2FFFD9")


canvas = Canvas(
    window,
    bg = "#2FFFD9",
    height = 481,
    width = 855,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    439.0,
    135.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=select_file,
    relief="flat"
)
button_1.place(
    x=361.5882568359375,
    y=223.0,
    width=154.41175842285156,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=362.0,
    y=309.0,
    width=154.41175842285156,
    height=35.0
)
window.resizable(False, False)
window.mainloop()
