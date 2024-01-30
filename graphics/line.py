from tkinter import BOTH

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)
        canvas.pack(fill=BOTH, expand=1)
        
