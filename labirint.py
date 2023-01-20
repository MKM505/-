from pygame import *

win_width = 1200
win_height = 700
display.set_caption('Лабиринт')
window = display.set_mode((1200,700))
win = transform.scale(image.load('pobeda.jpg'), (1200,700))
background = transform.scale(image.load('background.jpg'), (win_width,win_height))
GREEN = (100,67,63)

class GameSprite(sprite.Sprite):
    def __init__(self, picture,w,h,y,x):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w,h,y,x, speed_x, speed_y):
        super().__init__(picture,w,h,y,x)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.speed_x > 0:
            for p in platforms_touched:
                self.right = min(self.right, p.left)
        elif self.speed_x < 0:
            for p in platforms_touched:
                self.left = max(self.left, p.right)
                self.rect.y += self.speed_y
                platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.speed_y > 0:
            for p in platforms_touched:
                self.bottom = min(self.bottom, p.top)
        elif self.speed_y < 0:
            for p in platforms_touched:
                self.top = max(self.bottom, p.top)
    def fire(self):
        bullet = Bullet('fireball.png', 20,20,self.rect.centery ,self.rect.right, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    direction = 'left'
    def __init__(self,picture, w,h,y,x,speed):
        super().__init__(picture, w,h,y,x)
        self.speed = speed
    def update(self):
        if self.rect.x <= 220:
            self.direction = 'right'
        elif self.rect.x >= win_width-500:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self,picture, w,h,y,x,speed):
        super().__init__(picture, w,h,y,x)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()

#?SUIII
#!да окей
#*wasd
#


player = Player('ghost.png',100,100,100,0,0,0)
final = GameSprite('Finish-Banner.png',20, 20, 10, 10)
Pic = GameSprite('default.jpg',150,150,100,500)
Lose = GameSprite('lose.jpg', 200, 200, 500, 950)
monster = Enemy('ghost.png', 150, 150, 350, 250, 15)
finish = False

w1 = GameSprite('wall.jpg', 100,500,0,150)
w2 = GameSprite('wall.jpg', 100,500,200,800)
barriers = sprite.Group()
barriers.add(w1)
barriers.add(w2)

bullets = sprite.Group()

monsters = sprite.Group()
monsters.add(monster)

run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP or e.key == K_w:
                player.speed_y = -10
            elif e.key == K_DOWN or e.key == K_s:
                player.speed_y = 10
            elif e.key == K_LEFT or e.key == K_a:
                player.speed_x = -10
            elif e.key == K_RIGHT or e.key == K_d:
                player.speed_x = 10
            elif e.key == K_SPACE:
                player.fire()

        elif e.type == KEYUP:
            if e.key == K_UP or e.key == K_w:
                player.speed_y = 0
            elif e.key == K_DOWN or e.key == K_s:
                player.speed_y = 0
            elif e.key == K_LEFT or e.key == K_a:
                player.speed_x = 0
            elif e.key == K_RIGHT or e.key == K_d:
                player.speed_x = 0

    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        Pic.reset()
        bullets.update()
        bullets.draw(window)
        monster.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)
        sprite.groupcollide(bullets, monsters, True, False)
        Lose.reset()
        barriers.draw(window)
    display.update()