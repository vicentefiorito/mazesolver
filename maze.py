from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                new_cell = Cell(self._win)
                col_cells.append(new_cell)
            self._cells.append(col_cells)

        # drawing the cell in the matrix
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        # if there is no window
        if self._win is None:
            return
        # calculating the bottom x coordinate
        x1 = self._x1 + i * self._cell_size_x
        # calculating the bottom y coordinate
        y1 = self._y1 + j * self._cell_size_y
        # calculating the top x coordinate
        x2 = x1 + self._cell_size_x
        # calculating the top y coordinate
        y2 = y1 + self._cell_size_y

        # drawing the cell
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

if __name__ == "__main__":
    maze = Maze(0,0,10,10,50,50,None)
    maze._create_cells()