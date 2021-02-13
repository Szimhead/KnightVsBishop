import numpy

import main
from NextMove import NextMove


class Bishop:
    pos = [0, 0]

    def __init__(self, pos):
        self.pos = pos
        self.range = []

    def fillRange(self):
        self.range = self.findNeighbours(self.pos)

    def nextMove(self, goal):
        move = NextMove()
        self.pos, steps, cost = move.findNext(goal, self, self.pos)
        return steps

    def move(self, direction):
        new_position = numpy.add(self.pos, direction)
        if main.checkIfInBounds(new_position):
            self.pos = new_position

    def findNeighbours(self, position):
        i = position[0]
        j = position[1]

        neighbours = []

        while main.checkIfInBounds([i, j]):
            neighbours.append([i, j])
            i += 1
            j += 1

        i = position[0]
        j = position[1]

        while main.checkIfInBounds([i, j]):
            neighbours.append([i, j])
            i -= 1
            j -= 1

        i = position[0]
        j = position[1]

        while main.checkIfInBounds([i, j]):
            neighbours.append([i, j])
            i -= 1
            j += 1

        i = position[0]
        j = position[1]

        while main.checkIfInBounds([i, j]):
            neighbours.append([i, j])
            i += 1
            j -= 1

        return neighbours

    def findAllNeighbours(self, position):
        return self.findNeighbours(position)
