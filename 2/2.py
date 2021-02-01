valid = 0

with open("./2/input.txt", "r") as f:
    values =  [i for i in f.read().split("\n")[:-1]]
    for v in values:
        splitted = v.split(" ")
        minimum = int(splitted[0].split('-')[0]) - 1
        maximum = int(splitted[0].split('-')[1]) - 1
        letter = splitted[1][:-1]
        password = splitted[2]

        # s = sum([letter==n for n in password])
        if (password[minimum] == letter or password[maximum] == letter) and not (password[minimum] == letter and password[maximum] == letter):
            valid += 1

        # print(s)



print(valid)