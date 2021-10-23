from tkinter import *
from trial3 import *
import time

a = Tk()
x1 = 100
global score
score = 1
result = 'parag'
a.geometry('400x400')
label = Label(a, text=score)
label.place(x=230, y=310,  width=50, height=50)
canvas = Canvas(a, width=300, height=300, bg='#ffffff')
canvas.place(x=0, y=0)
enter = Entry(a, bd=0, bg="#FFFFFF", font=('Forte 30'))
enter.place(x=20, y=310, width=200, height=80)
frame1 = trial2(enter, label, score, result, canvas, x1, 10, 1)
while True:
    frame1.move()
    a.update()
    time.sleep(0.006)

a.mainloop()