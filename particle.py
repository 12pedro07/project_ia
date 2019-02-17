from Map import *
import threading

class particle:
    def __init__(self,m,pos):
        self.color = (0,100,0)
        self.border = (0,0,0)
        self.pos = pos # (row , col) in map cell_grid
        self.neighbors = []
        self.map = m

    def check_neighbors(self):

        ymax = len(self.map.cell_grid)-1
        xmax = len(self.map.cell_grid[0])-1
        #print("*** ymax: ",ymax," / xmax: ",xmax)

        self.neighbors = []
        end = self.map.end[0]

        if (self.pos[0] < ymax and ( self.map.cell_grid[self.pos[0]+1][self.pos[1]].fill != (0,0,0) or (self.pos[0]+1,self.pos[1]) == end)):
            self.neighbors.append( ((self.pos[0]+1,self.pos[1]),"down"  ) )
        if (self.pos[0] > 0    and ( self.map.cell_grid[self.pos[0]-1][self.pos[1]].fill != (0,0,0) or (self.pos[0]-1,self.pos[1]) == end)):
            self.neighbors.append( ((self.pos[0]-1,self.pos[1]),"up"    ) )
        if (self.pos[1] < xmax and ( self.map.cell_grid[self.pos[0]][self.pos[1]+1].fill != (0,0,0) or (self.pos[0],self.pos[1]+1) == end)):
            self.neighbors.append( ((self.pos[0],self.pos[1]+1),"right" ) )
        if (self.pos[1] > 0    and ( self.map.cell_grid[self.pos[0]][self.pos[1]-1].fill != (0,0,0) or (self.pos[0],self.pos[1]-1) == end)):
            self.neighbors.append( ((self.pos[0],self.pos[1]-1),"left"  ) )

        # Debug tool
        # print("\n","#"*30,"\n",self.pos)
        # print(self.neighbors,"\n","#"*30,"\n")

    def move_particle(self,direction):
        self.map.cell_grid[self.pos[0]][self.pos[1]].def_color((140,140,140),(50,50,50))
        coord = [i[0] for i in self.neighbors if i[1] == direction] # find coordinate of the desired movement
        if len(coord) != 0: self.pos = coord[0]
        if self.pos == self.map.end[0]: return -1

    def update(self):
        # updates
        self.map.cell_grid[self.pos[0]][self.pos[1]].def_color(self.color,self.border)
        self.map.update()
        self.check_neighbors()
