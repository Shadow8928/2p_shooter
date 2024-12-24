import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(40, screen.get_height()-40)
projectile_pos = pygame.Vector2(40, screen.get_height() -40)
player_pos1 = pygame.Vector2(screen.get_width()-40, 40)
projectile_pos1 = pygame.Vector2(screen.get_width()-40, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "red", player_pos1, 40)
    pygame.draw.circle(screen, "blue",projectile_pos, 10)
    pygame.draw.circle(screen, "blue",projectile_pos1, 10)
    if projectile_pos.y != screen.get_height() -40:
        projectile_pos.y = screen.get_height() -40
    if projectile_pos1.y != 40:
        projectile_pos1.y = 40
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        projectile_pos.x -= 300 * dt

    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        projectile_pos.x += 300 * dt

    if keys[pygame.K_j]:
        player_pos1.x -= 300 * dt
        projectile_pos1.x -= 300 * dt

    if keys[pygame.K_l]:
        player_pos1.x += 300 * dt
        projectile_pos1.x += 300 * dt

    if keys[pygame.K_i]:
        projectile_pos1.y = screen.get_height()-10
        if player_pos.x-40 < projectile_pos1.x and projectile_pos1.x < player_pos.x+40:
            print("Player 2 Wins")
            running = False
    if keys[pygame.K_w]:
        projectile_pos.y = 10
        if player_pos1.x-40 < projectile_pos.x and projectile_pos.x < player_pos1.x+40:
            print("Player 1 Wins")
            running = False
    if player_pos.x < 40:
        player_pos.x = 40
    if player_pos.x > screen.get_width()-40:
        player_pos.x = screen.get_width()-40
    if player_pos1.x < 40:
        player_pos1.x = 40
    if player_pos1.x > screen.get_width()-40:
        player_pos1.x = screen.get_width()-40
    if projectile_pos.x < 40:
        projectile_pos.x = 40
    if projectile_pos.x > screen.get_width()-40:
        projectile_pos.x = screen.get_width()-40
    if projectile_pos1.x < 40:
        projectile_pos1.x = 40
    if projectile_pos1.x > screen.get_width()-40:
        projectile_pos1.x = screen.get_width()-40
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
