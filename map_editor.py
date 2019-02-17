import cv2
import threading

class edit_tools:
    def __init__(self,mp):
        self.map = mp
        self.click = False
        self.mode = 1
        self.img = mp.img

    def usr_input(self):
        while(self.mode != 0):
            print("#"*61 + "\n### exit (0) / wall (1) / space (2) / start (3) / end (4) ###\n" + "#"*61)
            inp = int(input("option: "))
            self.mode = inp

    def mouse_callback(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.click = True
            edit_cell(self.map,(x,y),self.mode)

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.click == True:
                #print(x,y)
                edit_cell(self.map,(x,y),self.mode) # x = col / y = row

        elif event == cv2.EVENT_LBUTTONUP:
            self.click = False

def edit_cell(mp,coord,mode):
    cell_i = int(coord[1]/mp.altura) # vertical (line)
    cell_j = int(coord[0]/mp.base) # horizontal (col)
    if cell_i >= mp.rows:
        cell_i = mp.rows-1
    elif cell_i < 0:
        cell_i = 0
    if cell_j >= mp.cols:
        cell_j = mp.cols-1
    elif cell_j < 0:
        cell_j = 0
    if mode == 1:
        mp.cell_grid[cell_i][cell_j].def_color((0,0,0),(0,0,0))
    elif mode == 2:
        mp.cell_grid[cell_i][cell_j].def_color((140,140,140),(50,50,50))
    elif mode == 3:
        mp.change_start((cell_i,cell_j))
    elif mode == 4:
        mp.change_end((cell_i,cell_j))
    else:
        print("Error: Invalid mode, please change and try again...\nchose another option: ")
        #print(cell_i,cell_j)

def map_editor(mp):
    mouse = edit_tools(mp)
    cv2.setMouseCallback('image',mouse.mouse_callback)

    # Threading user input
    thrd = threading.Thread(target=mouse.usr_input) # Create the thread
    thrd.daemon = True # python will shut down the thread when the code end
    thrd.start() # start running the thread

    while (mouse.mode != 0):
        mp.update()
    cv2.setMouseCallback('image', lambda *args : None)
