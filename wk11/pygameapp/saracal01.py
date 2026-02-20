import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Sara Cal")

running = True
sara = pygame.image.load("sara/sara-cal-cut.png").convert_alpha()  # sara-cal1.png
clock = pygame.time.Clock()

while running:  # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # Limit 60 FPS
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(f"FPS: {clock.get_fps():.2f}", True, (0, 0, 0))

    screen.blit(text, (300, 230))
    screen.blit(sara, (100, 50))
    pygame.display.update()

pygame.quit()
