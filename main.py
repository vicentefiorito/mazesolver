from graphics import Window
from maze import Maze


def main():
    # implementing the Maze
    num_cols = 12
    num_rows = 4
    margin = 50
    cell_x = 100
    cell_y = 300
    screen_x = 1500
    screen_y= 800

    win = Window(screen_x, screen_y)
    maze = Maze(margin,margin,num_rows,num_cols,cell_x,cell_y,win)
    win.wait_for_close()
    
main()