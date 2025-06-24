import pygame

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    pygame.display.update()

pygame.quit()