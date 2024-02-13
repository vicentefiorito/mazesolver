from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed = None
            ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
    
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
    
    def _break_entrance_and_exit(self):
        # reveals the entrance to the maze
        self._cells[0][0].has_top_wall = False
        # redraws the cell withouth the top wall
        self._draw_cell(0,0)
        # reveals the exit to the maze
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        # redraws the cell
        self._draw_cell(self._num_cols - 1,self._num_rows - 1)
    
    # DFS method that breaks down the cell's walls
    def _break_walls_r(self,i,j):
        # marks the current cell as visited
        self._cells[i][j].visited = True
        # infinte loop
        while True:
            next_to_visit = []

            # determine which cell to visit next
            # going left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_to_visit.append((i-1,j))
            # going right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_to_visit.append((i+1,j))
            # going up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_to_visit.append((i,j-1))
            # going down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_to_visit.append((i,j+1))
            
            # if there are no directions to move to
            if len(next_to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            # picking a random direction
            random_index = random.randrange(len(next_to_visit))
            next_index = next_to_visit[random_index]

            # breaking down the walls
            # right wall
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            
            # left wall
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            
            # top wall
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            # bottom wall
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            # recursively call the function
            self._break_walls_r(next_index[0],next_index[1])