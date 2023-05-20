from tkinter import *
from define import *
from app import App
from tkinter import font
import random

window = Tk()
app = App(window)
font_title = font.Font(family="fangsong ti", size=13, weight=font.BOLD)
font_text = font.Font(family="fangsong ti", size=20)


def random_color():
    r = lambda: random.randint(0, 225)
    return '#%02X%02X%02X' % (r(), r(), r())


def change_label_color(background):
    label_Hello = Label(window, text='HELLO', font=font_title, background=background, fg=COLOR_BLACK, width=10, padx=30, pady=20)
    label_Hello.grid(row=0, column=0, columnspan=4, sticky="wse")


def create_button(name, background, active_color, index):
    Button(window, text=name, font=font_text, padx=30, pady=20, bg=background, activebackground=active_color, fg=COLOR_BLACK, command=lambda: change_label_color(background)).grid(row=1, column=index, sticky='we', padx=30)


label_Hello = Label(window, text='HELLO', font=font_title, background=random_color(), fg=COLOR_BLACK, width=10, padx=30, pady=20)
label_Hello.grid(row=0, column=0, columnspan=4, sticky="wse")

create_button("Green", COLOR_GREEN, COLOR_WHITE, 0)
create_button("Blue", COLOR_BLUE, COLOR_WHITE, 1)
create_button("Red", COLOR_RED, COLOR_WHITE, 2)
create_button("Yellow", COLOR_YELLOW, COLOR_WHITE, 3)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.mainloop()
