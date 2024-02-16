import pygame
import os
import obstacles
import menu

pygame.init()

main_menu = True
obs = obstacles.Obstacles(500, 400, 100, 100)
timer = pygame.time.Clock()
fps = 60
screen_setups = [pygame.RESIZABLE, pygame.FULLSCREEN]
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
menu_screen = pygame.display.set_mode((screen_width - 100, screen_height - 100), screen_setups[0])
pygame.display.set_caption('Tankpygame ta ligado!')


def start_game():

    global menu_screen, obs
    running = True

    while running:
        pygame.display.update()
        timer.tick(fps)
        menu_screen.fill((0, 0, 0))
        pygame.draw.rect(menu_screen, 'green', pygame.rect.Rect(obs.posx, obs.posy, obs.width, obs.height))
        menu.draw_main_menu(menu_screen)

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


start_game()
