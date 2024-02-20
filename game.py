import pygame
from pygame.locals import *
import os
import obstacles
import bullet
import tank
import sys

pygame.init()

main_menu = True
timer = pygame.time.Clock()
fps = 60

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
menu_screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Tankpygame ta ligado!')
largura = screen_width
altura = screen_height

image_fundo = pygame.image.load('background.png').convert()
image_fundo = pygame.transform.scale(image_fundo, (screen_width, screen_height))
qtd_tanks = 4

vet_tanks = []
ultima_direcao = []
for i in range(qtd_tanks):
    if i == 0:
        ultima_direcao.append(2)
    elif i == 1:
        ultima_direcao.append(1)
    elif i == 2:
        ultima_direcao.append(3)
    else:
        ultima_direcao.append(4)
todas_as_sprites = pygame.sprite.Group()
i = 0
for i in range(qtd_tanks):
    tank1 = tank.Tank(ultima_direcao[i])
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

def start_game():

    global menu_screen
    while True:
        timer.tick(fps)
        menu_screen.fill((255, 255, 255))
        #tela.fill(BRANCO)
        for i in vet_tanks:
            if len(i.bullets) > 0:
                for j in i.bullets:
                    j.moviment()

            if i.moving_left:
                i.move_left()
            if i.moving_right:
                i.move_right()
            if i.moving_up:
                i.move_up()
            if i.moving_down:
                i.move_down()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            for i in range(len(vet_tanks)):
                if i == 0:
                    if event.type == KEYDOWN:
                        if event.key == K_a:
                            vet_tanks[0].moving_left = True
                            vet_tanks[0].direcao = 1
                    if event.type == KEYUP:
                        if event.key == K_a:
                            vet_tanks[0].moving_left = False

                    if event.type == KEYDOWN:
                        if event.key == K_d:
                            vet_tanks[0].moving_right = True
                            vet_tanks[0].direcao = 2
                    if event.type == KEYUP:
                        if event.key == K_d:
                            vet_tanks[0].moving_right = False

                    if event.type == KEYDOWN:
                        if event.key == K_w:
                            vet_tanks[0].moving_up = True
                            vet_tanks[0].direcao = 3
                    if event.type == KEYUP:
                        if event.key == K_w:
                            vet_tanks[0].moving_up = False

                    if event.type == KEYDOWN:
                        if event.key == K_s:
                            vet_tanks[0].moving_down = True
                            vet_tanks[0].direcao = 4
                    if event.type == KEYUP:
                        if event.key == K_s:
                            vet_tanks[0].moving_down = False

                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            vet_tanks[0].atirar(vet_tanks[0].rect.x, vet_tanks[0].rect.y, vet_tanks[0].direcao)
                            ultimo = len(vet_tanks[0].bullets) - 1
                            todas_as_sprites.add(vet_tanks[0].bullets[ultimo])

                elif i == 1:
                    if event.type == KEYDOWN:
                        if event.key == K_j:
                            vet_tanks[1].moving_left = True
                            vet_tanks[1].direcao = 1
                    if event.type == KEYUP:
                        if event.key == K_j:
                            vet_tanks[1].moving_left = False

                    if event.type == KEYDOWN:
                        if event.key == K_l:
                            vet_tanks[1].moving_right = True
                            vet_tanks[1].direcao = 2
                    if event.type == KEYUP:
                        if event.key == K_l:
                            vet_tanks[1].moving_right = False

                    if event.type == KEYDOWN:
                        if event.key == K_i:
                            vet_tanks[1].moving_up = True
                            vet_tanks[1].direcao = 3
                    if event.type == KEYUP:
                        if event.key == K_i:
                            vet_tanks[1].moving_up = False
                    if event.type == KEYDOWN:
                        if event.key == K_k:
                            vet_tanks[1].moving_down = True
                            vet_tanks[1].direcao = 4
                    if event.type == KEYUP:
                        if event.key == K_k:
                            vet_tanks[1].moving_down = False

                    if event.type == KEYDOWN:
                        if event.key == K_o:
                            vet_tanks[1].atirar(vet_tanks[1].rect.x, vet_tanks[1].rect.y, vet_tanks[1].direcao)
                            ultimo = len(vet_tanks[1].bullets) - 1
                            todas_as_sprites.add(vet_tanks[1].bullets[ultimo])
                elif i == 2:
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            vet_tanks[2].moving_left = True
                            vet_tanks[2].direcao = 1
                    if event.type == KEYUP:
                        if event.key == K_LEFT:
                            vet_tanks[2].moving_left = False

                    if event.type == KEYDOWN:
                        if event.key == K_RIGHT:
                            vet_tanks[2].moving_right = True
                            vet_tanks[2].direcao = 2
                    if event.type == KEYUP:
                        if event.key == K_RIGHT:
                            vet_tanks[2].moving_right = False

                    if event.type == KEYDOWN:
                        if event.key == K_UP:
                            vet_tanks[2].moving_up = True
                            vet_tanks[2].direcao = 3
                    if event.type == KEYUP:
                        if event.key == K_UP:
                            vet_tanks[2].moving_up = False

                    if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                            vet_tanks[2].moving_down = True
                            vet_tanks[2].direcao = 4
                    if event.type == KEYUP:
                        if event.key == K_DOWN:
                            vet_tanks[2].moving_down = False

                    if event.type == KEYDOWN:
                        if event.key == K_RCTRL:
                            vet_tanks[2].atirar(vet_tanks[2].rect.x, vet_tanks[2].rect.y, vet_tanks[2].direcao)
                            ultimo = len(vet_tanks[2].bullets) - 1
                            todas_as_sprites.add(vet_tanks[2].bullets[ultimo])

                elif i == 3:
                    if event.type == KEYDOWN:
                        if event.key == K_KP1:
                            vet_tanks[3].moving_left = True
                            vet_tanks[3].direcao = 1
                    if event.type == KEYUP:
                        if event.key == K_KP1:
                            vet_tanks[3].moving_left = False

                    if event.type == KEYDOWN:
                        if event.key == K_KP3:
                            vet_tanks[3].moving_right = True
                            vet_tanks[3].direcao = 2
                    if event.type == KEYUP:
                        if event.key == K_KP3:
                            vet_tanks[3].moving_right = False

                    if event.type == KEYDOWN:
                        if event.key == K_KP5:
                            vet_tanks[3].moving_up = True
                            vet_tanks[3].direcao = 3
                    if event.type == KEYUP:
                        if event.key == K_KP5:
                            vet_tanks[3].moving_up = False

                    if event.type == KEYDOWN:
                        if event.key == K_KP2:
                            vet_tanks[3].moving_down = True
                            vet_tanks[3].direcao = 4
                    if event.type == KEYUP:
                        if event.key == K_KP2:
                            vet_tanks[3].moving_down = False

                    if event.type == KEYDOWN:
                        if event.key == K_KP_ENTER:
                            vet_tanks[3].atirar(vet_tanks[3].rect.x, vet_tanks[3].rect.y, vet_tanks[3].direcao)
                            ultimo = len(vet_tanks[3].bullets) - 1
                            todas_as_sprites.add(vet_tanks[3].bullets[ultimo])

        # collision with walls
        for tank in vet_tanks:
            if (tank.rect.x + tank.rect.width) > largura:
                tank.rect.x = largura - tank.rect.width
            if tank.rect.x < 0:
                tank.rect.x = 0
            if tank.rect.y < 0:
                tank.rect.y = 0
            if (tank.rect.y + tank.rect.height) > altura:
                tank.rect.y = altura - tank.rect.height


        # collision bullet with wall
        i = 0
        j = 0
        while i < len(vet_tanks):
            j = 0
            while j < len(vet_tanks[i].bullets):
                if (vet_tanks[i].bullets[j].rect.x + vet_tanks[i].bullets[j].rect.width) > largura:
                    vet_tanks[i].bullets[j].rect.x = -40
                    vet_tanks[i].bullets.pop(j)
                    i -= 1
                elif vet_tanks[i].bullets[j].rect.x < 0:
                    vet_tanks[i].bullets[j].rect.x = -40
                    vet_tanks[i].bullets.pop(j)
                    i -= 1
                elif vet_tanks[i].bullets[j].rect.y + vet_tanks[i].bullets[j].rect.height > altura:
                    vet_tanks[i].bullets[j].rect.y = -40
                    vet_tanks[i].bullets.pop(j)
                    i -= 1
                elif vet_tanks[i].bullets[j].rect.y < 0:
                    vet_tanks[i].bullets[j].rect.y  = -40
                    vet_tanks[i].bullets.pop(j)
                    i -= 1
                j += 1
            i += 1

        menu_screen.blit(image_fundo, (0, 0))
        todas_as_sprites.draw(menu_screen)
        todas_as_sprites.update()
        pygame.display.flip()


start_game()
