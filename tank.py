import pygame
import bullet

class Tank:
    def __init__(self, division, posx, posy, color, width, height, firerate):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.width = width
        self.height = height

    def create_tank(self, screen):
        pygame.draw.rect(screen, self.color, [self.posx, self.posy, self.width, self.height])
        return self

    def move_up(self):
        self.posy = self.posy - 3
        return self.posy

    def move_left(self):
        self.posx = self.posx - 3
        return self.posx

    def move_right(self):
        self.posx = self.posx + 3
        return self.posx

    def move_down(self):
        self.posy = self.posy + 3
        return self.posy

    def change_color(self, color):
        self.color = color

    def shot(self):
        print('disparou')
        #  create a bullet
