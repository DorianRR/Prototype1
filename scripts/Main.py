import PyIgnition,pygame, math, sys
from Player import *
from DestructibleObject import *
from SimpleUI import *
from Level import *

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Destructo-Spin!")
clock = pygame.time.Clock()
FPS = 60
#player = Player("PlayerCharacterTemp.png")
#box = DestructibleObject("BoxCollider",(100,100))
#collidableSprites = pygame.sprite.Group()
#collidableSprites.add(box)
level = Level()

#------------------
fire = PyIgnition.ParticleEffect(screen, (0, 0), (800, 600))
#gravity = fire.CreateDirectedGravity(strength = 0.00, direction = [player.direction.x,player.direction.y]) #here to change gravity direction should be the same as player facing direction
wind = fire.CreateDirectedGravity(strength = 0.00, direction = [1, 0])
#here change the initial direction
source = fire.CreateSource((300, 500), initspeed = 3.0, initdirection = 3.140, initspeedrandrange = 0.3, initdirectionrandrange = 0.1, particlesperframe = 10, particlelife = 100, drawtype = PyIgnition.DRAWTYPE_IMAGE, colour = (255, 255, 255), radius = 3.0,imagepath = "arrow.png")
source.CreateParticleKeyframe(10, colour = (200, 200, 220), radius = 4.0)
source.CreateParticleKeyframe(30, colour = (190, 190, 200), radius = 6.0)
source.CreateParticleKeyframe(60, colour = (100, 100, 150), radius = 20.0)

#------------------


while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

         #if event.type == pygame.KEYUP:
          #   if event.key == pygame.K_SPACE:


    screen.fill((0, 0, 0))
    source.SetPos(player.location)
    #source.SetPos(((player.location[0] - level.mapRect.centerx)+512, (player.location[1] - level.mapRect.centery)+384))
    #source.SetInitDirection(FPS) #still need to calculate from player's direction
    source.SetInitDirection(player.imageRotated*2*math.pi/8)
    player.update()
    level.update()
     #still need to calculate from player's direction
    #screen.blit(map, level.shiftLevel())
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
    #collidableSprites.draw(screen)
    #keep these two lines of code after any screen.blit() bacause we want texts appear above everything#
    screen.blit(uicreate(player)[0], [20, 20])                                                          #
    screen.blit(uicreate(player)[1], [654, 20])
    clock.tick(FPS)
    pygame.display.flip()

    #    for event in pygame.event.get():
     #    if event.type == pygame.QUIT:
     #        pygame.quit()
     #        sys.exit()

    #screen.fill((0, 0, 0))
    #source.SetPos(player.location)
    #source.SetInitDirection(player.imageRotated*2*3.14/8)
    #player.update()
     #still need to calculate from player's direction
    #keep these two lines of code after any screen.blit() bacause we want texts appear above everything#
    #screen.blit(uicreate(player)[0], [20, 20])                                                          #
    #screen.blit(uicreate(player)[1], [654, 20])                                                         #
    #player.draw(screen)
    #fire.Update()
    #fire.Redraw()
    #clock.tick(FPS)
    #pygame.display.flip()--

