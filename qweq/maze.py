from pygame import *

mixer.init()

win = display.set_mode((500,500))

back = transform.scale(image.load("background.jpg") , (500,500))
gold = transform.scale(image.load("treasure.png") , (40,40))

class script(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,w , h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
        self.direction =''

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class player(script):
    keys = key.get_pressed()
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 500-60:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-60:
            self.rect.y += self.speed
    def shift(self):
        keys = key.get_pressed()
        while keys[K_LSHIFT]:
            self.speed = 5
        self.speed = 10 
class enemy(script):
    def update(self):
        if self.rect.x <= 251:
            self.direction = 'right'
        if self.rect.x >= 500 - 60:
            self.direction ='left'
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

player1 = player('images.jpg',100,100,10,65,65)
robot = enemy('lsjhfajhdfias.jpg', 250,300,10,65,65)
robot1 = enemy('lsjhfajhdfias.jpg', 123,312,10,65,65)
robot2 = enemy('lsjhfajhdfias.jpg', 253,131,10,65,65)
robot3 = enemy('lsjhfajhdfias.jpg', 212,392,10,65,65)
robot4 = enemy('lsjhfajhdfias.jpg', 172,172,10,65,65)
robot5 = enemy('lsjhfajhdfias.jpg', 421,492,10,65,65)
robot6 = enemy('lsjhfajhdfias.jpg', 221,261,10,65,65)
robot7 = enemy('lsjhfajhdfias.jpg', 271,410,10,65,65)

spryte1 = script('Без названия (5).jpg',50,100,10,50,10)
spryte2 = script('Без названия (5).jpg',80,100,10,10,50)
spryte3 = script('Без названия (5).jpg',51,167,10,82,20)
spryte4 = script('Без названия (5).jpg',72,400,10,20,53)
spryte5 = script('Без названия (5).jpg',340,400,10,123,54)
spryte6 = script('Без названия (5).jpg',301,256,10,121,8)
spryte7 = script('Без названия (5).jpg',172,182,10,43,200)
spryte8 = script('Без названия (5).jpg',450,20,10,43,123)

#делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стени делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаб стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки делаю стенки 

mixer.music.load("killing-z_uki-_oyny.mp3")
mixer.music.play()
war = mixer.Sound("jungles.ogg")
war.play

game = True 

while game:
    win.blit(back,(0,0))
    win.blit(gold,(450,450))
    player1.reset()
    player1.update()
    player1.shift()
    robot.reset()
    robot.update()
    robot1.reset()
    robot2.reset()
    robot3.reset()
    robot4.reset()
    robot5.reset()
    robot6.reset()
    robot7.reset()
    robot1.update()
    robot2.update()
    robot3.update()
    robot4.update()
    robot5.update()
    robot6.update()
    robot7.update()
    spryte1.reset()
    spryte2.reset()
    spryte3.reset()
    spryte4.reset()
    spryte5.reset()
    spryte6.reset()
    spryte7.reset()
    spryte8.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock = time.Clock()
    clock.tick(120)
    display.update()