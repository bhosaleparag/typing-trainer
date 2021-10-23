from tkinter import *
from move import *
import time
class start_window(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        x1 = 10
        global level, score
        score = 1
        level = 'low'
        result = 'wait for second'
        self.geometry("1200x700")
        self.title('infinite typing')
        self.configure(bg="#eaeaea")
        canvas = Canvas(self, bg="#ffffff", height=700, width=1200, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        entry_image_main_frame = PhotoImage(file="png\\main_frame.png")
        canvas.create_image(476, 301.5, image=entry_image_main_frame)
        main_frame = Canvas(self, width=932, height=568, bd=0, bg="#FFFFFF", highlightthickness=0)
        main_frame.place(x=10, y=19)

        label_image = PhotoImage(file="png\\enter text here.png")
        Label(self, image=label_image).place(x=39, y=608, width=157, height=13)
        entry_image = PhotoImage(file="png\\entry.png")
        canvas.create_image(308.5, 648.5, image=entry_image)
        enter = Entry(self, bd=0, font=("Arial Rounded MT", 28, 'bold'), bg="#FFFFFF", highlightthickness=0)
        enter.place(x=17, y=623, width=584, height=57)

        label_image_1 = PhotoImage(file="png\\best score.png")
        Label(self, image=label_image_1).place(x=1018, y=9, width=106, height=12)
        entry_image_best_score = PhotoImage(file="png\\entry_2.png")
        canvas.create_image(1074, 80.5, image=entry_image_best_score)
        entry_best_score = Entry(self,bd=0, bg="#FFFFFF", highlightthickness=0)
        entry_best_score.place(x=974, y=25, width=200, height=119)

        label_image_2 = PhotoImage(file="png\\your current score.png")
        Label(self, image=label_image_2).place(x=975, y=190, width=192, height=12)
        entry_image_your_current_score = PhotoImage(file="png\\entry_2.png")
        canvas.create_image(1074, 258.5, image=entry_image_your_current_score)
        label_score = Label(self, text=score, bd=0, bg="#FFFFFF", font=("Arial Rounded MT", 28, 'bold'), highlightthickness=0)
        label_score.place(x=974, y=202, width=200, height=119)

        label_image_3 = PhotoImage(file="png\\your current speed.png")
        Label(self, image=label_image_3).place(x=975, y=363, width=181, height=13)
        image_your_current_level = PhotoImage(file="png\\entry_2.png")
        canvas.create_image(1074, 436.5, image=image_your_current_level)
        label_level = Label(self, text=level, bd=0, bg="#FFFFFF", font=("Arial Rounded MT", 28, 'bold'),
                                   highlightthickness=0)
        label_level.place(x=974, y=380, width=200, height=119)

        button_image_quit = PhotoImage(file="png\\button_quit.png")
        button_quit = Button(self, image=button_image_quit, borderwidth=0, highlightthickness=0,
                             command=lambda: self.destroy(), relief="flat")
        button_quit.place(x=969, y=554, width=210, height=133)
        button_image_give_up = PhotoImage(file="png\\button_give_up.png")
        button_give_up = Button(self, image=button_image_give_up, borderwidth=0, highlightthickness=0,
                                command=lambda: self.destroy(), relief="flat")
        button_give_up.place(x=647, y=617, width=280, height=69)
        frame1 = move(enter, label_score, score, label_level, level, result, main_frame, x1, 10, 1)
        self.resizable(False, False)
        while True:
            frame1.move()
            time.sleep(0.004)
            self.update()



