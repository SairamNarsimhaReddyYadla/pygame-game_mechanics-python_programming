import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32) #screen dimensions

spriteBall = pygame.image.load('../Images/football.png')
spriteButterfly = pygame.image.load('../Images/butterfly.png')
spriteButterfly = pygame.transform.scale(spriteButterfly, (32,32)) #resizing using transform.scale

spriteWidth = spriteButterfly.get_width() #to contorl sprite sizes and scaling w.r.t screen
spriteHeight = spriteButterfly.get_height()

pygame.display.set_caption('Hello Keyboard')
screen.fill((0, 0, 0))
game_over = False

x, y = 0, 0

clock = pygame.time.Clock()


while not game_over:

    dt = clock.tick(60) #to control as per frames by multiplying with the movement speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 *dt
    if pressed[K_DOWN]:
        y += 0.5 *dt
    if pressed[K_LEFT]:
        x -= 0.5 *dt
    if pressed[K_RIGHT]:
        x += 0.5 *dt
    if pressed[K_SPACE]:
        x,y = 0,0

    screen.fill((0, 0, 0))

    screen.blit(spriteButterfly, (x,y))
    pygame.display.update()

pygame.quit()