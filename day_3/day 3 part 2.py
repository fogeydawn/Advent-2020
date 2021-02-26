with open('2020 advent day 3.txt', 'r') as f:
    treeMap = f.readlines()


def path_route(angle, speed):
    horizontal = 0
    counter = 0
    slopes = []
    for row in treeMap:
        slopes.append(row.strip())
    for altitude in range(0, len(slopes), speed):
        if horizontal >= len(slopes[altitude]):
            horizontal -= len(slopes[altitude])
        if slopes[altitude][horizontal] == '#':
            counter += 1
        horizontal += angle
    return counter


answer = path_route(1, 1) * path_route(3, 1) * path_route(5, 1) * path_route(7, 1) * path_route(1, 2)
print(answer)
