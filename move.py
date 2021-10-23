import random
from tkinter import END


class move:
    def __init__(self,  enter, label_score, score, label_level, level, result, main_frame, x, y, y_velocity):
        self.main_frame = main_frame
        self.label_level = label_level
        self.level = level
        self.enter = enter
        self.label_score = label_score
        self.x = x
        self.y = y
        self.score = score
        self.result = result
        self.text = main_frame.create_text(x, y, text=self.result, font=("Arial Rounded MT", 20, 'bold'))
        self.y_velocity = y_velocity

    def move(self):
        li = ['morning', 'afternoon', 'thursday', 'public static', 'material', 'google', 'fortunate',
              'information', 'external', 'sequence',
              'application', 'connection', 'most common', 'saturday', 'interruption', 'information',
              'college', 'permission', 'unfortunately', 'android',
              'caps lock', 'scanner', 'ocean', 'permission', 'documentation', 'unfortunate',
              'misunderstand', 'counselor', 'december', 'multiplication',
              'interrupt', 'dangerous', 'librarian', 'february', 'luckily', 'wonderful', 'wednesday', 'pollution',
              'subtraction', 'aquarium',
              'gigantic', 'tremendous', 'accidentally', 'immediately', 'susceptible', 'tomorrow', 'independent',
              'achievement', 'incidentally', 'transferring',
              'considerate', 'fashionable', 'appreciative', 'determined', 'good nature', 'hyperactive', 'beautiful',
              'overweight', 'persistence', 'entertainment',
              'exclusive', 'delightful', 'enchanting', 'backspace', 'favorite', 'disagree', 'handsome', 'appearance',
              'uncommonly', 'fundamental', 'significant']
        co = self.main_frame.coords(self.text)

        def get_enter(event):
            self.result = self.enter.get()
            self.enter.delete(0, END)

        self.enter.bind("<Return>", get_enter)
        if co[1] >= 580:
            self.y_velocity = 1
            self.x = random.randint(50, 870)
            n = random.randint(0, 70)
            self.text = self.main_frame.create_text(2, 2, text=li[n], font=("Arial Rounded MT", 20, 'bold'))
            self.main_frame.coords(self.text, self.x, self.y)
        elif self.main_frame.itemcget(self.text, 'text') == self.result:
            self.main_frame.itemconfigure(self.text, fill='#ffffff')
            self.score += 1
            self.label_score.config(text=self.score // 290)
            if self.score // 290 == 90:
                self.level = 'hell'
                self.label_level.config(text=self.level)
            elif self.score // 290 == 60:
                self.level = 'high'
                self.label_level.config(text=self.level)
            elif self.score // 290 == 30:
                self.level = 'medium'
                self.label_level.config(text=self.level)
            elif self.score // 290 == 3:
                self.level = 'good'
                self.label_level.config(text=self.level)
        self.main_frame.move(self.text, 0, self.y_velocity)
