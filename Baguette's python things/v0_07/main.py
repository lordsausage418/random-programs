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

ball = pygame.image.load('ball.png')
#ball is now a photo of a ball

isJump = False
#is the player jumping?
jumpCount = 10
#how much to jump

pygame.init()
#initialize pygame
win = pygame.display.set_mode((500, 500))
#set display resolution

pygame.display.set_caption("test idk")
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

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        #check if the rectangle is off the screen, if not, change 'x'

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel

    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
            #is the spacebar pressed?

    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            #maths
            jumpCount -= 1
            #x=x-1
        else:
            jumpCount = 10
            isJump = False
            #reset the jump variables


    win.fill((0,0,0))
    #fill the screen

    win.blit(ball, (x,y))
    #draw a ball at 'x,y'
    
    pygame.display.update()
    #update the display
pygame.quit()
