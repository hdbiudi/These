from define import *


class App():
    def __init__(self, window) -> None:
        # thiết lập Wight Height Position
        # .geometry("window wight x window height + position right + position down")
        window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_POSITION_RIGHT, WINDOW_POSITION_DOWN))
        # title
        window.title("Change Color")
        # background
        window.configure(bg='blue')
        window['background'] = COLOR_BACKGROUND
        # window.resizable(False, False)
        window.minsize(400, 100)
