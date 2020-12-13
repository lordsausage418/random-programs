import pygame
#import the pygame library

#--------------VARIABLES----------------
x = 32
#x of the player
y = 398
#y of the player
height = 50
#height of the player
width = 50
#width of the player
vel = 5
#idk velocity maybe?
cactusX = 608
#X of the cactus
cactusY = 416
#Y of the cactus
isJump = False
#is the player jumping
jumpCount = 8
#jump count
score = 0
#set the score
delayTime = 20

pygame.init()
#initialize pygame
mainScreen = pygame.display.set_mode((640, 480))
#set display resolution

pygame.display.set_caption("Jumping Dino")
#change the title

run = True
#should the loop run?

while run:
    pygame.time.delay(delayTime)
    #set the delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #close the program if the window closes

    mainScreen.fill((0,0,0))
    #fill the screen

    pygame.draw.rect(mainScreen, (255,0,0), (x, y, width, height))
    #draw the player

    cactusX = cactusX - 8
    if cactusX <= 0:
        cactusX = 608
        score += 1

    keys = pygame.key.get_pressed()
    #make it simpler to get input

    if keys[pygame.K_SPACE]:
        isJump = True
        #is the spacebar pressed?

    if isJump:
        if jumpCount >= -8:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            #maths
            jumpCount -= 0.5
            #x=x-1
        else:
            jumpCount = 8
            isJump = False
            #reset the jump variables

    if y > 366 and cactusX < 82:
        run = False

    pygame.draw.rect(mainScreen, (0, 200, 0), (cactusX, cactusY, 32, 32))

    if score >= 100:
        print("100!!")
    else:
        delayTime = int(20 - int(score/5))

    pygame.display.update()
    #update the display
print(score)
pygame.quit()
#quit pygame