import pygame, sys, random, math, datetime
import globalvars
from classes import *
from pygame.locals import *

# define constants
BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
RED        = (255,   0,   0)
GREEN      = (  0, 255,   0)
BLUE       = (  0,   0, 255)
PURPLE     = (255,   0, 255)
YELLOW     = (255, 255,   0)

BGCOLOR = BLACK

startpos = (800, 800)

# load pygame
pygame.init()
screen = pygame.display.set_mode(globalvars.screensize)

forces = []
f1 = Force(startpos, 0, 100, RED)
f2 = Force(startpos, 90, 100, BLUE)
f3 = Force.addforces(f1, f2)

def convert_pos(pos):
    x = pos[0]
    y = globalvars.screensize[1] - pos[1]
    return (x, y)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_p:
                now = datetime.datetime.now()
                filename = "PhysicsAnimation screenshot at %02d-%02d-%04d %02d.%02d.%02d.png" % (now.day, now.month, now.year, now.hour, now.minute, now.second)
                pygame.image.save(screen, filename)



    # rotate force2:
    # if pygame.mouse.get_pressed()[0]:
    #     pos = convert_pos(pygame.mouse.get_pos())
    #     angle = math.degrees(math.atan2(pos[1] - startpos[1], pos[0] - startpos[0]))
    #     f2.direction = angle
    #     f3 = Force.addforces(f1, f2)

    # position force2:
    if pygame.mouse.get_pressed()[0]:
        pos = convert_pos(pygame.mouse.get_pos())
        f2.terminal = pos
        f3 = Force.addforces(f1, f2)

    # draw
    screen.fill(BGCOLOR)
    forces = [f1, f2, f3]
    for force in forces:
        force.draw(screen)

    pygame.display.update()
