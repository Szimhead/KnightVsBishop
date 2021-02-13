class Position:

    def __init__(self, position):
        self.position = position
        self.parent = None
        self.cost = 0

    def calculateCost(self, costOfGettingHere, goal):
        self.cost = costOfGettingHere + self.manhattanCost(goal)

    def manhattanCost(self, goal):
        return abs(self.position[0] - goal[0]) + abs(self.position[1] - goal[1])
