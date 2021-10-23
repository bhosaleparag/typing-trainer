import tkinter
from PIL import Image, ImageTk, ImageSequence

class gif_move:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=1000, height=1000)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)for img in ImageSequence.Iterator(Image.open(r'png//fast.gif'))]
        self.image = self.canvas.create_image(800,600, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

root = tkinter.Tk()