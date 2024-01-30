from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.create_canvas()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__running = False

    def create_canvas(self):
        self.canvas = Canvas(self.__root, width=self.__width, height=self.__height, bg="#1d1d1d")
        self.canvas.pack(fill=BOTH, expand=True)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    def close(self):
        self.__running = False

    def draw_line(self, line, color="white"):
        line.draw(self.canvas, color)

