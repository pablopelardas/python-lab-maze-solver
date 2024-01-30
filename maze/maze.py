import time
import random

from graphics.cell import Cell
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y,  win = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed is not None:
            random.seed(seed)
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self.break_walls()
        self._reset_cells_visited()
    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cells(i, j)
    def _draw_cells(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
        
    def _break_entrance_and_exit(self):
        # Break the entrance and exit
        self._cells[0][0].walls[3] = False
        # Draw
        self._draw_cells(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].walls[2] = False
        self._draw_cells(self._num_cols - 1, self._num_rows - 1)
    def _break_walls_r(self, i, j):
        # recursive break walls method
        self._cells[i][j].visited = True
        while(True):
            possible_directions = []
            # check neighbors, if not visited, add to list
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append(0)
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append(1)
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append(2)
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append(3)
            # if no neighbors, draw and return
            if len(possible_directions) == 0:
                self._draw_cells(i, j)
                return
            # choose random neighbors
            direction = random.choice(possible_directions)
            # break walls
            if direction == 0:
                self._cells[i][j].walls[3] = False
                self._cells[i - 1][j].walls[1] = False
                self._break_walls_r(i - 1, j)
            elif direction == 1:
                self._cells[i][j].walls[1] = False
                self._cells[i + 1][j].walls[3] = False
                self._break_walls_r(i + 1, j)
            elif direction == 2:
                self._cells[i][j].walls[0] = False
                self._cells[i][j - 1].walls[2] = False
                self._break_walls_r(i, j - 1)
            elif direction == 3:
                self._cells[i][j].walls[2] = False
                self._cells[i][j + 1].walls[0] = False
                self._break_walls_r(i, j + 1)

    def break_walls(self):
        self._break_walls_r(0, 0)
        self._animate()

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    def _solve_r(self, i, j):
        self._animate()
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        self._cells[i][j].visited = True

        # MOVE UP
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].walls[0]:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # MOVE RIGHT
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].walls[1]:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # MOVE DOWN
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].walls[2]:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # MOVE LEFT
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].walls[3]:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        return False

    def solve(self):
        return self._solve_r(0,0)