from tkinter import *
from tkinter.colorchooser import askcolor

x, y, color, size = None, None, "#212121", 2


def mouse_click(e):
    global x, y
    x, y = e.x, e.y


def mouse_move(e):
    global x, y, c
    canvas.create_line(x, y, e.x, e.y, width=size, fill=color)
    x, y = e.x, e.y


def change_color():
    global color
    color = askcolor()[1]


def change_width(e):
    global size
    size = e


win = Tk()
win.title("Paint")


btn_new = Button(text="New")
btn_new.grid(row=0, column=0)


btn_color = Button(text="Color", command=change_color)
btn_color.grid(row=0, column=2)


scale_size = Scale(orient=HORIZONTAL, from_=2, to=50, command=change_width)
scale_size.grid(row=0, column=1)


canvas = Canvas(background="white")
canvas.grid(row=1, columnspan=3)


canvas.bind("<ButtonPress-1>", mouse_click)
canvas.bind("<B1-Motion>", mouse_move)
win.mainloop()
