#/bin/python3
import pygame
#import the pygame library

#--------------VARIABLES----------------
x = 50
#x of the sprite
y = 50
#y of the sprite
width = 40
#width of the sprite
height = 60
#height of the sprite
vel = 5
#idk velocity maybe

pygame.init()
#initialize pygame
win = pygame.display.set_mode((500, 500))
#set display resolution

pygame.display.set_caption("First Game")
#change the title

run = True
#should the loop run?

while run:
    pygame.time.delay(100)
    #set the delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #close the program if the window closes

    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    #draw a rectange on screen win, color is #FF0000, the x and y and width and height

    pygame.display.update()
    #update the display
pygame.quit()
#quit pygame
