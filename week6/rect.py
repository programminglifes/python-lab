import tkinter
from tkinter import Canvas
#from tkinter import colorchooser
#from tkinter import Button

tk = tkinter.Tk()
tk.title("Making Rectangle")


def draw_rectangle(canvas, x1, y1, x2, y2, color):
    canvas.create_rectangle(10, 10, 50, 50, fill=color)
    canvas.pack()


#def chooseclr():
#    color = colorchooser.askcolor()
#    myCanvas.configure(bg=color[1] or "#fff")


myCanvas = Canvas(tk, height=100, width=100, bg="#fff")
myCanvas.pack()

draw_rectangle(canvas, 10, 10, 60, 60, color="#000")

#bt = Button(tk, text="Choose a color", command=chooseclr)
#bt.pack()

tk.mainloop()
