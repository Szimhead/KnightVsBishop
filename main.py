import os
import random

import numpy
import pygame

import Knight
from Bishop import Bishop

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
LIGHT_GREY = (150, 150, 150)
DARK_GREY = (50, 50, 50)
DARK_BLUE = (0, 0, 100)
GREEN = (0, 255, 0)
YELLOW = (200, 150, 0)
LIGHT_YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

LEFT_UP = (-2, -1)
UP_LEFT = (-1, -2)
RIGHT_UP = (2, -1)
UP_RIGHT = (-1, 2)
LEFT_DOWN = (-2, 1)
DOWN_LEFT = (1, -2)
RIGHT_DOWN = (2, 1)
DOWN_RIGHT = (1, 2)

BISHOP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'chess-piece-bishop-queen-knight-chess-8891c80137562be704e3e92a5085ce18.png'))
BISHOP = pygame.transform.scale(
    BISHOP_IMAGE, (FIELD_SIZE - DIST_FROM_BORDER, FIELD_SIZE - DIST_FROM_BORDER))
KNIGHT_IMAGE = pygame.image.load(
    os.path.join('Assets', 't1ilegfv89cm8g2kevbnkb5vm1.png'))
KNIGHT = pygame.transform.scale(
    KNIGHT_IMAGE, (FIELD_SIZE - DIST_FROM_BORDER, FIELD_SIZE - DIST_FROM_BORDER))

FIGURE_FONT = pygame.font.SysFont('comicsans', 300 // BOARD_SIZE)


def draw_window(knight_pos, bishop_black_pos, bishop_white_pos, goal_pos, steps_knight, steps_bishop_black,
                steps_bishop_white):
    goal = pygame.Rect(goal_pos[0] * FIELD_SIZE + DIST_FROM_BORDER, goal_pos[1] * FIELD_SIZE + DIST_FROM_BORDER,
                       SQUARE_SIZE, SQUARE_SIZE)

    WIN.fill(BLACK)

    white = True

    frame = SIZE % BOARD_SIZE // 2

    for i in range(BOARD_SIZE):
        if BOARD_SIZE % 2 == 0:
            white = not white
        for j in range(BOARD_SIZE):
            if white:
                firstColor = YELLOW
            else:
                firstColor = DARK_BLUE
            white = not white
            field = pygame.Rect(frame + i * FIELD_SIZE + (SIZE % BOARD_SIZE) // BOARD_SIZE,
                                frame + j * FIELD_SIZE + (SIZE % BOARD_SIZE) // BOARD_SIZE, FIELD_SIZE, FIELD_SIZE)

            pygame.draw.rect(WIN, firstColor, field)

    pygame.draw.rect(WIN, LIGHT_YELLOW, goal)

    WIN.blit(KNIGHT,
             (knight_pos[0] * FIELD_SIZE, knight_pos[1] * FIELD_SIZE + DIST_FROM_BORDER))
    WIN.blit(BISHOP,
             (FIELD_SIZE * bishop_black_pos[0] + DIST_FROM_BORDER,
              FIELD_SIZE * bishop_black_pos[1] + DIST_FROM_BORDER))
    WIN.blit(BISHOP,
             (FIELD_SIZE * bishop_white_pos[0] + DIST_FROM_BORDER,
              FIELD_SIZE * bishop_white_pos[1] + DIST_FROM_BORDER))

    color = 1

    for i in range(0, len(steps_knight) - 1, 2):
        if color % 2 == 0:
            col = LIGHT_YELLOW
        else:
            col = WHITE
        color += 1
        pygame.draw.line(WIN, col,
                         numpy.add(numpy.multiply(steps_knight[i],
                                                  (FIELD_SIZE, FIELD_SIZE)), (FIELD_SIZE // 2, FIELD_SIZE//2)),
                         numpy.add(numpy.multiply(steps_knight[i + 1],
                                                  (FIELD_SIZE, FIELD_SIZE)), (FIELD_SIZE // 2, FIELD_SIZE//2)), 3)

    for i in range(0, len(steps_bishop_black) - 1, 2):
        if color % 2 == 0:
            col = BLACK
        else:
            col = BLUE
        color += 1
        pygame.draw.line(WIN, col,
                         numpy.add(numpy.multiply(steps_bishop_black[i],
                                                  (FIELD_SIZE, FIELD_SIZE)), (FIELD_SIZE // 2, FIELD_SIZE//2)),
                         numpy.add(numpy.multiply(steps_bishop_black[i + 1],
                                                  (FIELD_SIZE, FIELD_SIZE)), (FIELD_SIZE // 2, FIELD_SIZE//2)), 3)

    for i in range(0, len(steps_bishop_white) - 1, 2):
        if color % 2 == 0:
            col = BLACK
        else:
            col = BLUE
        color += 1
        pygame.draw.line(WIN, col,
                         numpy.add(numpy.multiply(steps_bishop_white[i],
                                                  (FIELD_SIZE, FIELD_SIZE)), (FIELD_SIZE // 2, FIELD_SIZE//2)),
                         numpy.add(numpy.multiply(steps_bishop_white[i + 1],
                                                  (FIELD_SIZE, FIELD_SIZE)), (FIELD_SIZE // 2, FIELD_SIZE//2)), 3)

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

    bishop_black_pos = [5, 2]
    bishop_white_pos = [3, 5]
    goal_pos = [6, 1]

    steps_knight = []
    steps_bishop_black = []
    steps_bishop_white = []

    display_pause = False
    game_over = False

    knight = Knight.Knight()
    bishop_black = Bishop(bishop_black_pos)
    bishop_white = Bishop(bishop_white_pos)

    move = 1

    knight_pos = knight.pos

    while run:
        clock.tick(FPS)

        if not display_pause:
            draw_window(knight_pos, bishop_black_pos, bishop_white_pos, goal_pos, steps_knight, steps_bishop_black,
                        steps_bishop_white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if not game_over:
                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_DOWN:
                    #     bishop_pos[1] += 1
                    # if event.key == pygame.K_UP:
                    #     bishop_pos[1] -= 1
                    # if event.key == pygame.K_LEFT:
                    #     bishop_pos[0] -= 1
                    # if event.key == pygame.K_RIGHT:
                    #     bishop_pos[0] += 1
                    if event.key == pygame.K_s:
                        knight_pos[1] += 1
                        knight.pos[1] += 1
                    if event.key == pygame.K_w:
                        knight_pos[1] -= 1
                        knight.pos[1] -= 1
                    if event.key == pygame.K_a:
                        knight_pos[0] -= 1
                        knight.pos[0] -= 1
                    if event.key == pygame.K_d:
                        knight_pos[0] += 1
                        knight.pos[0] += 1

                    if event.key == pygame.K_SPACE:
                        if move == 1:
                            print("knight move")
                            steps_knight = knight.nextMove(goal_pos)
                            if (knight.pos[0] == goal_pos[0] and knight.pos[1] == goal_pos[1]) or \
                                    (knight.pos[0] == knight_pos[0] and knight.pos[1] == knight_pos[1]):
                                knight_pos = knight.pos
                                game_over = True
                            else:
                                knight_pos = knight.pos
                                print(knight_pos)
                                move = 0
                        elif move == 0:
                            print("black bishop move")
                            steps_bishop_black = bishop_black.nextMove(knight_pos)
                            bishop_black_pos = bishop_black.pos

                            print("white bishop move")
                            steps_bishop_white = bishop_white.nextMove(knight_pos)
                            bishop_white_pos = bishop_white.pos

                            move = 1

                    if event.key == pygame.K_z:
                        display_pause = not display_pause

                    if event.key == pygame.K_x:
                        knight.nextMove(goal_pos)

        bishop_black.fillRange()
        bishop_white.fillRange()

        knight.fillObstacles(bishop_black.range, bishop_white.range)


if __name__ == '__main__':
    main()
