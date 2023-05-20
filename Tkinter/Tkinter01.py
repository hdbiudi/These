from tkinter import *
import tkinter
import PIL.Image

import PIL.ImageTk
import cv2
import numpy as np

window = Tk()
window.title("hello Tkinter")
window.geometry("800x800")
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture("/home/haidang/PycharmProjects/B1812260/file_test/video1.mp4")

canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

canvas = Canvas(window, width=canvas_w, height=canvas_h, bg='red')
canvas.grid(column=0, row=0)

bw = 0


def handleBW():
    global bw
    bw = 1 - bw


def close():
    global window
    window.destroy()


button = Button(window, text="Black & White", command=handleBW)
button.grid(column=0, row=1)
# button.pack()

photo = None




def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])


def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0, 0, 255), -1)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255, 0, 0), thickness=2)
    return frame

def detection(frame):
    points = []
    while True:
        ret, frame = video.read()
        if not ret:
            break
        # Ve ploygon
        frame = cv2.resize(frame, (576, 320))
        frame = draw_polygon(frame, points)
        key = cv2.waitKey(int(1000 / 60))
        if key & 0xFF == ord('q'):
            break
        elif key == ord('d'):
            points.append(points[0])
            detect = True
        # Hien anh ra man hinh
        image = cv2.imshow("cam", frame)
        image = cv2.setMouseCallback("cam", handle_left_click, points)
    return image


def update_frame():
    points = []
    global canvas, photo, bw
    # doc tu camera
    ret, frame = video.read()
    # Ressize
    frame = cv2.resize(frame, dsize=None, fx=1, fy=1)
    # frame = detection(frame)

    # chuyen he mau
    if bw == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Convert thanh image TK
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # show
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    # cv2.setMouseCallback("hello Tkinter", handle_left_click, points)
    window.after(15, update_frame)
    # Bind the protocol inside the update_frame function
    window.protocol("WM_DELETE_WINDOW", close)


update_frame()
window.mainloop()
