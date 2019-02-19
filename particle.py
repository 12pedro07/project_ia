from Map import *
import threading

class particle:
    def __init__(self,m,pos):
        self.color = (0,100,0)
        self.border = (0,0,0)
        self.pos = pos # (row , col) in map cell_grid
        self.neighbors = []
        self.map = m

    def move_particle(self,direction):
        self.map.cell_grid[self.pos[0]][self.pos[1]].def_color((140,140,140),(50,50,50))
        coord = [i[0] for i in self.neighbors if i[1] == direction] # find coordinate of the desired movement
        if len(coord) != 0: self.pos = coord[0]
        if self.pos == self.map.end[0]: return -1

    def update(self):
        # updates
        # update color
        self.map.cell_grid[self.pos[0]][self.pos[1]].def_color(self.color,self.border)
        # update image and cells individualy
        self.map.update()
        # update particle neighbors using the specific cell neighbors
        self.neighbors = self.map.cell_grid[self.pos[0]][self.pos[1]].neighbors

        # Debug tool
        # print("\n","#"*30,"\n",self.pos)
        # print(self.neighbors,"\n","#"*30,"\n")
