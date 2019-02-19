import cv2

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
        self.prev_fill = (140,140,140)
        self.fill = (140,140,140) # fill color
        self.prev_border = (50,50,50)
        self.border = (50,50,50) # borders color
        # neighbors
        self.neighbors = []

    def def_color(self,new_fill,new_border): # fill and color must be tuples
        if self.fill != new_fill:
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
        # cv2.circle(img,(self.x,self.y), 2, (255,255,255), -1)
        # show all cell id's (debug purposes)
        # self.show_id(img)

    def show_id(self,img):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,str(self.id),self.botton_left, font, 0.5,(255,255,255),1,cv2.LINE_AA)
