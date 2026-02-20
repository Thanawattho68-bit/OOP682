import pygame
from pygame.sprite import Sprite


class Hero(Sprite):
    def __init__(self, name, filename, x, y, row=2, cols=3, width=34, height=56):
        super().__init__()
        self.name = name
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sheet.set_colorkey((215, 255, 255))
        self.row = 0
        self.col = 0
        self.elapsed_time = 0
        self.rect = pygame.Rect(x, y, width, height)
        self.sound = pygame.mixer.Sound("sara/swishes/swish-1.wav")

    def act(self):
        self.sound.play()

    def update(self, elapsed_time=100):
        self.elapsed_time += elapsed_time
        if self.elapsed_time > 100:  # 30 FPS
            self.col = (self.col + 1) % 3
            if self.col == 0:
                self.row = (self.row + 1) % 2
            self.elapsed_time -= 100

    def left(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.x = 0

    def right(self):
        self.rect.x += 5
        if self.rect.x > 400 - self.rect.width:
            self.rect.x = 400 - self.rect.width

    def up(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.rect.y = 0

    def down(self):
        self.rect.y += 5
        if self.rect.y > 300 - self.rect.height:
            self.rect.y = 300 - self.rect.height

    def draw(self, surface):
        frame = self.sheet.subsurface(
            self.col * self.rect.width,
            self.row * self.rect.height,
            self.rect.width,
            self.rect.height,
        )
        surface.blit(frame, self.rect)
