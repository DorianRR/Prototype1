import PyIgnition,pygame, math, sys
from Player import *
from DestructibleObject import *
from SimpleUI import *
from Level import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
pygame.display.set_caption("Destructo-Spin!")
clock = pygame.time.Clock()
FPS = 60
level = Level()

#------------------
fire = PyIgnition.ParticleEffect(screen, (0, 0), (800, 600))
#gravity = fire.CreateDirectedGravity(strength = 0.00, direction = [player.direction.x,player.direction.y]) #here to change gravity direction should be the same as player facing direction
#here change the initial direction
source = fire.CreateSource((player.rect.center), initspeed = 3.0, initdirection = 3.140, initspeedrandrange = 0.3, initdirectionrandrange = 0.3, particlesperframe = 8, particlelife = 70, drawtype = PyIgnition.DRAWTYPE_IMAGE, colour = (255, 255, 255), radius = 3.0,imagepath = "../images/ParticleTexture_01.png")
#source.CreateParticleKeyframe(10, colour = (200, 200, 220), radius = 4.0)
#source.CreateParticleKeyframe(30, colour = (190, 190, 200), radius = 6.0)
#source.CreateParticleKeyframe(60, colour = (100, 100, 150), radius = 20.0)

#------------------


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
         if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
             pygame.quit()
             sys.exit()



    screen.fill((0, 0, 0))
    tempTuple = (player.rect.centerx+16,player.rect.centery+16)
    source.SetPos(tempTuple)
    source.SetInitDirection(player.imageRotated*2*math.pi/8)
    player.update()
    level.update()

    level.draw(screen)
    key_1 = pygame.key.get_pressed()
    if not key_1[pygame.K_SPACE]:
        for particle in fire.particles:
            particle.alive = False
        else:
            pass

    fire.Update()
    fire.Redraw()
    player.draw(screen)
    #keep these two lines of code after any screen.blit() bacause we want texts appear above everything#
    clock.tick(FPS)
    screen.blit(uicreate(level)[0], [20, 20])  #
    screen.blit(uicreate(level)[1], [654, 20])
    pygame.display.flip()
