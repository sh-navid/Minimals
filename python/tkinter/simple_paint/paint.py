from tkinter import *

x, y = None, None


win = Tk()

canvas = Canvas()
canvas.pack()


def mouse_click(e):
    global x, y
    x, y = e.x, e.y


def mouse_move(e):
    global x, y, c
    canvas.create_line(x, y, e.x, e.y, width=5, fill="yellow")
    x, y = e.x, e.y


win.bind("<ButtonPress-1>", mouse_click)
win.bind("<B1-Motion>", mouse_move)
win.mainloop()
