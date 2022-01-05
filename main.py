import pygame, sys

pygame.init()

clock = pygame.time.Clock()
screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))

p1_rect = pygame.Rect(900, 330, 15, 100)
p2_rect = pygame.Rect(100, 330, 15, 100)
player_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (255, 255, 255), p1_rect)
    pygame.draw.rect(screen, (255, 255, 255), p2_rect)

    pygame.display.flip()
    clock.tick(60)