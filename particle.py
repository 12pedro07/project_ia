from Map import *
import threading

class particle:
    def __init__(self,m,pos):
        self.color = (0,100,0)
        self.border = (0,0,0)
        self.pos = pos # (row , col) in map cell_grid
        self.neighbours = []
        self.map = m

    def move_particle(self,direction):
        self.map.cell_grid[self.pos[0]][self.pos[1]].def_color((140,140,140),(50,50,50))
        coord = [i[0] for i in self.neighbours if i[1] == direction] # find coordinate of the desired movement
        if len(coord) != 0: self.pos = coord[0]
        if self.pos == self.map.end[0]: return -1

    def update(self):
        # updates
        # update color
        self.map.cell_grid[self.pos[0]][self.pos[1]].def_color(self.color,self.border)
        # update image and cells individualy
        self.map.update()
        # update particle neighbours using the specific cell neighbours
        self.neighbours = self.map.check_neighbours(self.pos[0],self.pos[1])

        # Debug tool
        # print("\n","#"*30,"\n",self.pos)
        # print(self.neighbours,"\n","#"*30,"\n")
