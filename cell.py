from graphics import Line, Point

class Cell:
    def __init__(self,win=None) :
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    # draws a line onto the canvas
    def draw(self,x1,y1,x2,y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        # if the cell has left wall
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line,"white")
        
        # if cell has top wall
        if self.has_top_wall:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line,"white")
        
        # if cell has right wall
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line,"white")
        
        # if cell has bottom wall
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line,"white")
        
    # draws a path between two cells
    def draw_move(self,to_cell,undo=False):
        if self._win is None:
            return 

        # calculating midpoints
        mid_x = (self._x1 + self._x2) / 2
        mid_y = (self._y1 + self._y2) / 2
        
        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        # moving left 
        if self._x1 > to_cell._x1:
            # draws the line from the left side to the center
            line = Line(Point(self._x1,mid_y),Point(mid_x,mid_y))
            self._win.draw_line(line,fill_color)
            # draws the line to the other cell
            line = Line(Point(to_x,to_y), Point(to_cell._x2,to_y))
            self._win.draw_line(line)
        
        # moving right
        elif self._x1 < to_cell._x1:
            # draws the line from the center of the current cell to the right
            line = Line(Point(mid_x,mid_y), Point(self._x2,mid_y))
            self._win.draw_line(line,fill_color)
            # draw to the line to the other cell
            line = Line(Point(to_cell._x1,to_y), Point(to_x,to_y))
            self._win.draw_line(line,fill_color)
        
        # moving up
        elif self._y1 > to_cell._y1:
            # draws the line from the current cell to the midpoint
            line = Line(Point(mid_x,mid_y), Point(mid_x,self._y1))
            self._win.draw_line(line,fill_color)
            # draws the line from the next cell to the midpoint
            line = Line(Point(to_x,to_cell._y2), Point(to_x,to_y))
            self._win.draw_line(line,fill_color)
        
        # moving down
        elif self._y1 < to_cell._y1:
            # draws the line from the current cell to the midpoint
            line = Line(Point(mid_x,mid_y), Point(mid_x,self._y2))
            self._win.draw_line(line,fill_color)
            # draws the line from the next cell to the midpoint
            line = Line(Point(to_x,to_y), Point(to_x,to_cell._y1))
            self._win.draw_line(line,fill_color)