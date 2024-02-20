import pygame
from pygame.locals import *
from sys import exit


pygame.init()

largura = 640
altura = 480

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

velocidade_tanks = 5

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite(self)


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.speed = velocidade_tanks

        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/tank1.png'))
        self.sprites.append(pygame.image.load('sprites/tank2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (64, 32))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (64, 32))

    def atacar(self):
        self.animar = True

    def move_left(self):
        self.rect.x-=self.speed
    def move_right(self):
        self.rect.x+=self.speed
    def move_up(self):
        self.rect.y-=self.speed
    def move_down(self):
        self.rect.y+=self.speed

image_fundo = pygame.image.load('background.png').convert()
image_fundo = pygame.transform.scale(image_fundo, (largura, altura))

relogio = pygame.time.Clock()
qtd_tanks = 4
vet_tanks = []
todas_as_sprites = pygame.sprite.Group()
i = 0
for i in range(qtd_tanks):
    tank1 = Tank()
    vet_tanks.append(tank1)
    todas_as_sprites.add(tank1)
    if i == 0:
        vet_tanks[i].rect.x = 0
        vet_tanks[i].rect.y = (altura / 2) - ((vet_tanks[i].rect.height) / 2)
    elif i == 1:
        vet_tanks[i].rect.x = largura - vet_tanks[i].rect.width
        vet_tanks[i].rect.y = (altura / 2) - ((vet_tanks[i].rect.height) / 2)
    elif i == 2:
        vet_tanks[i].rect.x = (largura/2) - ((vet_tanks[i].rect.width) / 2)
        vet_tanks[i].rect.y = altura - vet_tanks[i].rect.height
    elif i == 3:
        vet_tanks[i].rect.x = (largura/2) - ((vet_tanks[i].rect.width) / 2)
        vet_tanks[i].rect.y = 0


while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for i in vet_tanks:
        if i.moving_left:
            i.move_left()
        if i.moving_right:
            i.move_right()
        if i.moving_up:
            i.move_up()
        if i.moving_down:
            i.move_down()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        i = 0
        for i in range(len(vet_tanks)):
            if i==0:
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        vet_tanks[0].moving_left = True
                if event.type == KEYUP:
                    if event.key == K_a:
                        vet_tanks[0].moving_left = False

                if event.type == KEYDOWN:
                    if event.key == K_d:
                        vet_tanks[0].moving_right = True
                if event.type == KEYUP:
                    if event.key == K_d:
                        vet_tanks[0].moving_right = False

                if event.type == KEYDOWN:
                    if event.key == K_w:
                        vet_tanks[0].moving_up = True
                if event.type == KEYUP:
                    if event.key == K_w:
                        vet_tanks[0].moving_up = False

                if event.type == KEYDOWN:
                    if event.key == K_s:
                        vet_tanks[0].moving_down = True
                if event.type == KEYUP:
                    if event.key == K_s:
                        vet_tanks[0].moving_down = False
            elif i==1:
                if event.type == KEYDOWN:
                    if event.key == K_j:
                        vet_tanks[1].moving_left = True
                if event.type == KEYUP:
                    if event.key == K_j:
                        vet_tanks[1].moving_left = False

                if event.type == KEYDOWN:
                    if event.key == K_l:
                        vet_tanks[1].moving_right = True
                if event.type == KEYUP:
                    if event.key == K_l:
                        vet_tanks[1].moving_right = False

                if event.type == KEYDOWN:
                    if event.key == K_i:
                        vet_tanks[1].moving_up = True
                if event.type == KEYUP:
                    if event.key == K_i:
                        vet_tanks[1].moving_up = False

                if event.type == KEYDOWN:
                    if event.key == K_k:
                        vet_tanks[1].moving_down = True
                if event.type == KEYUP:
                    if event.key == K_k:
                        vet_tanks[1].moving_down = False
            elif i==2:
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        vet_tanks[2].moving_left = True
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        vet_tanks[2].moving_left = False

                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        vet_tanks[2].moving_right = True
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        vet_tanks[2].moving_right = False

                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        vet_tanks[2].moving_up = True
                if event.type == KEYUP:
                    if event.key == K_UP:
                        vet_tanks[2].moving_up = False

                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        vet_tanks[2].moving_down = True
                if event.type == KEYUP:
                    if event.key == K_DOWN:
                        vet_tanks[2].moving_down = False
            elif i==3:
                if event.type == KEYDOWN:
                    if event.key == K_KP1:
                        vet_tanks[3].moving_left = True
                if event.type == KEYUP:
                    if event.key == K_KP1:
                        vet_tanks[3].moving_left = False

                if event.type == KEYDOWN:
                    if event.key == K_KP3:
                        vet_tanks[3].moving_right = True
                if event.type == KEYUP:
                    if event.key == K_KP3:
                        vet_tanks[3].moving_right = False

                if event.type == KEYDOWN:
                    if event.key == K_KP5:
                        vet_tanks[3].moving_up = True
                if event.type == KEYUP:
                    if event.key == K_KP5:
                        vet_tanks[3].moving_up = False

                if event.type == KEYDOWN:
                    if event.key == K_KP2:
                        vet_tanks[3].moving_down = True
                if event.type == KEYUP:
                    if event.key == K_KP2:
                        vet_tanks[3].moving_down = False

    tela.blit(image_fundo, (0, 0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()