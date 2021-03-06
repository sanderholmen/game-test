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

#defining borders
screen_right = 1000
screen_left = 0
screen_top = 0
screen_bottom = 700

# score
p1_points = 0
p2_points = 0

font = pygame.font.Font('freesansbold.ttf', 32)

textX = 800
textY = 100

def show_score(x, y):
    p1_score = font.render(str(p1_points), True, (255, 255, 255))
    screen.blit(p1_score, (x, y))
    
    p2_score = font.render(str(p2_points), True, (255, 255, 255))
    screen.blit(p2_score, (x-600, y))


# ball speed
x_speed = -3
y_speed = -3

# game state
running, pause = True, False
state = pause


def bounce_ball():
    global screen_top, screen_bottom, y_speed, x_speed

    if game_ball.top <= screen_top or game_ball.bottom >= screen_bottom:
        y_speed *= -1

    if game_ball.colliderect(p1_rect) or game_ball.colliderect(p2_rect):
        x_speed *= -1

def score():
    global screen_right, screen_left, y_speed, x_speed, p1_points, p2_points, state

    if game_ball.left <= screen_left:
        p1_points += 1
        state = pause
        game_ball.x = 500
        game_ball.y = 350

    if game_ball.right >= screen_right:
        p2_points += 1
        state = pause
        game_ball.x = 500
        game_ball.y = 350



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
            if event.key == pygame.K_SPACE:
                if state == pause:
                    state = running
                else:
                    state = pause
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p1_speed = 0
            if event.key == pygame.K_DOWN:
                p1_speed = 0
            if event.key == pygame.K_w:
                p2_speed = 0
            if event.key == pygame.K_s:
                p2_speed = 0

    bounce_ball()

    score()

    #when game is not paused
    if state == running:
        # add movement to players
        p1_rect.y += p1_speed
        p2_rect.y += p2_speed

        # ball movement
        game_ball.x += x_speed
        game_ball.y += y_speed

        #checking if players hit borders
        if p1_rect.y <= 0:
            p1_rect.y = 0
        if p1_rect.y >= 600:
            p1_rect.y = 600
        if p2_rect.y <= 0:
            p2_rect.y = 0
        if p2_rect.y >= 600:
            p2_rect.y = 600

    screen.fill((30, 30, 30))

    show_score(textX, textY)

    #draw objects on screen
    pygame.draw.rect(screen, (255, 255, 255), p1_rect)
    pygame.draw.rect(screen, (255, 255, 255), p2_rect)
    pygame.draw.rect(screen, (255, 255, 255), game_ball)

    pygame.display.flip()
    clock.tick(60)