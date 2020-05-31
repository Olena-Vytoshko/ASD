def getInteger(message, predicate):
    number = 0
    while(True):
        number = input(message)
        try:
            number = int(number)
        except:
            print("Error with number, try again")
            continue
        if predicate(number) == False:
             print("Error with number, try again")
             continue
        break
    return number


def getMatrix(count):
    matrix = [[0 for x in range(count)] for y in range(count)] 
    for i in range(count):
        for j in range(i + 1, count):
            matrix[i][j] = matrix[j][i] = getInteger("Write length between {first} and {second}\n".format(first = i + 1, second = j + 1), (lambda x: x > 0))
    for i in range(count):
        matrix[i][i] = -1
    return matrix

def isSafe(path, vertex):
    if (vertex in path) or (vertex == 2 and (not 1 in path)):
        return False
    return True
        
def salesmanTask(indx, path):
    if indx == count - 1:
        allPaths.append(path)
        return
    for i in range(1, count):
        if isSafe(path, i):
            copyPath = path.copy()
            copyPath.append(i)
            salesmanTask(indx + 1, copyPath)

def getLength(path):
    length = 0
    for i in range(len(path) - 1):
        length += matrix[path[i]][path[i+1]]
    return length

def print_path(path, length):
    print("[", end = ' ')
    for i in path:
        print(i + 1, end = ' ')
    print("]", end = ' ')
    print("length =", length)

allPaths = []
count = getInteger("Input count of vertex. Must be more then 3\n", (lambda x: x > 3))
matrix = getMatrix(count)
salesmanTask(0, [0])
lengths = []
print("\nAll paths:")
for l in allPaths:
    l.append(0)
    pathLen = getLength(l)
    lengths.append(pathLen)
    print_path(l, pathLen)

print("\nPath(s) with min length:")
minPath = min(lengths)
for i in range(len(lengths)):
    if lengths[i] == minPath:
        print_path(allPaths[i], minPath)






