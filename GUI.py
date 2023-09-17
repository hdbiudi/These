import tkinter as tk
import cv2
from PIL import Image, ImageTk
import easygui
from Tkinter.define import *
from tkinter import font

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.font_text = font.Font(family="TkDefaultFont", size=13, weight=font.BOLD)
        # Tạo khung video
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Tạo nút mở video
        self.btn_open = tk.Button(window, text="Open", font=self.font_text, width=20, bg=COLOR_GREEN, activebackground=COLOR_RED, command=self.open_video)
        self.btn_open.pack(anchor=tk.CENTER, expand=True)
        # tạo label get ip
        self.entry1 = tk.Entry(window)
        self.canvas.create_window(10, 10, window=self.entry1)

        # Tạo nút thoát
        self.btn_exit = tk.Button(window, text="Exit", font=self.font_text, width=20, bg=COLOR_GREEN, activebackground=COLOR_RED, command=window.quit)
        self.btn_exit.pack(anchor=tk.CENTER, expand=True)
        self.video = None
        self.window.mainloop()

    def open_video(self):
        # Mở tệp video
        filename = easygui.fileopenbox(default='*.mp4', filetypes=['*.mp4'])
        self.video = cv2.VideoCapture(filename)
        # Hiển thị video
        self.show_frame()

    def show_frame(self):
        ret, frame = self.video.read()
        if ret:
            # Chuyển frame ảnh sang định dạng đồ họa để hiển thị trên canvas
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            self.photo = ImageTk.PhotoImage(image=image)

            # Hiển thị frame ảnh trên canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Thực hiện lặp lại việc hiển thị các frame ảnh khác
        self.window.after(15, self.show_frame)


if __name__ == '__main__':
    App(tk.Tk(), "Tkinter Video Player")
