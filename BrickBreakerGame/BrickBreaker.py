import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Brick Breaker')

########################################################

#load the assets and convert them for faster loading
bat = pygame.image.load('../Images/paddle.png')
ball = pygame.image.load('../Images/football.png')
brick = pygame.image.load('../Images/brick.png')

bat = bat.convert_alpha()
ball = ball.convert_alpha()
brick = brick.convert_alpha()

bat_rect = bat.get_rect()
ball_rect = ball.get_rect()
brick_rect = brick.get_rect()

########################################################
bat_rect[1] = screen.get_height() - 100
ball_start = (200, 200)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2


for y in range(brick_rows):
    brick_y = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brick_x = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brick_x, brick_y))




clock = pygame.time.Clock()
game_over = False

while not game_over:

    dt = clock.tick(60)
    screen.fill((0, 0, 0))

    for b in bricks:
        screen.blit(brick, b)

    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        ball_served = True


    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and \
        ball_rect[1] + ball_rect.height >= bat_rect[1] and \
        sy >0:
        sy *= -1
        sx *= 1.02 #increase speed/ difficulty
        sy *= 1.02
        continue

    delete_brick = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect[0] <= bx + brick_rect.width and \
            by <= ball_rect[1] <= by + brick_rect.height:
            delete_brick = b

            if ball_rect[0] <= bx + 2:
                sx *= -1
            elif ball_rect[0] >= bx + brick_rect.width-2:
                sx *= -1

            if ball_rect[1] <= by + 2:
                sy *= -1
            elif ball_rect[1] >= by + brick_rect.height - 2:
                sy *= -1

    if delete_brick is not None:
        bricks.remove(delete_brick)

    #top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1


    #bottom
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        #ball_rect[1] = screen.get_height() - ball_rect.height
        #sy *= -1
        ball_served = False
        ball_rect.topleft = ball_start



    #right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    #left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1



    bat_rect[0] = x
    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy




    pygame.display.update()

pygame.quit()