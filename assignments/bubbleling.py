import tkinter as tk
import time


top = tk.Tk()
C = tk.Canvas(top, bg="blue", height=1024, width=1024)
coord = 10, 50, 110, 150
xdelta = 3
ydelta = 0

character_shape = None

def draw_frame():
    global character_shape

    if character_shape != None:
        top.dele
    character_shape = C.create_arc(coord,
                 start=10, extent=340, fill="red")
    top.move(character_shape, xdelta, ydelta)
    top.after(30, draw_frame)


if __name__ == "__main__":
    draw_frame()
    C.pack()
    top.mainloop()