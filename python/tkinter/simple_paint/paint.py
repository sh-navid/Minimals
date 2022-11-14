from tkinter import *
from tkinter.colorchooser import askcolor

x, y, color = None, None, "#212121"


def mouse_click(e):
    global x, y
    x, y = e.x, e.y


def mouse_move(e):
    global x, y, c
    canvas.create_line(x, y, e.x, e.y, width=5, fill=color)
    x, y = e.x, e.y


def change_color():
    global color
    color = askcolor()[1]


win = Tk()
win.title("Paint")


btn_new = Button(text="New")
btn_new.grid(row=0, column=0)


btn_color = Button(text="Color", command=change_color)
btn_color.grid(row=0, column=1)


btn_size = Scale(orient=HORIZONTAL,from_=2,to=50)
btn_size.grid(row=0, column=2)


canvas = Canvas(background="white")
canvas.grid(row=1, columnspan=3)


win.bind("<ButtonPress-1>", mouse_click)
win.bind("<B1-Motion>", mouse_move)
win.mainloop()
