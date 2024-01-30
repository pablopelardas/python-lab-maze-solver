from graphics.line import Line
from graphics.point import Point


class Cell():
    def __init__(self,win = None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.walls = [True, True, True, True] # top, right, bottom, left
        self._win = win
        self.visited = False
    def draw(self, x1, y1, x2, y2, color="white"):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.walls[0]:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), color=color)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), color="#1d1d1d")
        if self.walls[1]:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), color=color)
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), color="#1d1d1d")
        if self.walls[2]:
            self._win.draw_line(Line(Point(self._x2, self._y2), Point(self._x1, self._y2)), color=color)
        else:
            self._win.draw_line(Line(Point(self._x2, self._y2), Point(self._x1, self._y2)), color="#1d1d1d")
        if self.walls[3]:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x1, self._y1)), color=color)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x1, self._y1)), color="#1d1d1d")
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "#262626"
        #moving left
        if self._x1 > to_cell._x1:
            self._win.draw_line(Line(Point(x_mid, y_mid), Point(self._x1, y_mid)), color=fill_color)
            self._win.draw_line(Line(Point(to_x_mid, y_mid), Point(to_cell._x2, y_mid)), color=fill_color)
        #moving right
        elif self._x1 < to_cell._x1:
            self._win.draw_line(Line(Point(x_mid, y_mid), Point(self._x2, y_mid)), color=fill_color)
            self._win.draw_line(Line(Point(to_x_mid, y_mid), Point(to_cell._x1, y_mid)), color=fill_color)
        #moving up
        elif self._y1 > to_cell._y1:
            self._win.draw_line(Line(Point(x_mid, y_mid), Point(x_mid, self._y1)), color=fill_color)
            self._win.draw_line(Line(Point(x_mid, to_y_mid), Point(x_mid, to_cell._y2)), color=fill_color)
        #moving down
        elif self._y1 < to_cell._y1:
            self._win.draw_line(Line(Point(x_mid, y_mid), Point(x_mid, self._y2)), color=fill_color)
            self._win.draw_line(Line(Point(x_mid, to_y_mid), Point(x_mid, to_cell._y1)), color=fill_color)