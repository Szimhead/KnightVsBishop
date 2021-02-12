import numpy
import main

from NextMove import NextMove


class Knight:
    def __init__(self):
        self.pos = [0, 0]
        self.neighbours = []
        self.obstacles = []
        self.steps = 0

    def knight_move(self, direction):
        new_position = numpy.add(self.pos, direction)
        if main.checkIfInBounds(new_position):
            self.pos = new_position


    def fillObstacles(self, bishopRange):
        for field in bishopRange:
            self.obstacles.append(field)

    def fillNeighbours(self):
        self.neighbours = self.findNeighbours(self.pos)

    def nextMove(self, goal):
        next = NextMove()
        next.findNext(self.pos, goal, self)

    def findNeighbours(self, position):
        neighbours = []
        positions = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        for pos in positions:
            if main.checkIfInBounds(numpy.add(position,pos)):
                neighbours.append(numpy.add(position, pos))
        return neighbours

