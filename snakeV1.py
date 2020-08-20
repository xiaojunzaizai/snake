import pygame, sys, time, random
from pygame.locals import *

pygame.init()
fpsclock = pygame.time.Clock()
playsurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('Snake')

# color
redcolor = pygame.Color(255,0,0)
blackcolor = pygame.Color(0,0,0)
whitecolor = pygame.Color(255,255,255)
greycolor = pygame.Color(150,150,150)

#initial position
snakeposition = [100,100]
snakeSegments = [[100,100],[80,100],[60,100]]
raspberryposition = [300,300]

raspberrySpawned = 1
direction = 'right'
changeDirection = direction

def gameOver():
    gameOverFont =pygame.font.Font('/Users/xiaojunzai/Google 云端硬盘/snake/FiraCode.ttf',72)
    gameOverSurf = gameOverFont.render('Game Over', True, greycolor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320,10)
    playsurface.blit(gameOverSurf,gameOverRect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))


def quitgame():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quitgame()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection ='up'
            if event.key == K_DOWN or event.key == ord ('s'):
                changeDirection ='down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    if changeDirection == 'right' and not direction =='left':
        direction = changeDirection
    if changeDirection == 'left' and not direction =='right':
        direction = changeDirection
    if changeDirection == 'up' and not direction =='down':
        direction = changeDirection
    if changeDirection == 'down' and not direction =='up':
        direction = changeDirection
    if direction == 'right':
        snakeposition[0] +=20
    if direction == 'left':
        snakeposition[0] -= 20
    if direction == 'up':
        snakeposition[1] -=20
    if direction =='down':
        snakeposition[1] +=20
    snakeSegments.insert(0,list(snakeposition))
    if snakeposition[0]== raspberryposition[0] and snakeposition[1] == raspberryposition[1]:
        raspberrySpawned =0
    else:
        snakeSegments.pop()
    if raspberrySpawned ==0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        raspberryposition = [int(x*20),int(y*20)]
    raspberrySpawned =1
    playsurface.fill(blackcolor)
    for position in snakeSegments:
        pygame.draw.rect(playsurface,whitecolor,Rect(position[0],position[1],20,20))
    pygame.draw.rect(playsurface,redcolor,Rect(raspberryposition[0],raspberryposition[1],20,20))
    pygame.display.flip()
    if snakeposition[0]>620 or snakeposition[0]<0 or snakeposition[1]>460 or snakeposition[1]<0:
        gameOver()
    for snakeBody in snakeSegments[1:]:
        if snakeposition[0] == snakeBody[0] and snakeposition[1] == snakeBody[1]:
            gameOver()
    fpsclock.tick(5)




#测试用
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()