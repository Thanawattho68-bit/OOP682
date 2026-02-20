import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Sara Cal")

running = True
sara_sheet = pygame.image.load("sara/sara-cal1.png").convert_alpha()
sara_rect = pygame.Rect(0, 0, 34, 56)  # Assuming each frame is 64x64 pixels
sara_pos = pygame.Rect(50, 50, 34, 56)

clock = pygame.time.Clock()

while running:  # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and sara_pos.x < screen.get_width() - sara_rect.width:
        sara_pos.x += 5
    if keys[pygame.K_LEFT] and sara_pos.x > 0:
        sara_pos.x -= 5
    if keys[pygame.K_DOWN] and sara_pos.y < screen.get_height() - sara_rect.height:
        sara_pos.y += 5
    if keys[pygame.K_UP] and sara_pos.y > 0:
        sara_pos.y -= 5

    clock.tick(60)  # Limit 60 FPS
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"FPS: {clock.get_fps():.2f}", True, (0, 0, 0))

    screen.blit(text, (10, 10))
    screen.blit(sara_sheet, sara_pos, sara_rect)
    pygame.display.update()

pygame.quit()
