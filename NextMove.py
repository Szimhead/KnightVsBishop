import pygame

from Position import Position
import main


class NextMove:

    def __init__(self):
        self.openList = []
        self.closedList = []

    def findNext(self, current, goal, figure):
        positions = []

        currentPosition = Position(current)
        currentPosition.cost = 0
        self.openList.append(currentPosition)

        goalPosition = Position(goal)

        step = 0
        while self.openList is not [] and goal not in positions:
            print(str(step))
            step += 1
            for p in self.openList:
                print(p.position)
            print()
            minCost = self.openList[0].cost
            cheapestPos = self.openList[0]
            for position in self.openList:
                if position.cost < minCost:
                    minCost = position.cost
                    cheapestPos = position

            self.openList.remove(cheapestPos)
            self.closedList.append(cheapestPos)

            neighbours = figure.findNeighbours(cheapestPos.position)

            for neighbour in neighbours:
                newPos = Position((neighbour[1], neighbour[1]))
                newPos.parent = currentPosition
                newPos.calculateCost(newPos.parent.cost, goal)
                self.openList.append(newPos)
                positions.append(newPos.position)

        if goalPosition in self.openList:
            position = goalPosition.parent
            while position is not currentPosition:
                pygame.draw.line(main.WIN, main.GREEN, position.position, position.parent.position, 3)
                pygame.display.update()



