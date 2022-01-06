import pygame, sys

pygame.init()

clock = pygame.time.Clock()
screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))

#create player objects
p1_rect = pygame.Rect(900, 330, 15, 100)
p2_rect = pygame.Rect(100, 330, 15, 100)

#create variable for player movement
p1_speed = 0
p2_speed = 0

#create ball object
game_ball = pygame.Rect(500, 350, 10, 10)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checking if key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1_speed = -6
            if event.key == pygame.K_DOWN:
                p1_speed = 6
            if event.key == pygame.K_w:
                p2_speed = -6
            if event.key == pygame.K_s:
                p2_speed = 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p1_speed = 0
            if event.key == pygame.K_DOWN:
                p1_speed = 0
            if event.key == pygame.K_w:
                p2_speed = 0
            if event.key == pygame.K_s:
                p2_speed = 0

    # add movement to players
    p1_rect.y += p1_speed
    p2_rect.y += p2_speed

    screen.fill((30, 30, 30))

    #draw objects on screen
    pygame.draw.rect(screen, (255, 255, 255), p1_rect)
    pygame.draw.rect(screen, (255, 255, 255), p2_rect)
    pygame.draw.rect(screen, (255, 255, 255), game_ball)

    pygame.display.flip()
    clock.tick(60)