

with open("./3/input.txt", "r") as f:
    values =  [i for i in f.read().split("\n")[:-1]]
    print(values)
    maxX = len(values[0])
    maxY = len(values)
    

def find_trees(values,r,d):
    trees = 0
    x = 0
    y = 0
    while True:
        if y < maxY:
            print(values[y][x%maxX])
            if values[y][x%maxX] == "#":
                print("tree")
                trees += 1
            x += r
            y += d
        else:
            return(trees)


print(find_trees(values,1,1)*252*find_trees(values,5,1)*find_trees(values,7,1)*find_trees(values,1,2))