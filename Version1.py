mymap = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
width = 3
height = 3


def victory():
    flag = True
    for i in range(height):
        for j in range(width):
            if mymap[i][j] != target[i][j]:
                flag = False
    return flag


def printmap():
    for i in range(height):
        for j in range(width):
            print("+-----", end="")
        print("+")
        for j in range(width):
            print("|", end="")
            if mymap[i][j] > 0:
                print("{:5d}".format(mymap[i][j]), end="")
            else:
                print("     ", end="")
        print("|")
    for j in range(width):
        print("+-----", end="")
    print("+")


def findzero():
    for i in range(height):
        for j in range(width):
            if mymap[i][j] == 0:
                return i, j


def change(x, y, i, j):
    temp = mymap[i][j]
    mymap[i][j] = mymap[x][y]
    mymap[x][y] = temp


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


while(victory() is False):
    printmap()
    dir = input("Please move!\n")
    move(dir)

printmap()
print("Congratulations!")
