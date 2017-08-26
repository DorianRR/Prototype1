import pygame
#origin ： CSDN community
x = 10
y = 10
vx = 6
vy = 0
gy = 3
fx = -1
fy = -4
pygame.init()
clock = pygame.time.Clock()
area = [800,500]
screen = pygame.display.set_mode(area)
pygame.display.set_caption("PHY")
time = 10
while True:
    screen.fill(0)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_n:
            pygame.quit()
            exit(0)
    clock.tick(30)
    x += vx
    vy = vy+gy
    y += vy
    if y > 490:
        y = 490
        vx += fx
        if vx < 0:
            vx = 0
        vy += fy
        if vy < 0:
            vy = 0
        vy = -vy
    pygame.draw.circle(screen,[255,0,0],[x,y],10)
    pygame.display.update()
    time += 1