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
        # ((row,col),fill,border)
        self.start = ((0,0) , (255,255,0), (50,50,50))
        self.end   = ((0,0) , (30,30,135)  , (50,50,50))

        # create a grid of cell objects
        self.cell_grid = [ [] for y in range(self.rows)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cell = Cell(grid[i][j][0],grid[i][j][1],self.base,self.altura,j+i*self.rows,i,j)
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

    def check_all_neighbours(self):
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[i])):
                self.cell_grid[i][j].neighbours = self.check_neighbours(i,j)


    def check_neighbours(self,i,j): # i = row / j = col

        imax = len(self.cell_grid)-1
        jmax = len(self.cell_grid[0])-1
        #print("*** imax: ",imax," / jmax: ",jmax)

        neighbours = []
        end = self.end[0]

        # Adjacents
        if (i < imax):
            if (( self.cell_grid[i+1][j].fill != (0,0,0) or (i+1,j) == end)): neighbours.append(((i+1,j),"down"))
        if (i > 0):
            if (( self.cell_grid[i-1][j].fill != (0,0,0) or (i-1,j) == end)): neighbours.append(((i-1,j),"up"))
        if (j < jmax):
            if (( self.cell_grid[i][j+1].fill != (0,0,0) or (i,j+1) == end)): neighbours.append(((i,j+1),"right"))
        if (j > 0):
            if (( self.cell_grid[i][j-1].fill != (0,0,0) or (i,j-1) == end)): neighbours.append(((i,j-1),"left"))

        # Diagonals
        if (i > 0 and j > 0):
            if (( self.cell_grid[i-1][j-1].fill != (0,0,0) or (i-1,j-1) == end)): neighbours.append(((i-1,j-1),"upleft"))
        if (i > 0 and j < jmax):
            if (( self.cell_grid[i-1][j+1].fill != (0,0,0) or (i-1,j+1) == end)): neighbours.append(((i-1,j+1),"upright"))
        if (i < imax and j > 0):
            if (( self.cell_grid[i+1][j-1].fill != (0,0,0) or (i+1,j-1) == end)): neighbours.append(((i+1,j-1),"downleft"))
        if (i < imax and j < jmax):
            if (( self.cell_grid[i+1][j+1].fill != (0,0,0) or (i+1,j+1) == end)): neighbours.append(((i+1,j+1),"downright"))

        return neighbours

    def update(self):
        # drawing the grid
        self.img = np.zeros((self.height,self.width,3), np.uint8)
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[i])):
                self.cell_grid[i][j].draw_cell(self.img)
                #cell_grid[i][j].show_id(img)
        cv2.imshow('image',self.img)
        cv2.waitKey(1)
