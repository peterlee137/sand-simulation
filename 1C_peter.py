import random,copy,time
world=[[random.randint(0,1) for _ in range(18)] for _ in range(18)]
#world=[[0 for _ in range(18)] for _ in range(18)]
for i in range(18):
    for j in range(18):
        if i==0 or i==17 or j==0 or j == 17:
            world[i][j]=1
tempworld=[]
print(3)

def showworld():
    print("\n\n\n\n\n")
    for i in range(1,17):
        for j in range(1,17):
            if world[i][j]==1:
                print("■",end=" ")
            else:
                #print("□",end=" ")
                print(" ",end=" ")
        print()

def refreshworld():
    global world
    tempworld=copy.deepcopy(world)
    for y in range(16,0,-1):
        for x in range(16,0,-1):
            if tempworld[y][x]==1:
                if world[y+1][x]==0:
                    world[y+1][x]=1
                    world[y][x]=0
                else:
                    rd= not world[y][x+1] and not world[y+1][x+1]
                    ld= not world[y][x-1] and not world[y+1][x-1]
                    if rd and ld:
                        n=random.choice([-1,1])
                        world[y+1][x+n]=1
                        world[y][x]=0
                    elif rd:
                        world[y+1][x+1]=1
                        world[y][x]=0
                    elif ld:
                        world[y+1][x-1]=1
                        world[y][x]=0
while True:
    showworld()
    prevworld=copy.deepcopy(world)
    refreshworld()
    if world==prevworld:
        break
    time.sleep(0.2)