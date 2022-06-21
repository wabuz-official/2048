import pygame

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

# VARIABLES

icon = pygame.image.load('logo.png')


# - SCREEN

width = 700
height = 600

screen = pygame.display.set_mode((width,height))


# - VISUALS
pygame.display.set_caption("2048")
pygame.display.set_icon(icon)
pygame.display.flip()

grid = pygame.image.load('grid.png')


# FUNCTIONS

def draw(obj,x,y):
    screen.blit(obj,((x-obj.get_width()/2),(y-obj.get_height()/2)))



# INIT

pygame.init()

# LOOP

PRun = True
while PRun:

    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PRun = False

        draw(grid,width/2,height/2)

        pygame.display.update()