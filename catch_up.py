# импортирование модулей
from pygame import *
from random import *
# классы GameSprite и Player
class GameSprite(sprite.Sprite):
    pass
class Player(GameSprite):
    pass


# описание игровой сцены, флаги состояний игры, надписи
window = display.set_mode((800,600))
clock = time.Clock()
display.set_caption("Пинг-понг")
background = transform.scale(image.load('oblaka.jpg'), (800,600))

game = True

# создание игровых спрайтов

# пока игра продолжается
while game:
    window.blit(background, (0,0))
    # Если нажата кнопка "Завершить игру"
    for e in event.get():
         if e.type == QUIT:
            game = False
        

###### Закрыть приложение

### Переместить ракетки

### Обновить спрайты и сцену
    display.update()
    clock.tick(40)






















































































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