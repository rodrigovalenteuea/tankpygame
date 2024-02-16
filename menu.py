import pygame
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 24)
def draw_main_menu(screen):
    pygame.draw.rect(screen, (255, 0, 0), [200, 300, 260, 40])
    menu_text = font.render('Start Game', True, (200, 200, 200))
    screen.blit(menu_text, (207, 305))
