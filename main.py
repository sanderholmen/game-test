import pygame, sys

pygame.init()

def bouncing_rect():
    global x_speed, y_speed

    #make rect move
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    #collision with screen borders
    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
        y_speed *= -1

    #collision with rect
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) > collision_tolerance:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) > collision_tolerance:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) > collision_tolerance:
            x_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) > collision_tolerance:
            y_speed *= -1

    #render objects
    pygame.draw.rect(screen, (255, 255, 255), moving_rect)
    pygame.draw.rect(screen, (255, 0, 0), other_rect)

clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))

#creating first object
moving_rect = pygame.Rect(100, 100, 100, 100)
x_speed, y_speed = 5, 4

#creating second object
other_rect = pygame.Rect(300, 300, 200, 100)
other_speed = 2



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    bouncing_rect()

    pygame.display.flip()
    clock.tick(60)