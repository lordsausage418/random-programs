import pygame
#import the pygame library

#--------------VARIABLES----------------
x = 50
#x of the player
y = 240
#y of the player
height = 50
#height of the player
width = 50
#width of the player
vel = 5
#idk velocity maybe?

isJump = False
#is the player jumping?
jumpCount = 10
#how much to jump
gravity = 5

pygame.init()
#initialize pygame
mainScreen = pygame.display.set_mode((144, 144))
#set display resolution

pygame.display.set_caption("test")
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

    keys = pygame.key.get_pressed()
    #make it simpler to get input

    if keys[pygame.K_SPACE]:
        isJump = True
        jumpCount = 10
        #is the spacebar pressed?

    else:
        y = y + gravity


    if isJump:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            #maths
            jumpCount -= 1
            #x=x-1
        else:
            jumpCount = 10
            isJump = False
            #reset the jump variables



    mainScreen.fill((0,0,0))
    #fill the screen

    pygame.draw.rect(mainScreen, (255,0,0), (x, y, width, height))
    #draw a rectange on screen win, color is #FF0000, the x and y and width and height

    pygame.display.update()
    #update the display
pygame.quit()
#quit pygame

