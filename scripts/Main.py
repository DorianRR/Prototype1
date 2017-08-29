import PyIgnition,pygame, math, sys
from Player import *
from SimpleUI import *

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Destructo-Spin!")
clock = pygame.time.Clock()
FPS = 60

player = Player("PlayerCharacterTemp.png")
map = pygame.image.load("BgForTest.png")


#------------------
fire = PyIgnition.ParticleEffect(screen, (0, 0), (800, 600))
gravity = fire.CreateDirectedGravity(strength = 0.07, direction = [player.direction.x,player.direction.y]) #here to change gravity direction should be the same as player facing direction
wind = fire.CreateDirectedGravity(strength = 0.00, direction = [1, 0])
source = fire.CreateSource((300, 500), initspeed = 2.0, initdirection = 0.0, initspeedrandrange = 0.5, initdirectionrandrange = 0.5, particlesperframe = 10, particlelife = 100, drawtype = PyIgnition.DRAWTYPE_CIRCLE, colour = (255, 255, 255), radius = 3.0)
source.CreateParticleKeyframe(10, colour = (200, 200, 220), radius = 4.0)
source.CreateParticleKeyframe(30, colour = (190, 190, 200), radius = 6.0)
source.CreateParticleKeyframe(60, colour = (100, 100, 150), radius = 20.0)
source.CreateParticleKeyframe(80, colour = (0, 0, 0), radius = 50.0)
#rect = fire.CreateRectangle((400, 100), (200, 100, 100), bounce = 0.2, width = 100, height = 20)
#rect.CreateKeyframe(frame = 500, pos = (400, 250), width = 200, height = 30)

#fire.SaveToFile("Fire.ppe")
#------------------


while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

    player.update()
    screen.fill((0, 0, 0))
    source.SetPos(player.location)
    #keep these two lines of code after any screen.blit() bacause we want texts appear above everything#
    screen.blit(uicreate(player)[0], [20, 20])                                                          #
    screen.blit(uicreate(player)[1], [654, 20])
    screen.blit(map, player.getPositionOffset())
    #screen.blit(map, [0,0])
    player.draw(screen)
    fire.Update()
    fire.Redraw()
    clock.tick(FPS)
    pygame.display.flip()
