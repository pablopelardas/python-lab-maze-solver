from graphics.windows import Window
from maze.maze import Maze

def main():
    num_rows = 25
    num_cols = 25
    # num_cols = 5
    # num_rows = 5
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    window = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window, 1)
    maze.solve()

    window.wait_for_close()
    print("Window closed")

main()