import random,copy,time
sandglass='''11111111111111111
10211111111111201
10211111111111201
10211111111111201
10211111111111201
10020001110002001
10002000000020001
10000200000200001
10000020002000001
10000002020000001
10000020002000001
10000200000200001
10002000000020001
10020000000002001
10200000000000201
10200000000000201
10200000000000201
10200000000000201
11111111111111111'''

world=[]
sandglass=list(sandglass.split("\n"))
for i in sandglass:
    world.append(list(map(int,list(i))))

def showworld():
    print("\n\n\n\n\n")
    for i in range(1,18):
        for j in range(1,16):
            if world[i][j]==1:
                print("■",end=" ")
            elif world[i][j]==2:
                print("□",end=" ")
            else:
                print(" ",end=" ")
        print()

def refreshworld():
    global world
    tempworld=copy.deepcopy(world)
    for y in range(17,0,-1):
        for x in range(15,0,-1):
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

def flip():
    for i in range(9):
        world[i],world[18-i]=world[18-i],world[i]

def run():
    while True:
        showworld()
        prevworld=copy.deepcopy(world)
        refreshworld()
        if world==prevworld:
            break
        time.sleep(0.3)

while True:
    run()
    a=input("\nflip? (y/n): ")
    if a=="y":
        flip()
    else:
        break