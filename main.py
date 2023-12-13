import tkinter as tk
from math import sqrt
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def copy(self):
        return Point(self.x, self.y)


def add_point(point, radius=0.5):
    x, y = point.x, point.y
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill='black')


def rand():
    return random.choice((a, b, c))


root = tk.Tk()
root.geometry("512x512")

label = tk.Label(root, text="Sierpinski's Triangle")
label.pack()

canvas = tk.Canvas(root, bg='white', width=512, height=512)
canvas.pack()

a = Point(0, 512)
b = Point(512, 512)
c = Point(256, 512 - (sqrt(3) / 2) * 512)

# canvas.create_line(a.x, a.y, b.x, b.y, fill="black", width=1)
# canvas.create_line(b.x, b.y, c.x, c.y, fill="black", width=1)
# canvas.create_line(c.x, c.y, a.x, a.y, fill="black", width=1)

current = rand()
add_point(current)

CONVERGENCE_SPEED: int = 200 # Recommended range 0-100

for j in range(0, 1000):
    for i in range(0, CONVERGENCE_SPEED):
        current = (current + rand()) / 2
        add_point(current)
    root.update()