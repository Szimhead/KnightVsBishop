import numpy
import main

from NextMove import NextMove


class Knight:
    def __init__(self):
        self.pos = [1, 7]
        self.neighbours = []
        self.obstacles = []
        self.steps = 0

    def move(self, direction):
        new_position = numpy.add(self.pos, direction)
        if main.checkIfInBounds(new_position):
            self.pos = new_position

    def fillObstacles(self, bishopBlackRange, bishopWhiteRange):
        self.obstacles = []
        for field in bishopBlackRange:
            self.obstacles.append(field)
        for field in bishopWhiteRange:
            self.obstacles.append(field)

    def fillNeighbours(self):
        self.neighbours = self.findNeighbours(self.pos)

    def nextMove(self, goal):
        move = NextMove()
        self.pos, steps = move.findNext(goal, self)
        return steps

    def findNeighbours(self, position):
        neighbours = []
        positions = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        for pos in positions:
            newPosition = numpy.add(position, pos)
            if main.checkIfInBounds(newPosition) and (newPosition[0], newPosition[1]) not in self.obstacles:
                neighbours.append(numpy.add(position, pos))
        return neighbours

    def findAllNeighbours(self, position):
        neighbours = []
        positions = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        for pos in positions:
            newPosition = numpy.add(position, pos)
            if main.checkIfInBounds(newPosition):
                neighbours.append(numpy.add(position, pos))
        return neighbours
