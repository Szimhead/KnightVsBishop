
from Position import Position


class NextMove:

    def __init__(self):
        self.openList = []
        self.closedList = []

    def findNext(self, goal, figure, current):
        self.openList = []
        self.closedList = []
        print("looking for a path to goal " + str(goal) + " from " + str(current))
        positions = []

        goalPos = [goal[0], goal[1]]

        cost = 0

        currentPosition = Position(current)
        currentPosition.cost = 0
        self.openList.append(currentPosition)
        positions.append(current)

        step = 0
        while len(self.openList) > 0 and goalPos not in positions:
            # print("step " + str(step))
            minCost = self.openList[0].cost
            cheapestPos = self.openList[0]
            for position in self.openList:
                if position.cost < minCost:
                    minCost = position.cost
                    cheapestPos = position

            self.openList.remove(cheapestPos)
            #positions.remove(cheapestPos.position)
            self.closedList.append(cheapestPos)

            neighbours = figure.findAllNeighbours(cheapestPos.position)

            for neighbour in neighbours:
                a = [neighbour[0], neighbour[1]]
                if a not in positions:
                    newPos = Position(a)
                    newPos.parent = cheapestPos
                    newPos.calculateCost(newPos.parent.cost, goal)
                    self.openList.append(newPos)
                    positions.append(newPos.position)

            step += 1

        if goalPos in positions:

            goalPosition = self.openList[0]
            i = 1
            while goalPosition.position != goalPos:
                goalPosition = self.openList[i]
                i += 1

            steps = []

            while [goalPosition.parent.position[0], goalPosition.parent.position[1]] != [current[0], current[1]]:
                steps.append(goalPosition.position)
                steps.append(goalPosition.parent.position)
                goalPosition = goalPosition.parent
                cost += goalPosition.cost

            steps.append(goalPosition.parent.position)

            return goalPosition.position, steps, cost

        return figure.pos, [], cost




