input = [
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0]
]

#  [0,5] [4,6]
#  [1,1] [3,3]
#  [5,2] [6,2]

visited = list()
result = list()

def coordinates(input):
    for i in xrange(len(input)):
        visited.append(list())
        for j in xrange(len(input[i])):
            visited[i].append(0)


    for i in xrange(len(input)):
        for j in xrange(len(input[i])):
            if visited[i][j] == 0:
                visited[i][j] = 1
                if input[i][j] == 1:
                    if not check_collision(i, j):
                        tx,ty = i,j
                        bx,by = detect_square(i, j)
                        result.append([[tx,ty], [bx,by]])

    for item in result:
        print item

def check_collision(i, j):
    for item in result:
        if (item[0][0] <= i <= item[1][0]) and (item[0][1] <= j <= item[1][1]):
            return True
    return False


def detect_square(i, j):
    j1 = j
    dec = False
    for j1 in range(j+1, len(input[i])):
        if visited[i][j1] == 0 and input[i][j1] == 1:
            visited[i][j1] = 1
            continue
        else:
            dec = True
            break
    if dec:
        by = j1-1
    else:
        by = j1

    i1 = i
    dec = False
    for i1 in range(i+1, len(input)):
        if visited[i1][by] == 0 and input[i1][by] == 1:
            visited[i1][by] = 1
            continue
        else:
            dec = True
            break
    if dec:
        bx = i1-1
    else:
        bx = i1
    return bx,by


coordinates(input)