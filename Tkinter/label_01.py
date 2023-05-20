from tkinter import *
from define import *
from app import App
from tkinter import font

window = Tk()
app = App(window)
font_title = font.Font(family="fangsong ti", size=20, weight=font.BOLD)
font_text = font.Font(family="fangsong ti", size=20)

# label pack() palce() grid()
label_NW = Label(window, text='NW', font=font_title, background=COLOR_BLUE, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_WN.place(relx=0, rely=0, anchor=NW)
label_NW.grid(row=0, column=0, sticky=NW)

label_N = Label(window, text='N', font=font_title, background=COLOR_RED, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_python.place(relx=0.5, rely=0, anchor=N)
label_N.grid(row=0, column=1, sticky=N)

label_NE = Label(window, text='NE', font=font_title, background=COLOR_GREEN, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_NE.place(relx=1, rely=0, anchor=NE)
label_NE.grid(row=0, column=2, sticky=NE)

label_W = Label(window, text='W', font=font_title, background=COLOR_PURPLE, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_W.place(relx=0, rely=0.5, anchor=W)
label_W.grid(row=1, column=0, sticky=W)

label_Center = Label(window, text='Center', font=font_title, background=COLOR_YELLOW, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_Tkinter.pack(side=BOTTOM, anchor=SE)
# label_Tkinter.place(relx=0.5, rely=0.5, anchor=CENTER)
label_Center.grid(row=1, column=1)

label_E = Label(window, text='E', font=font_title, background=COLOR_BLACK, fg=COLOR_WHITE, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_E.place(relx=1, rely=0.5, anchor=E)
label_E.grid(row=1, column=2, sticky=E)

label_SW = Label(window, text='SW', font=font_title, background=COLOR_RED, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_SW.place(relx=0, rely=1, anchor=SW)
label_SW.grid(row=2, column=0, sticky=SW)

label_S = Label(window, text='S', font=font_title, background=COLOR_RED, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_S.place(relx=0.5, rely=1, anchor=S)
label_S.grid(row=2, column=1, sticky=S)

label_SE = Label(window, text='SE', font=font_title, background=COLOR_RED, fg=COLOR_BLACK, width=10, padx=5, pady=5)
# label_python.pack(side=TOP, anchor=NW)  # West (W), North (N), East (E), South (S).
# label_SE.place(relx=1, rely=1, anchor=SE)
label_SE.grid(row=2, column=2, sticky=SE)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(2, weight=1)
window.mainloop()
