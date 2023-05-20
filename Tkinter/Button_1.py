from tkinter import *
from define import *
from app import App
from tkinter import font

window = Tk()
app = App(window)
font_title = font.Font(family="fangsong ti", size=20, weight=font.BOLD)
font_text = font.Font(family="fangsong ti", size=20, weight=font.BOLD)


def show_hello(text=""):
    print(text)


btnHello = Button(window, text='Helllo', font=font_text, padx=30, pady=20, bg=COLOR_YELLOW, activebackground=COLOR_GREEN, fg=COLOR_RED, command=lambda: show_hello(text="hello"))
btnHello.grid(row=0, column=0)

btnPython = Button(window, text='Python', font=font_text, padx=30, pady=20, bg=COLOR_YELLOW, activebackground=COLOR_GREEN, fg=COLOR_RED, command=lambda: show_hello(text="python"))
btnPython.grid(row=0, column=1)

btnTkinter = Button(window, text='Tkinter', font=font_text, padx=30, pady=20, bg=COLOR_YELLOW, activebackground=COLOR_GREEN, fg=COLOR_RED, command=lambda: show_hello(text="Tkinter"))
btnTkinter.grid(row=0, column=2)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
