f = open('2020 advent day 1.txt')
expenseReport = f.readlines()
answers = []

for i in range(len(expenseReport)):
    for k in range(len(expenseReport)):
        if int(expenseReport[i])+int(expenseReport[k]) == 2020:
            answer = int(expenseReport[i])*int(expenseReport[k])
            answers.append(answer)

print(answers)