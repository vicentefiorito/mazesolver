from graphics import Window,Line,Point


def main():
    win = Window(800, 600)
    line1 = Line(Point(50,50),Point(400,400))
    win.draw_line(line1,"black")
    win.wait_for_close()


main()