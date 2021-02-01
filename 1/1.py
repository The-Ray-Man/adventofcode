

with open("./1/input.txt", "r") as f:
    values =  [int(i) for i in f.read().split("\n")[:-1]]


def part1(values):
    for i in values:
        for j in values:
            if i != j:
                s = i + j
                if s == 2020:
                    return i*j
def part2(values):
    values.sort()

    for c1 in range(0,len(values)):
        for c2 in range(c1,len(values)):
            for c3 in range(c2,len(values)):
                if values[c1] + values[c2] + values[c3] == 2020:
                    return(values[c1]*values[c2]*values[c3])