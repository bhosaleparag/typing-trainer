from tkinter import *
class exit_window(Toplevel):
        def __init__(self, parent):
                super().__init__(parent)
                self.title("you want to exit")
                self.geometry('500x350')
                global me, Button_yes, text_exit
                global Button_no
                me = PhotoImage(file="png\\exit_icon.png")
                label = Label(self, image=me, height=200, width=200)
                label.pack()
                text_exit = PhotoImage(file="png\\text_exit.png")
                label = Label(self, image=text_exit)
                label.pack()
                Button_yes = PhotoImage(file="png\\Button_yes.png")
                yes = Button(self, image=Button_yes, borderwidth=0, highlightthickness=0, command=lambda: exit(), relief="flat")
                yes.place(x=25, y=270)
                Button_no = PhotoImage(file="png\\Button_no.png")
                no = Button(self,image=Button_no, borderwidth=0, highlightthickness=0, command=lambda: self.destroy(), relief="flat")
                no.place(x=300, y=270)
                self.resizable(False, False)

