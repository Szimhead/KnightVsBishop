import main


def findNeighbours(position):
    i = position[0]
    j = position[1]

    neighbours = []

    while main.checkIfInBounds((i, j)):
        neighbours.append((i, j))
        i += 1
        j += 1

    i = position[0]
    j = position[1]

    while main.checkIfInBounds((i, j)):
        neighbours.append((i, j))
        i -= 1
        j -= 1

    i = position[0]
    j = position[1]

    while main.checkIfInBounds((i, j)):
        neighbours.append((i, j))
        i -= 1
        j += 1

    i = position[0]
    j = position[1]

    while main.checkIfInBounds((i, j)):
        neighbours.append((i, j))
        i += 1
        j -= 1

    return neighbours


class Bishop:
    pos = [0, 0]

    def __init__(self, pos):
        self.pos = pos
        self.range = []

    def fillRange(self, boardSize):
        self.range = findNeighbours(self.pos)

        print(self.range)
