from Cell import *
from math import *
import cv2
import numpy as np

class Map:

    def __init__(self,rows,cols,width,height): # base / altura = square sizes --- width / height = window sizes

        self.height = height
        self.width  = width
        self.cols   = cols
        self.base   = floor(self.width/self.cols)
        self.rows   = rows
        self.altura = floor(self.height/self.rows)

        # Create a black image
        self.img = np.zeros((self.height,self.width,3), np.uint8)
        cv2.namedWindow('image')

        # create a temp grid with coordinates of the cells
        grid = [ [ [ ((self.base/2)+x*self.base) , ((self.altura/2)+y*self.altura) ] for x in range(self.cols)] for y in range(self.rows)]

        # define start and end points
        # (row,col,fill,border)
        self.start = ((0,0) , (255,255,0), (50,50,50))
        self.end   = ((0,0) , (30,30,135)  , (50,50,50))

        # create a grid of cell objects
        self.cell_grid = [ [] for y in range(self.rows)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cell = Cell(grid[i][j][0],grid[i][j][1],self.base,self.altura,j+i*self.rows)
                self.cell_grid[i].append(cell)

    def change_start(self,new_start_cell):
        # reset the color to the previous one
        self.cell_grid[self.start[0][0]][self.start[0][1]].def_color(self.cell_grid[self.start[0][0]][self.start[0][1]].prev_fill,self.cell_grid[self.start[0][0]][self.start[0][1]].prev_border)
        # reposition the new start point
        self.start = ((new_start_cell[0],new_start_cell[1]) , self.start[1], self.start[2])
        # Atualize the new start colors
        self.cell_grid[self.start[0][0]][self.start[0][1]].def_color(self.start[1],self.start[2])

    def change_end(self,new_end_cell):
        self.cell_grid[self.end[0][0]][self.end[0][1]].def_color(self.cell_grid[self.end[0][0]][self.end[0][1]].prev_fill,self.cell_grid[self.end[0][0]][self.end[0][1]].prev_border)
        self.end = ((new_end_cell[0],new_end_cell[1]) , self.end[1], self.end[2])
        self.cell_grid[self.end[0][0]][self.end[0][1]].def_color(self.end[1],self.end[2])

    def check_neighbors(self,y,x): # y = row / x = col

        ymax = len(self.cell_grid)-1
        xmax = len(self.cell_grid[0])-1
        #print("*** ymax: ",ymax," / xmax: ",xmax)

        neighbors = []
        end = self.end[0]

        # Adjacents
        if (y < ymax):
            if (( self.cell_grid[y+1][x].fill != (0,0,0) or (y+1,x) == end)): neighbors.append(((y+1,x),"down"))
        if (y > 0):
            if (( self.cell_grid[y-1][x].fill != (0,0,0) or (y-1,x) == end)): neighbors.append(((y-1,x),"up"))
        if (x < xmax):
            if (( self.cell_grid[y][x+1].fill != (0,0,0) or (y,x+1) == end)): neighbors.append(((y,x+1),"right"))
        if (x > 0):
            if (( self.cell_grid[y][x-1].fill != (0,0,0) or (y,x-1) == end)): neighbors.append(((y,x-1),"left"))

        # Diagonals
        if (y > 0 and x > 0):
            if (( self.cell_grid[y-1][x-1].fill != (0,0,0) or (y-1,x-1) == end)): neighbors.append(((y-1,x-1),"upleft"))
        if (y > 0 and x < xmax):
            if (( self.cell_grid[y-1][x+1].fill != (0,0,0) or (y-1,x+1) == end)): neighbors.append(((y-1,x+1),"upright"))
        if (y < ymax and x > 0):
            if (( self.cell_grid[y+1][x-1].fill != (0,0,0) or (y+1,x-1) == end)): neighbors.append(((y+1,x-1),"downleft"))
        if (y < ymax and x < xmax):
            if (( self.cell_grid[y+1][x+1].fill != (0,0,0) or (y+1,x+1) == end)): neighbors.append(((y+1,x+1),"downright"))

        return neighbors

    def update(self):
        # drawing the grid
        self.img = np.zeros((self.height,self.width,3), np.uint8)
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[i])):
                self.cell_grid[i][j].draw_cell(self.img)
                self.cell_grid[i][j].neighbors = self.check_neighbors(i,j)
                #cell_grid[i][j].show_id(img)
        cv2.imshow('image',self.img)
        cv2.waitKey(1)
