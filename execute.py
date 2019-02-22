from AStar import *
from particle import *
from Map import *
from map_editor import *
import random
import pickle

def get_key():
    key_dict = {177:"downleft",178:"down",179:"downright",180:"left",182:"right",183:"upleft",184:"up",185:"upright"}
    key=cv2.waitKey(0) & 0xFF
    if key in key_dict:
        return key_dict[key]

# background updates
def background():
    while True:
        #p.update()
        mp.update()

# manual setup
option = int(input("1 - load / 2 - new: "))

if option == 1:
    tryagain = True
    while(tryagain == True):
        try:
            myfile = open(filename+".txt",'rb')
            mp = pickle.load(myfile)
            mp.update()
            myfile.close()
            tryagain = False
        except:
            filename = input("file name (or exit to leave): ")
            if (filename == "exit"):
                tryagain = False

elif option == 2:
    r = int(input("rows: "))
    c = int(input("cols: "))
    h = int(input("height: "))
    w = int(input("width: "))
    mp = Map(r,c,w,h)

else:
    mp = Map(25,25,800,800)

if option != 1:
    option = int(input("1 - editor / 2 - random: "))
    if option == 1:
        map_editor(mp)
        tryagain = False
    else:
        for i in range(mp.rows):
            for j in range(mp.cols):
                rnd = random.random()
                if rnd <= 0.3:
                    mp.cell_grid[i][j].def_color((0,0,0),(0,0,0))
        mp.change_start((mp.cell_grid[1][1].mp_i,mp.cell_grid[1][1].mp_j))
        mp.change_end((mp.cell_grid[len(mp.cell_grid)-2][len(mp.cell_grid[0])-2].mp_i,mp.cell_grid[len(mp.cell_grid)-2][len(mp.cell_grid[0])-2].mp_j))
        mp.check_all_neighbours()
        mp.update()

# Threading runs regardless of user input
thrd = threading.Thread(target=background) # Create the thread
thrd.daemon = True # python will shut down the thread when the code end
thrd.start() # start running the thread

# deciding for manual or A*
tryagain = True
while (tryagain == True):
    try:
        option = int(input("1 - Manual mode / 2 - A*: "))
    except:
        continue

    # manual mode
    if option == 1:
        tryagain = False
        print("\n\n"+"-"*50+"\n---   Use the numpad to move particle around   ---\n"+"-"*50+"\n\n")
        p = particle(mp,(mp.start[0][0],mp.start[0][1]))

        while(True):
            p.update()
            nxt = get_key()
            val = p.move_particle(nxt)
            if nxt == "close" or val == -1:
                break
            else:
                pass

        print("End poit reached!\nSelect the maze and press esc to close...\n")

    # A*
    elif option == 2:
        tryagain = False
        AStar(mp)
    else:
        print("invalid option, try again")

cv2.waitKey(0)
cv2.destroyAllWindows()
