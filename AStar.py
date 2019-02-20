from Map import *
from Cell import *
import math
import cv2
import time

def update_vals(mp,current_cell,flag=""):
    # for simplification purposes
    end_cell = mp.cell_grid[mp.end[0][0]][mp.end[0][1]]

    for node in current_cell.neighbours:

        # update g value
        if (flag == "-A" or flag == "-g"):
            if (len(node[1]) > 5 and mp.cell_grid[node[0][0]][node[0][1]].g > current_cell.g + 14): # if it's a diagonal (based on the size of the word)
                mp.cell_grid[node[0][0]][node[0][1]].g = current_cell.g + 14
            elif(mp.cell_grid[node[0][0]][node[0][1]].g > current_cell.g + 10):
                mp.cell_grid[node[0][0]][node[0][1]].g = current_cell.g + 10
            else:
                pass

        # update h value
        if (flag == "-A" or flag == "-h"):
            mp.cell_grid[node[0][0]][node[0][1]].h = math.sqrt((current_cell.i - end_cell.i)**2 + (current_cell.j - end_cell.j)**2)

        # update f value
        if (flag == "-A" or flag == "-f"):
            mp.cell_grid[node[0][0]][node[0][1]].f = mp.cell_grid[node[0][0]][node[0][1]].g + mp.cell_grid[node[0][0]][node[0][1]].h

def AStar(mp): # map
    finish = False

    mp.cell_grid[mp.start[0][0]][mp.start[0][1]].g = 0
    open_list   = [mp.cell_grid[mp.start[0][0]][mp.start[0][1]]]
    closed_list = []
    # calculate g h and f vals
    update_vals(mp,open_list[0],"-A")
    # start A* process
    while(len(open_list) > 0 or finish == False):
        # find the node with the lower f value and call it "q"
        q = open_list[0]
        for node in open_list:
            if node.f < q.f:
                q = node
        # list management
        open_list.remove(q)
        closed_list.append(q)

        # check if current node is the final node
        if (q.id == mp.cell_grid[mp.end[0][0]][mp.end[0][1]].id):
            print("DONE!")
            break

        for neighbour in q.neighbours:
            if mp.cell_grid[neighbour[0][0]][neighbour[0][1]] in closed_list:
                continue

            # update values
            update_vals(mp,q,"-A")
            if mp.cell_grid[neighbour[0][0]][neighbour[0][1]] not in open_list:
                mp.cell_grid[neighbour[0][0]][neighbour[0][1]].parent = q
                if mp.cell_grid[neighbour[0][0]][neighbour[0][1]] not in open_list:
                    open_list.append(mp.cell_grid[neighbour[0][0]][neighbour[0][1]])

        for node in open_list:
            node.def_color((255,0,0),(0,0,0))
        if len(closed_list) != 0:
            for node in closed_list:
                node.def_color((0,0,255),(0,0,0))
        q.def_color((255,255,0),(0,0,0))
        time.sleep(0.05)
        q.def_color((0,0,255),(0,0,0))

    while(q.parent != None):
        q.def_color((0,255,0),(0,0,0))
        q = q.parent
