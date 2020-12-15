f = open("2020 advent day 2.txt")
passwords = f.readlines()

finalCount = 0
for x in range(len(passwords)):
    counter = 0
    test1 = passwords[x][1:2].isnumeric()
    if test1:
        firstNum = passwords[x][0:2]
        test = passwords[x][4:5].isnumeric()
        if test:
            secondNum = passwords[x][3:5]
            letter = passwords[x][6:7]
            ending = passwords[x][9:]
        if not test:
            secondNum = passwords[x][3:4]
            letter = passwords[x][5:6]
            ending = passwords[x][8:]
    elif not test1:
        firstNum = passwords[x][0:1]
        test = passwords[x][3:4].isnumeric()
        if test:
            secondNum = passwords[x][2:4]
            letter = passwords[x][5:6]
            ending = passwords[x][8:]
        if not test:
            secondNum = passwords[x][2:3]
            letter = passwords[x][4:5]
            ending = passwords[x][7:]

    if int(secondNum) >= int(len(ending)+1):
        secondNum = firstNum

    if ending[int(firstNum)-1] == letter:
        if ending[int(secondNum)-1] != letter:
            finalCount += 1
    if ending[int(firstNum)-1] != letter:
        if ending[int(secondNum)-1] == letter:
            finalCount += 1

print(finalCount)
