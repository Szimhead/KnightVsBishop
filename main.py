import random

import numpy
import pygame

import Knight

pygame.font.init()

SIZE = 500
FPS = 60

WIN = pygame.display.set_mode((SIZE, SIZE + 50))
pygame.display.set_caption("KnightVsBishop")

BOARD_SIZE = 8
FIELD_SIZE = SIZE // BOARD_SIZE
DIST_FROM_BORDER = FIELD_SIZE // 10 + 2
SQUARE_SIZE = FIELD_SIZE - 2 * DIST_FROM_BORDER
LINE_WIDTH = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 100)
GREEN = (0, 255, 0)

LEFT_UP = (-2, -1)
UP_LEFT = (-1, -2)
RIGHT_UP = (2, -1)
UP_RIGHT = (-1, 2)
LEFT_DOWN = (-2, 1)
DOWN_LEFT = (1, -2)
RIGHT_DOWN = (2, 1)
DOWN_RIGHT = (1, 2)

FIGURE_FONT = pygame.font.SysFont('comicsans', 300 // BOARD_SIZE)


def draw_window(knight_pos, bishop_pos, goal_pos):
    knight = pygame.Rect(knight_pos[0] * FIELD_SIZE + DIST_FROM_BORDER, knight_pos[1] * FIELD_SIZE + DIST_FROM_BORDER,
                         SQUARE_SIZE, SQUARE_SIZE)
    bishop = pygame.Rect(bishop_pos[0] * FIELD_SIZE + DIST_FROM_BORDER, bishop_pos[1] * FIELD_SIZE + DIST_FROM_BORDER,
                         SQUARE_SIZE, SQUARE_SIZE)
    goal = pygame.Rect(goal_pos[0] * FIELD_SIZE + DIST_FROM_BORDER, goal_pos[1] * FIELD_SIZE + DIST_FROM_BORDER,
                       SQUARE_SIZE, SQUARE_SIZE)

    knight_text = FIGURE_FONT.render("K", 1, BLACK)
    bishop_text = FIGURE_FONT.render("B", 1, BLACK)

    WIN.fill(DARK_BLUE)

    for i in range(BOARD_SIZE):
        pygame.draw.line(WIN, WHITE, (i * FIELD_SIZE + (SIZE % BOARD_SIZE) // BOARD_SIZE, 0),
                         (i * FIELD_SIZE + (SIZE % BOARD_SIZE) // BOARD_SIZE, SIZE), LINE_WIDTH)
        pygame.draw.line(WIN, WHITE, (0, i * FIELD_SIZE + (SIZE % BOARD_SIZE) // BOARD_SIZE),
                         (SIZE, i * FIELD_SIZE + (SIZE % BOARD_SIZE) // BOARD_SIZE), LINE_WIDTH)

    pygame.draw.line(WIN, WHITE, (SIZE - LINE_WIDTH, 0), (SIZE - LINE_WIDTH, SIZE), LINE_WIDTH)
    pygame.draw.line(WIN, WHITE, (0, SIZE - LINE_WIDTH), (SIZE, SIZE - LINE_WIDTH), LINE_WIDTH)

    pygame.draw.rect(WIN, WHITE, knight)
    pygame.draw.ellipse(WIN, WHITE, bishop)
    pygame.draw.rect(WIN, GREEN, goal)

    WIN.blit(knight_text,
             (knight_pos[0] * FIELD_SIZE + 2 * DIST_FROM_BORDER, knight_pos[1] * FIELD_SIZE + 2 * DIST_FROM_BORDER))
    WIN.blit(bishop_text,
             (FIELD_SIZE * bishop_pos[0] + 2 * DIST_FROM_BORDER, FIELD_SIZE * bishop_pos[1] + 2 * DIST_FROM_BORDER))

    pygame.display.update()


def knight_move(knight_pos, direction):
    new_position = numpy.add(knight_pos, direction)
    if 0 <= new_position[0] < BOARD_SIZE and 0 <= new_position[1] < BOARD_SIZE:
        return new_position
    else:
        return knight_pos


def checkIfInBounds(position):
    return 0 <= position[0] < BOARD_SIZE and 0 <= position[1] < BOARD_SIZE


def main():
    run = True
    clock = pygame.time.Clock()

    directions = (LEFT_UP, UP_LEFT, RIGHT_UP, UP_RIGHT, LEFT_DOWN, DOWN_LEFT, RIGHT_DOWN, DOWN_RIGHT)

    knight_pos = [0, 0]
    bishop_pos = [5, 1]
    goal_pos = [6, 1]

    display_pause = False

    knight = Knight.Knight()
    print(knight.findNeighbours(knight.pos))

    while run:
        clock.tick(FPS)

        if not display_pause:
            draw_window(knight_pos, bishop_pos, goal_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bishop_pos[1] += 1
                if event.key == pygame.K_UP:
                    bishop_pos[1] -= 1
                if event.key == pygame.K_LEFT:
                    bishop_pos[0] -= 1
                if event.key == pygame.K_RIGHT:
                    bishop_pos[0] += 1
                if event.key == pygame.K_s:
                    knight_pos[1] += 1
                if event.key == pygame.K_w:
                    knight_pos[1] -= 1
                if event.key == pygame.K_a:
                    knight_pos[0] -= 1
                if event.key == pygame.K_d:
                    knight_pos[0] += 1

                if event.key == pygame.K_SPACE:
                    rand = random.randrange(0, 8)
                    print("direction " + str(directions[rand]))
                    knight_pos = knight_move(knight_pos, directions[rand])
                    print(knight_pos)
                    knight.knight_move(directions[rand])

                if event.key == pygame.K_z:
                    display_pause = not display_pause

                if event.key == pygame.K_x:
                    knight.nextMove(goal_pos)

                print(knight.findNeighbours(knight.pos))


if __name__ == '__main__':
    main()
