f = open("2020 advent day 2.txt")
passwords = f.readlines()

finalCount = 0
for x in range(len(passwords)):
    counter = 0
    test1 = passwords[x][1:2].isnumeric()
    if test1:
        low = passwords[x][0:2]
        test = passwords[x][4:5].isnumeric()
        if test:
            high = passwords[x][3:5]
            letter = passwords[x][6:7]
            ending = passwords[x][9:]
        if not test:
            high = passwords[x][3:4]
            letter = passwords[x][5:6]
            ending = passwords[x][8:]
    elif not test1:
        low = passwords[x][0:1]
        test = passwords[x][3:4].isnumeric()
        if test:
            high = passwords[x][2:4]
            letter = passwords[x][5:6]
            ending = passwords[x][8:]
        if not test:
            high = passwords[x][2:3]
            letter = passwords[x][4:5]
            ending = passwords[x][7:]
    for i in range(len(ending)):
        if ending[i] == letter:
            counter += 1
    if int(low) <= counter <= int(high):
        finalCount += 1

print(finalCount)
