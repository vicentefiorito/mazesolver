from graphics import Window,Line,Point
from cell import Cell


def main():
    win = Window(800, 600)

    # testing cell
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50,50,100,100)

    c1 = Cell(win)
    c1.has_top_wall = False
    c1.has_right_wall = False
    c1.draw(150,150,200,200)

    c2 = Cell(win)
    c2.has_right_wall = False
    c2.draw(250,250,300,300)

    win.wait_for_close()


main()