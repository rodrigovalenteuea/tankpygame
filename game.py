import pygame
import os
import obstacles
import bullet
import tank

pygame.init()

main_menu = True
obs = obstacles.Obstacles(500, 400, 100, 100)
timer = pygame.time.Clock()
fps = 60

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
menu_screen = pygame.display.set_mode((screen_width - 200, screen_height - 200), pygame.RESIZABLE)
pygame.display.set_caption('Tankpygame ta ligado!')

# test's variables
tank1 = tank.Tank(screen_width - 400, screen_height/2 + 100, 'green', 100, 100)
bullet1 = bullet.Bullet(tank1, 'red', 5, 5, tank1.posx + 100, tank1.posy + 100, 20, 20)

def start_game():

    global menu_screen, obs
    running = True

    while running:
        pygame.display.update()
        timer.tick(fps)
        menu_screen.fill((0, 0, 0))

        tank1.create_tank(menu_screen)
        tank1.shot(bullet1, menu_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


start_game()
