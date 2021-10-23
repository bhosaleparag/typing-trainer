import random
from tkinter import END


class trial2:
    def __init__(self, enter, label, score,  result, main_frame, x, y, y_velocity):
        self.main_frame = main_frame
        self.enter = enter
        self.label = label
        self.x = x
        self.y = y
        self.score = score
        self.result = result
        self.text = main_frame(x, y, text=self.result, font=('Forte 20'))
        self.y_velocity = y_velocity

    def move(self):
        li = ['bank', 'bhosale', 'pranav', 'omkar', 'cloud', 'create', 'asus', 'realme', 'oppo']
        co = self.main_frame.coords(self.text)
        def get_enter(event):
            self.result = self.enter.get()
            self.enter.delete(0, END)

        self.enter.bind("<Return>", get_enter)
        if co[1] >= 576:
            self.y = 5
            self.x = random.randint(30, 900)
            n = random.randint(0, 8)
            self.text = self.main_frame.create_text(2, 2, text=li[n], font=('Forte 20'))
            self.main_frame.coords(self.text, self.x, self.y)
        elif self.main_frame.itemcget(self.text, 'text') == self.result:
            self.main_frame.itemconfigure(self.text, fill='#ffffff')
            self.score += 1
            self.label.config(text=self.score // 500)
        self.main_frame.move(self.text, 0, self.y_velocity)
