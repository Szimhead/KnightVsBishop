import numpy
import main

from NextMove import NextMove


class Knight:
    def __init__(self):
        self.pos = [0, 6]
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
        neighbours = self.findNeighbours(self.pos)

        check = False
        for n in neighbours:
            print([n[0], n[1]])
            print(goal)
            if goal == [n[0], n[1]]:
                check = True

        if not check:
            paths = []
            move = NextMove()
            for neighbour in neighbours:
                paths.append(move.findNext(goal, self, [neighbour[0], neighbour[1]]) + (neighbour,))

            chosenNeighbour = paths[0][3]
            steps = paths[0][1]
            minCost = paths[0][2]

            for path in paths:
                if path[2] < minCost:
                    chosenNeighbour = path[3]
                    steps = path[1]

            self.pos = chosenNeighbour
            steps.append(steps[len(steps) - 2])
            steps.append(self.pos)
        else:
            self.pos = goal
            steps = []
        return steps

    def findNeighbours(self, position):
        neighbours = []
        positions = ([1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1])
        for pos in positions:
            newPosition = numpy.add(position, pos)
            if main.checkIfInBounds(newPosition) and [newPosition[0], newPosition[1]] not in self.obstacles:
                neighbours.append(numpy.add(position, pos))
        return neighbours

    def findAllNeighbours(self, position):
        neighbours = []
        positions = ([1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1])
        for pos in positions:
            newPosition = numpy.add(position, pos)
            if main.checkIfInBounds(newPosition):
                neighbours.append(newPosition)
        return neighbours
