from math import *
import cv2
import numpy as np

class Cell:
    def __init__(self,x,y,base,altura,ID):
        # Caracteristics
        self.id = ID
        self.base = base
        self.altura = altura
        # position
        self.x = int(x)
        self.y = int(y)
        # coordinates
        self.top_left = (int(self.x-self.base/2),int(self.y-self.altura/2))
        self.top_right = (int(self.x+self.base/2),int(self.y-self.altura/2))
        self.botton_right = (int(self.x+self.base/2),int(self.y+self.altura/2))
        self.botton_left = (int(self.x-self.base/2),int(self.y+self.altura/2))
        # colors
        self.fill = (140,140,140) # fill color
        self.border = (50,50,50) # borders color

    def def_color(self,fill,border): # fill and color must be tuples
        self.fill = fill
        self.border = border

    def show_id(self,img):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,str(self.id),self.botton_left, font, 0.5,(255,255,255),1,cv2.LINE_AA)

    def draw_cell(self,img):
        # body
        cv2.rectangle(img,self.top_left,self.botton_right,self.fill,-1)
        # border
        cv2.rectangle(img,self.top_left,self.botton_right,self.border,2)
        # center
        # cv2.circle(img,(self.x,self.y), 2, (255,255,255), -1)
        # show all cell id's (debug purposes)
        # self.show_id(img)

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

        # create a grid of cell objects
        self.cell_grid = [ [] for y in range(self.rows)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cell = Cell(grid[i][j][0],grid[i][j][1],self.base,self.altura,j+i*self.rows)
                self.cell_grid[i].append(cell)

        # define start and end points
        # (row,col,fill,border)
        self.start = ((int(len(self.cell_grid)-1) , int(len(self.cell_grid[0])/2)) , (255,255,0), (50,50,50))
        self.end   = ((0                          , int(len(self.cell_grid[0])/2)) , (0,255,0)  , (50,50,50))
        self.cell_grid[self.start[0][0]][self.start[0][1]].def_color(self.start[1],self.start[2])
        self.cell_grid[self.end[0][0]][self.end[0][1]].def_color(self.end[1],self.end[2])


    def change_start(self,new_start_cell):
        self.cell_grid[self.start[0][0]][self.start[0][1]].def_color((140,140,140),(50,50,50))
        aux_debug = [new_start_cell[0],new_start_cell[1]]
        if new_start_cell[0] >= self.rows:
            aux_debug[0] = self.rows-1
        elif new_start_cell[0] < 0:
            aux_debug[0] = 0
        if new_start_cell[1] >= self.cols:
            aux_debug[1] = self.cols-1
        elif new_start_cell[1] < 0:
            aux_debug[1] = 0

        self.start = ((aux_debug[0],aux_debug[1]) , self.start[1], self.start[2])
        self.cell_grid[self.start[0][0]][self.start[0][1]].def_color(self.start[1],self.start[2])

    def change_end(self,new_end_cell):
        self.cell_grid[self.end[0][0]][self.end[0][1]].def_color((140,140,140),(50,50,50))
        aux_debug = [new_end_cell[0],new_end_cell[1]]
        if new_end_cell[0] >= self.rows:
            aux_debug[0] = self.rows-1
        elif new_end_cell[0] < 0:
            aux_debug[0] = 0
        if new_end_cell[1] >= self.cols:
            aux_debug[1] = self.cols-1
        elif new_end_cell[1] < 0:
            aux_debug[1] = 0

        self.end = ((aux_debug[0],aux_debug[1]) , self.end[1], self.end[2])
        self.cell_grid[self.end[0][0]][self.end[0][1]].def_color(self.end[1],self.end[2])

    def update(self):
        # drawing the grid
        self.img = np.zeros((self.height,self.width,3), np.uint8)
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[i])):
                self.cell_grid[i][j].draw_cell(self.img)
                #cell_grid[i][j].show_id(img)
        cv2.imshow('image',self.img)
        cv2.waitKey(1)
