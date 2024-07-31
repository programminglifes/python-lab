import tkinter
from tkinter import Canvas, Button, Entry


class Circle:
    x = 0
    y = 0
    raidus = 10
    id = 0
    borderWidth = 2

    def __init__(self, radius: int, borderWidth: int):
        self.radius = radius
        self.borderWidth = borderWidth

    def draw(self, canvas: tkinter.Canvas):
        self.id = canvas.create_oval(
            self.x,
            self.y,
            self.x + (self.radius * 2),
            self.y + (self.radius * 2),
            width=self.borderWidth,
        )
        canvas.pack()

    def update(self, canvas: tkinter.Canvas):
        canvas.delete(self.id)
        self.id = canvas.create_oval(
            self.x,
            self.y,
            self.x + (self.radius * 2),
            self.y + (self.radius * 2),
            width=self.borderWidth,
        )
        canvas.pack()

    def askUpdate(self, canvas: tkinter.Canvas):
        self.x = int(x.get())
        self.y = int(y.get())
        self.radius = int(radius_e.get())
        self.borderWidth = int(border.get())
        self.update(canvas)


tk = tkinter.Tk()

circle = Circle(10, 1)

c = Canvas(tk, width=100, height=100)
c.pack()

radius_e = Entry(tk)
radius_e.pack()

x = Entry(tk)
x.pack()

y = Entry(tk)
y.pack()

border = Entry(tk)
border.pack()

update = Button(tk, text="update", command=lambda: circle.askUpdate(c))
update.pack()

circle.draw(c)

tk.mainloop()
