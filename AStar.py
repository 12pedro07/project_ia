from Map import *
from Cell import *
import math
import cv2
import time

# x = i, y = j

def retracing(startNode,endNode):
    path = []
    current_node = endNode

    while (current_node.id != startNode.id):
        current_node.def_color((255,255,255),(0,0,0))
        path.append(current_node)
        current_node = current_node.parent

    path = path[::-1]

def update_fCost(mp,current_node):
    current_node.f = current_node.g + current_node.h

def node_dist(node1,node2):
    dsti = abs(node1.mp_i - node2.mp_i)
    dstj = abs(node1.mp_j - node2.mp_j)

    if dsti > dstj:
        return 14*dstj + 10*(dsti - dstj)
    return 14*dsti + 10*(dstj - dsti)


def AStar(mp): # map

    mp.cell_grid[mp.start[0][0]][mp.start[0][1]].g = 0
    open_set   = [mp.cell_grid[mp.start[0][0]][mp.start[0][1]]]
    closed_set = []

    # start A* process
    while(len(open_set) > 0):
        current_node = open_set[0]
        for i in range(1,len(open_set)):
            if open_set[i].f < current_node.f or open_set[i].f < current_node.f and open_set[i].h < current_node.h:
                current_node = open_set[i]

        open_set.remove(current_node)
        closed_set.append(current_node)
        if current_node.id == mp.cell_grid[mp.end[0][0]][mp.end[0][1]].id:
            retracing(mp.cell_grid[mp.start[0][0]][mp.start[0][1]],mp.cell_grid[mp.end[0][0]][mp.end[0][1]])
            print("end")
            return

        for neighbour in current_node.neighbours:
            ni = neighbour[0][0]
            nj = neighbour[0][1]
            if mp.cell_grid[ni][nj] in closed_set:
                continue

            newMovCost = current_node.g + node_dist(current_node,mp.cell_grid[ni][nj])

            if newMovCost < mp.cell_grid[ni][nj].g or (mp.cell_grid[ni][nj] not in open_set):
                mp.cell_grid[ni][nj].g = newMovCost
                mp.cell_grid[ni][nj].h = node_dist(mp.cell_grid[ni][nj],mp.cell_grid[mp.end[0][0]][mp.end[0][1]])
                update_fCost(mp,mp.cell_grid[ni][nj])
                mp.cell_grid[ni][nj].parent = current_node
                if mp.cell_grid[ni][nj] not in open_set:
                    open_set.append(mp.cell_grid[ni][nj])

        for node in open_set:
            node.def_color((255,0,0),(0,0,0))
        if len(closed_set) != 0:
            for node in closed_set:
                if node.id != mp.cell_grid[mp.start[0][0]][mp.start[0][1]].id:
                    node.def_color((0,0,255),(0,0,0))
        current_node.def_color((255,255,0),(0,0,0))
        time.sleep(0.01)
        # cv2.waitKey(0)
        if current_node.id != mp.cell_grid[mp.start[0][0]][mp.start[0][1]].id:
            current_node.def_color((0,0,255),(0,0,0))
