import numpy
import pygame

from Position import Position
import main


class NextMove:

    def __init__(self):
        self.openList = []
        self.closedList = []

    def findNext(self, goal, figure):
        positions = []

        current = figure.pos

        goalPos = (goal[0], goal[1])

        currentPosition = Position(current)
        currentPosition.cost = 0
        self.openList.append(currentPosition)

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
            self.closedList.append(cheapestPos)

            if step == 0:
                neighbours = figure.findNeighbours(cheapestPos.position)
            else:
                neighbours = figure.findAllNeighbours(cheapestPos.position)

            print(neighbours)
            for neighbour in neighbours:
                a = (neighbour[0], neighbour[1])
                if a not in positions:
                    newPos = Position((neighbour[0], neighbour[1]))
                    newPos.parent = cheapestPos
                    newPos.calculateCost(newPos.parent.cost, goal)
                    self.openList.append(newPos)
                    positions.append(newPos.position)

            step += 1

        print("am out")

        if goalPos in positions:
            print("FOUND IT!")

            goalPosition = self.openList[0]
            i = 1
            while goalPosition.position != goalPos:
                goalPosition = self.openList[i]
                i += 1

            print("found goal in open list")

            steps = []

            while goalPosition.parent.position != current:

                steps.append(goalPosition.position)
                steps.append(goalPosition.parent.position)
                pygame.display.update()
                goalPosition = goalPosition.parent

            steps.append(goalPosition.parent.position)

            return goalPosition.position, steps

        return figure.pos, []




