from AStar import *
from particle import *
from Map import *
from map_editor import *

def background():
    while True:
        #p.update()
        mp.update()

def get_input(p):
    nxt = input("---> ")
    val = p.move_particle(nxt)
    if nxt == "close" or val == -1: return -1
    else: return 0

# manual setup
r = int(input("rows: "))
c = int(input("cols: "))
h = int(input("height: "))
w = int(input("width: "))
mp = Map(r,c,w,h)

# for tests
# mp = Map(25,25,800,800)

map_editor(mp)
#p = particle(mp,(mp.start[0][0],mp.start[0][1]))

# Threading runs regardless of user input
thrd = threading.Thread(target=background) # Create the thread
thrd.daemon = True # python will shut down the thread when the code end
thrd.start() # start running the thread

# A*
AStar(mp)

# print("\n\n"+"-"*65+"\n---   Type up / down / left / right to move particle around   ---\n"+"-"*65+"\n\n")
#
# while(True):
#     p.update()
#     val = get_input(p)
#     if val == -1:
#         break
#     else:
#         pass
#
# print("End poit reached!\nSelect the maze and press esc to close...\n")
cv2.waitKey(0)
cv2.destroyAllWindows()
