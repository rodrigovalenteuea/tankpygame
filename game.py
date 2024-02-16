import pygame
import os

pygame.init()

main_menu = True

screen_setups = [pygame.RESIZABLE, pygame.FULLSCREEN]
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
menu_screen = pygame.display.set_mode((screen_width - 100, screen_height - 100), screen_setups[0])
pygame.display.set_caption('Tankpygame ta ligado!')

timer = pygame.time.Clock()
fps = 60

font = pygame.font.Font('freesansbold.ttf', 24)

def draw_main_menu():
    global menu_screen
    pygame.draw.rect(menu_screen, (255, 0, 0), [200, 300, 260, 40])
    menu_text = font.render('Start Game', True, (200, 200, 200))
    menu_screen.blit(menu_text, (207, 305))

def draw_game():
    pass

def start_game():
    global menu_screen
    running = True
    while running:
        pygame.display.update()
        timer.tick(fps)
        menu_screen.fill((0, 0, 0))

        if main_menu:
            draw_main_menu()
        else:
            pass

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

start_game()