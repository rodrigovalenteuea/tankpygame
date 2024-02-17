class Bullet:
    def __init__(self, tank, speedx, speedy, posx, posy, width, height):
        self.tank = tank
        self.speedx = speedx
        self.speedy = speedy
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

    def moviment_right(self, posx, speedx):
        self.posx = posx + speedx
        return posx

    def moviment_left(self, posx, speedx):
        self.posx = posx - speedx
        return posx

    def moviment_up(self, posy, speedy):
        self.posy = posy - speedy
        return posy

    def moviment_down(self, posy, speedy):
        self.posy = posy + speedy
        return posy
