import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32) #screen dimensions

spriteBall = pygame.image.load('../Images/football.png')
spriteButterfly = pygame.image.load('../Images/butterfly.png')
spriteButterfly = pygame.transform.scale(spriteButterfly, (32,32)) #resizing using transform.scale

spriteWidth = spriteButterfly.get_width() #to contorl sprite sizes and scaling w.r.t screen
spriteHeight = spriteButterfly.get_height()

pygame.display.set_caption('Hello Resize')
screen.fill((0, 0, 0))
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.blit(spriteButterfly, (screen.get_width()/2 - spriteWidth/2, screen.get_height()/2 - spriteHeight/2))
    pygame.display.update()

pygame.quit()