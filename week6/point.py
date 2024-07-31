import tkinter


def draw_point(canvas, x1, y1):
    canvas.create_oval(x1, y1, x1+1, y1+1)
    canvas.pack()


x1 = int(input("Enter x coordinate: "))
y1 = int(input("Enter y coordiante: "))

tk = tkinter.Tk()
tk.title("Point in canvas")

canvas = tkinter.Canvas(tk, width=500, height=500)
canvas.pack()

draw_point(canvas, x1, y1)

tk.mainloop()
