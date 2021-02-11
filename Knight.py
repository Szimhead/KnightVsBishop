import numpy


class Knight:
    def __init__(self):
        self.pos = [0, 0]
        self.neighbours = []
        self.obstacles = []
        self.steps = 0
        
    def knight_move(self, direction, boardSize):
        new_position = numpy.add(self.pos, direction)
        if self.checkIfInBounds(new_position, boardSize):
            return new_position
        else:
            return self.pos

    def fillObstacles(self, bishopRange):
        for field in bishopRange:
            self.obstacles.append(field)

    def findNeighbours(self, boardSize):
        positions = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        for pos in positions:
            if self.checkIfInBounds(pos, boardSize):
                self.neighbours.append(numpy.add(self.pos, pos))

    def checkIfInBounds(self, position, boardSize):
        return 0 <= position[0] < boardSize and 0 <= position[1] < boardSize
