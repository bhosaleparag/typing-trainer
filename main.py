from exit_class import *
from start_window import *


# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title('great typist')
        self.configure(bg="#D3D3D3")
        global button_image_4, button_image_3, button_image_2, button_image_1
        canvas = Canvas(self, bg="#ffffff", height=700, width=1200,
                        bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        button_image_1 = PhotoImage(file="png\\button_1.png")
        button_1 = Button(image=button_image_1,
                          borderwidth=0, highlightthickness=0,
                          command=self.command_start, relief="flat")
        button_1.place(x=739, y=138, width=358, height=77)
        button_image_2 = PhotoImage(file="png\\button_2.png")
        button_2 = Button(image=button_image_2,
                          borderwidth=0, highlightthickness=0,
                          command=self.command_high_score, relief="flat")
        button_2.place(x=662, y=255, width=435, height=75)
        button_image_3 = PhotoImage(file="png\\button_3.png")
        button_3 = Button(image=button_image_3,
                          borderwidth=0, highlightthickness=0,
                          command=self.command_about_us, relief="flat")
        button_3.place(x=662, y=374, width=435, height=76)
        button_image_4 = PhotoImage(file="png\\button_4.png")
        button_4 = Button(image=button_image_4,
                          borderwidth=0, highlightthickness=0,
                          command=self.command_exit, relief="flat")
        button_4.place(x=739, y=489, width=358, height=77)
        self.resizable(False, False)

    def command_start(self):
        window = start_window(self)
        window.grab_set()

    def command_high_score(self):
        pass

    def command_about_us(self):
        pass

    def command_exit(self):
        window = exit_window(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
