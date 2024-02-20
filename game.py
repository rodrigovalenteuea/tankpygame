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

# test's variables
#tank1 = tank.Tank(screen_width * 0.8, screen_height * 0.5, 'green', 100, 100)
#bullet1 = bullet.Bullet(tank1, 'red', 5, 5, tank1.posx + 100, tank1.posy + 100, 20, 20)
#obs = obstacles.Obstacles(500, 400, 100, 100)


image_fundo = pygame.image.load('background.png').convert()
image_fundo = pygame.transform.scale(image_fundo, (screen_width, screen_height))
qtd_tanks = 4

vet_tanks = []
todas_as_sprites = pygame.sprite.Group()
i = 0
for i in range(qtd_tanks):
    tank1 = tank.Tank()
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
                elif i == 1:
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
                elif i == 2:
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
                elif i == 3:
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

        menu_screen.blit(image_fundo, (0, 0))
        todas_as_sprites.draw(menu_screen)
        todas_as_sprites.update()
        pygame.display.flip()


start_game()
