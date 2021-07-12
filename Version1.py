import random
myMap = [[0] * 10 for i in range(10)]
target = [[0] * 10 for i in range(10)]
width = 3
height = 3
directions = {1: "w", 2: "a", 3: "s", 4: "z"}


def victory():
    flag = True
    for i in range(height):
        for j in range(width):
            if myMap[i][j] != target[i][j]:
                flag = False
    return flag


def getRandomDir():
    i = random.randint(1, 4)
    return directions[i]


def printmap():
    for i in range(height):
        for j in range(width):
            print("+-----", end="")
        print("+")
        for j in range(width):
            print("|", end="")
            if myMap[i][j] > 0:
                print("{:5d}".format(myMap[i][j]), end="")
            else:
                print("     ", end="")
        print("|")
    for j in range(width):
        print("+-----", end="")
    print("+")


def findzero():
    for i in range(height):
        for j in range(width):
            if myMap[i][j] == 0:
                return i, j


def change(x, y, i, j):
    temp = myMap[i][j]
    myMap[i][j] = myMap[x][y]
    myMap[x][y] = temp


def valid(i, j):
    flag = True
    if (i < 0) or (i >= height) or (j < 0) or (j >= width):
        flag = False
    return flag


def move(dir):
    x, y = findzero()
    i = j = -1
    if dir == "w":
        i = x+1
        j = y
    if dir == "a":
        i = x
        j = y+1
    if dir == "s":
        i = x
        j = y-1
    if dir == "z":
        i = x-1
        j = y
    if valid(i, j):
        change(x, y, i, j)


def initialize(times):
    k = 1
    for i in range(height):
        for j in range(width):
            myMap[i][j] = k
            target[i][j] = k
            k = k + 1
    myMap[height-1][width-1] = 0
    target[height-1][width-1] = 0
    for i in range(times):
        dir = getRandomDir()
        move(dir)


order = input("Please enter size of the map! You can choose 2,3,4,5\n")
width = height = int(order)
initialize(500)
while(victory() is False):
    printmap()
    dir = input("Please move!\n")
    move(dir)
printmap()
print("Congratulations!")
