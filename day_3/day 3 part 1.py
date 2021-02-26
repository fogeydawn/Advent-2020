with open('2020 advent day 3.txt', 'r') as f:
    treeMap = f.readlines()

horizontal = 0
counter = 0
for row in treeMap:
    row = row.strip()
    if horizontal >= len(row):
        horizontal -= len(row)
    if row[horizontal] == '#':
        counter += 1
    horizontal += 3
print(counter)


