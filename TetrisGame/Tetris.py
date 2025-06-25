import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Tetris Game')
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()