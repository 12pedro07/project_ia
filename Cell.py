import cv2
import math

class Cell:
    def __init__(self,i,j,base,altura,ID,mp_i = 0,mp_j = 0):
        # Caracteristics
        self.id = ID
        self.base = base
        self.altura = altura
        self.mp_i = mp_i
        self.mp_j = mp_j
        # center coordinates
        self.i = int(i) # vertical pos
        self.j = int(j) # horizontal pos
        # coordinates
        self.top_left = (int(self.i-self.base/2),int(self.j-self.altura/2))
        self.top_right = (int(self.i+self.base/2),int(self.j-self.altura/2))
        self.botton_right = (int(self.i+self.base/2),int(self.j+self.altura/2))
        self.botton_left = (int(self.i-self.base/2),int(self.j+self.altura/2))
        # colors
        self.prev_fill = (140,140,140)
        self.fill = (140,140,140) # fill color
        self.prev_border = (50,50,50)
        self.border = (50,50,50) # borders color
        # neighbours
        self.neighbours = []
        # A* needs
        self.g = math.inf # cost to move from the starting point to a given square on the grid
        self.h = 0 # cost to move from that given square on the grid to the final destination
        self.f = 0 # g + h
        self.parent = None

    def def_color(self,new_fill,new_border): # fill and color must be tuples
        if self.fill != new_fill:
            self.prev_prev_fill = self.prev_fill
            self.prev_fill = self.fill
        self.fill = new_fill
        if self.border != new_border:
            self.prev_border = self.border
        self.border = new_border

    def draw_cell(self,img):
        # body
        cv2.rectangle(img,self.top_left,self.botton_right,self.fill,-1)

        # border
        cv2.rectangle(img,self.top_left,self.botton_right,self.border,2)

        # center
        # cv2.circle(img,(self.i,self.j), 2, (255,255,255), -1)

        # show all cell id's (debug purposes)
        # self.show_id(img)

    def show_id(self,img):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,"f-"+str(self.f),self.botton_left, font, 0.7,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(img,"g-"+str(self.g),(int(self.i-self.base/2),int(self.j+self.altura/2-50)), font, 0.7,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(img,"h-"+str(self.h),(int(self.i-self.base/2),int(self.j+self.altura/2-100)), font, 0.7,(255,255,255),1,cv2.LINE_AA)
