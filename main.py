import pygame, sys
from utils import vector2
from utils import sprite

# setup goes here
pygame.init()
screen = pygame.display.set_mode( (968,574) )
pygame.display.set_caption( "hi there" )

img = pygame.image.load( "mypic.jpeg" ).convert()

pos = vector2(400, 250)


v = vector2(0,0)

sprite1 = sprite("mypic.jpeg", pos, v) 

sprite1.ax = 0.002
sprite1.ay = 0

t = pygame.time.get_ticks()

while True:

    screen.fill( (255,0,80) )
    
    dt = pygame.time.get_ticks() - t
    t = pygame.time.get_ticks()

    sprite1.update(dt, screen)
  
    
    #get user events
    pygame.event.pump()
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    moveX = 0

    if keys[pygame.K_RIGHT]:
        moveX += 1
    elif keys[pygame.K_LEFT]:
        moveX += -1
    if moveX != 0:
        sprite1.vx = moveX * sprite1.ax
    elif sprite1.vx > 0:
        sprite1.vx = sprite1.vx - 0.001 * dt


                

    #siulation stuff goes here

    #draw to screen and flip
    sprite1.draw(screen)
   
    pygame.display.flip()
   

    

