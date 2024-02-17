import pygame
import os
import obstacles
import menu
import tank

pygame.init()

main_menu = True
obs = obstacles.Obstacles(500, 400, 100, 100)
timer = pygame.time.Clock()
fps = 60
screen_setups = [pygame.RESIZABLE, pygame.FULLSCREEN]
screen_options = 0
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
menu_screen = pygame.display.set_mode((screen_width - 100, screen_height - 100), screen_setups[screen_options])
pygame.display.set_caption('Tankpygame ta ligado!')


def start_game():

    global menu_screen, obs, screen_options
    running = True


    while running:
        pygame.display.update()
        timer.tick(fps)
        menu_screen.fill((0, 0, 0))
        #menu.draw_main_menu(menu_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            '''
            if event.type == pygame.KEYDOWN and pygame.K_f:
                if screen_options == 0:
                    screen_options = 1
                    pygame.display.set_mode((0, 0), screen_setups[screen_options])
                elif screen_options == 1:
                    print(pygame.event.get())
                    screen_options = 0
                    pygame.display.set_mode((screen_width - 100, screen_height - 100), screen_setups[screen_options])
            '''
    pygame.quit()


start_game()
