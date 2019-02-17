from particle import *
from Map import *
from map_editor import *

def background():
    while True:
        #print("update...")
        p.update()

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
map_editor(mp)

# for tests
# mp = Map(5,5,1200,800)
# mouse = mousecoord(mp)
# cv2.setMouseCallback('image',mouse.mouse_callback)

p = particle(mp,(mp.start[0][0],mp.start[0][1]))

# Threading runs regardless of user input
thrd = threading.Thread(target=background) # Create the thread
thrd.daemon = True # python will shut down the thread when the code end
thrd.start() # start running the thread

while(True):
    val = get_input(p)
    if val == -1:
        break
    else:
        pass

print("Closing...\n")
cv2.waitKey(0)
cv2.destroyAllWindows()
