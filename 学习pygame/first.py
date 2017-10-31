import sys
import pygame
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, img_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        global points
        self.rect = self.rect.move(self.speed)
        if self.rect.left<0 or self.rect.right>screen.get_width():
            self.speed[0] *= -1
            if self.rect.bottom <= paddle.rect.top+1:
                points += 1
                ball_bounce.play()
        if self.rect.top <= 0:
            self.speed[1] *= -1
            points += 1
            ball_bounce.play()
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, img_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
pygame.mixer.init()
splat = pygame.mixer.Sound("audio\\ball_bounce.wav")
ball_bounce = pygame.mixer.Sound("audio\\balloon_pop.wav")
screen = pygame.display.set_mode([1024, 768])
pygame.display.set_caption('火龙果2')
clock = pygame.time.Clock()
ball_speed = [2, 1]
ball_img = 'img\\dragon (1).ico'
myBall = MyBallClass(ball_img, [50,50], ball_speed)
ballGroup = pygame.sprite.Group(myBall)
paddle_img = 'img\\apple2.jpg'
paddle = MyPaddleClass(paddle_img, [400, 550])
points = 0
font = pygame.font.Font(None, 100)
collide = False #是否相撞
lives = 3
lives_image = pygame.image.load("img\\pig.ico")
gameover = False
while 1:
    clock.tick(150)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        if myBall.rect.bottom <= 551:
            myBall.speed[1] = -abs(myBall.speed[1])
        if (not collide) and (myBall.rect.bottom<=paddle.rect.top+1):
            points += 1
            splat.play()
        collide = True
    else:
        collide = False

    if not gameover:
        myBall.move()
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        score_str = 'Score:' + str(points)
        score_text = font.render(score_str, 1, (0,0,0))
        score_rect = score_text.get_bounding_rect()
        score_width = score_rect.width
        textpos = [screen.get_rect().width-score_width-10, 20]
        screen.blit(score_text, textpos)
        for i in range(lives-1):
            screen.blit(lives_image, [128*i, 0])
        pygame.display.flip()

    if myBall.rect.top >= screen.get_rect().bottom:
        lives -= 1
        if lives == 0:
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(points)
            font1 = pygame.font.Font(None, 70)
            surf1 = font1.render(final_text1, 1, (0,0,0))
            font2 = pygame.font.Font(None, 50)
            surf2 = font2.render(final_text2, 1, (0,0,0))
            screen.blit(surf1, [screen.get_width()/2 - surf1.get_width()/2, 200])
            screen.blit(surf2, [screen.get_width()/2 - surf2.get_width()/2, 300])
            pygame.display.flip()
            gameover = True
        else:
            pygame.time.delay(1000)
            myBall.rect.topleft = [lives*128, 0]