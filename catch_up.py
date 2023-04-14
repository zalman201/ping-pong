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
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed




# описание игровой сцены, флаги состояний игры, надписи
window = display.set_mode((800,600))
clock = time.Clock()
display.set_caption("Пинг-понг")
background = transform.scale(image.load('oblaka.jpg'), (800,600))

game = True

# создание игровых спрайтов
racket1 = Player('racket.png', 30, 200, 100, 250, 4)
racket2 = Player('racket.png', 700, 200, 100, 250, 4)

# пока игра продолжается
while game:
    window.blit(background, (0,0))
    # Если нажата кнопка "Завершить игру"
    for e in event.get():
         if e.type == QUIT:
            game = False
        

###### Закрыть приложение

### Переместить ракетки
    racket1.update_l()
    racket2.update_r()

    racket1.reset()
    racket2.reset()

### Обновить спрайты и сцену
    display.update()
    clock.tick(40)
