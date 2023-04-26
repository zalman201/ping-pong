# импортирование модулей
from pygame import *
from random import *
# классы GameSprite и Player
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect() # хитбокс спрайта
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 565:
            self.rect.y += self.speed

class Ball(GameSprite):
    pass
    # def update(self):
    #     speedx = self.speed
    #     speedy = self.speed
    #     self.rect.y += speedx
    #     self.rect.x += speedy
    #     if self.rect.y > 550 or self.rect.y < 0:
    #         speedy *= 1




# описание игровой сцены, флаги состояний игры, надписи
window = display.set_mode((1200,800))
clock = time.Clock()
display.set_caption("Пинг-понг")
background = transform.scale(image.load('oblaka.jpg'), (1200,800))

game = True

font.init()
font = font.Font(None, 35)
lose1 = font.render('COMPUTER LOSER', True, (180, 0, 0))
lose2 = font.render('PLAYER LOSE', True, (180, 0, 0))

mixer.init()
kick = mixer.Sound('fixic.ogg')


# создание игровых спрайтов
racket1 = Player('racket.png', 30, 200, 100, 250, 4)
racket2 = Player('racket.png', 1055, 200, 100, 250, 4)
ball = Ball('pngegg.png', 350, 250, 100, 100, 4)

speed_x = 10
speed_y = 10

# пока игра продолжается
while game:
    window.blit(background, (0,0))
    # Если нажата кнопка "Завершить игру"
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1
        kick.play()


    if ball.rect.y > 700 or ball.rect.y < 0:
        speed_y *= -1
        kick.play()


    #выйгрыш и проигрыш
    if ball.rect.x <= racket1.rect.x:
        window.blit(lose1, (350,250))
    if ball.rect.x >= racket2.rect.x:
        window.blit(lose2, (350,250))

    if racket1.rect.y != ball.rect.y - 50:
        if racket1.rect.y > ball.rect.y - 50:
            racket1.rect.y -= racket1.speed
        if racket1.rect.y < ball.rect.y - 50:
            racket1.rect.y += racket1.speed
    
        

###### Закрыть приложение

### Переместить ракетки
    racket1.update_l()
    racket2.update_r()
    #ball.update()

    racket1.reset()
    racket2.reset()
    ball.reset()

### Обновить спрайты и сцену
    display.update()
    clock.tick(30)






















































































# from pygame import *
# window = display.set_mode((700,500))
# clock = time.Clock()
# display.set_caption("Догонялки")
# background = transform.scale(image.load("background.png"), (700,500))



# game = True
# FPS = 60

# sprite1 = transform.scale(image.load("sprite1.png"), (100,100))
# sprite2 = transform.scale(image.load("sprite2.png"), (100,100))

# x1 = 100
# y1 = 300

# x2 = 300
# y2 = 300

# speed = 10


# while game:
#     window.blit(background,(0, 0))
#     window.blit(sprite1, (x1,y1))
#     window.blit(sprite2, (x2,y2))


#     for e in event.get():
#         if e.type == QUIT:
#             game = False

#     keys_pressed = key.get_pressed()


#     if keys_pressed[K_LEFT] and x1 > 5:
#         x1 -= speed
#     if keys_pressed[K_RIGHT] and x1 < 595:
#         x1 += speed
#     if keys_pressed[K_UP] and y1 > 5:
#         y1 -= speed
#     if keys_pressed[K_DOWN] and y1 < 395:
#         y1 += speed

#     display.update()
#     clock.tick(FPS)


# #создай окно игры

# #задай фон сцены

# #создай 2 спрайта и размести их на сцене

# #обработай событие «клик по кнопке "Закрыть окно"»