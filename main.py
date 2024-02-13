from graphics import Window
from maze import Maze


def main():
    # implementing the Maze
    num_cols = 12
    num_rows = 16
    margin = 50
    screen_x = 1500
    screen_y= 800
    cell_x = (screen_x - 2 * margin) / num_cols
    cell_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)
    maze = Maze(margin,margin,num_rows,num_cols,cell_x,cell_y,win)
    solved = maze.solve()
    if solved:
        print("Maze has been solved!")
    else:
        print("Maze cannot be solved!")
    win.wait_for_close()
    
main()