#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((800, 600))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("background.jpg"), (800, 600))

font.init()
lost = 0
font1 = font.SysFont('Arial', 36)
text_lose = font1.render('Пропущено:' + str(lost), 1, (255, 255, 255))

font.init()
score = 0
font2 = font.SysFont('Arial', 36)
text_win1 = font2.render('Уничтожено:' + str(score), 1, (255, 255, 255))
font.init()
font4 = font.SysFont('Arial', 36)
text_win = font4.render('Победа!', 1 , (255, 255, 0))

font.init()
font4 = font.SysFont('Arial', 36)
text_new = font4.render('Вы разблокировали новое улучшение!', 1 , (255, 255, 0))

font.init()
font4 = font.SysFont('Arial', 80)
text_lose1 = font4.render('Поражение!', 1, (255, 0, 0))






class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(10, 490) 
            self.rect.y = 0
            lost += 1

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 449:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 449:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self):
        pass
player1 = Player('racket.png', 20, 200, 35, 155, 10)
player2 = Player('racket.png', 740, 200, 35, 155, 10)
#ball = Ball('tenis_ball', 350, 200, 30, 30, 7)
finish = False
game = True
text_win = font4.render('Победа!', 1, (255, 255, 0))
clock = time.Clock()
lose = font1.render('Поражение', 1, (255, 255, 255))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

           
               


    if finish != True:
        window.blit(background,(0, 0))
    
    
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
       
    display.update()
    clock.tick(60)