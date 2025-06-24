import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height)) #set screen display
screen.fill((255, 255, 255))
pygame.display.set_caption('Hello Button')

text_colour = (0, 0, 0)
buttom_colour = (0, 255, 0)
button_over_colour = (255, 0, 0)

button_width = 100
button_height = 50

# centering the button as per screen size and button size
button_rect = [(screen_width - button_width)/2,
               (screen_height - button_height)/2,
               button_width,
               button_height
               ]

button_font = pygame.font.SysFont('Arial', 20, True)
button_text = button_font.render('Quit', True, text_colour)
screen.fill((100,100,100))


game_over = False
x, y = 0, 0

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN: #button press logic to quit
            x,y = event.pos
            if(button_rect[0] <= x <= button_rect[0] + button_rect[2] and
            button_rect[1] <= y <= button_rect[1] + button_rect[3]):
                game_over = True
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

    if(button_rect[0] <= x <= button_rect[0] + button_rect[2] and
            button_rect[1] <= y <= button_rect[1] + button_rect[3]):
        pygame.draw.rect(screen, button_over_colour, button_rect)
    else:
        pygame.draw.rect(screen, buttom_colour, button_rect)

    screen.blit(button_text,
            (button_rect[0] + (button_width - button_text.get_width())/2,
                (button_rect[1] + (button_height/2 - button_text.get_height()/2))))
    pygame.display.update()


pygame.quit()

