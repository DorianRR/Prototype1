import PyIgnition,pygame, math, sys
from Player import *
from DestructibleObject import *
from SimpleUI import *
from Level import *
from Fire import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
pygame.display.set_caption("Destructo-Spin!")
clock = pygame.time.Clock()
FPS = 60 
level = Level()
timeCount = 0


#------------------
fire = PyIgnition.ParticleEffect(screen, (0, 0), (800, 600))
#gravity = fire.CreateDirectedGravity(strength = 0.00, direction = [player.direction.x,player.direction.y]) #here to change gravity direction should be the same as player facing direction
#here change the initial direction
source = fire.CreateSource((player.rect.center), initspeed = 3.0, initdirection = 3.140, initspeedrandrange = 0.3, initdirectionrandrange = 0.3, particlesperframe = 8, particlelife = 30, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = "../images/ParticleTexture_03.png")
source1 = fire.CreateSource((player.rect.center), initspeed = 3.0, initdirection = 3.140, initspeedrandrange = 0.1, initdirectionrandrange = 0.7, particlesperframe = 1, particlelife = 20, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = "../images/ParticleTexture_07.png")
source2 = fire.CreateSource((player.rect.center), initspeed = 8.0, initdirection = 3.140, initspeedrandrange = 0.1, initdirectionrandrange = 0.2, particlesperframe = 3, particlelife = 30, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = "../images/ParticleTexture_07.png")
#source.CreateParticleKeyframe(10, colour = (200, 200, 220), radius = 4.0)
#source1.CreateParticleKeyframe(30, colour = (190, 190, 200), radius = 6.0)
#source2.CreateParticleKeyframe(60, colour = (100, 100, 150), radius = 20.0)
#------------------
playing = True


while playing:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
         if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
             pygame.quit()
             sys.exit()
    tempTuple = (player.rect.centerx+16,player.rect.centery+16)
    source1.SetPos(tempTuple)
    source1.SetInitDirection((player.imageRotated - 1.25 * math.pi) * 2 * math.pi / 8)
    source.SetPos(tempTuple)
    source.SetInitDirection((player.imageRotated-1.25*math.pi)*2*math.pi/8)
    source1.SetPos(tempTuple)
    source1.SetInitDirection((player.imageRotated - 1.25 * math.pi) * 2 * math.pi / 8)
    source2.SetPos((1775,430))
    player.update()
    level.update()
    #numberSurface = uicreate(level)[1]
    #titleSurface = uicreate(level)[0]
    level.draw(screen)
    #key_1 = pygame.key.get_pressed()

    if not keys[pygame.K_SPACE]:
        #fire.particles[:] = []
        for particle in fire.particles:
            if timeCount > 50:
                particle.alive = False
            timeCount += 1

    fire.Update()
    fire.Redraw()
    player.draw(screen)
    level.fireList.draw(screen)
    #keep these two lines of code after any screen.blit() bacause we want texts appear above everything#
    clock.tick(FPS)
    screen.blit(uicreate(level)[1], [1596, 50])
    screen.blit(uicreate(level)[0], [1596, 20])
    level.FuelBar(screen,[200,220,250],50,25,level.fuelLevel,level.Maxfuel)
    pygame.display.flip()
    if level.fuelLevel <= 0:
        playing = False
    print(len(fire.particles))  #it stays 24 so might not be the problem of particles
    #print("fire is"sys.getrefcount(fire))
while not playing:
    checkSurface = pygame.image.load("../images/Check00.jpg").convert_alpha()
    keys = pygame.key.get_pressed()
    #player.update()
    #level.update()

    level.draw(screen)
    level.FuelBar(screen, [25, 150, 160], 50, 25, level.fuelLevel, level.Maxfuel)
    screen.blit(checkSurface, (250, 200))
    screen.blit(uicreate(level)[1], [275, 210])
    for event in pygame.event.get():
         if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
             pygame.quit()
             sys.exit()

    pygame.display.flip()
    pass
