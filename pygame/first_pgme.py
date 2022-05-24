import pygame 
import random

pygame.init()

ORANGE =(255,140,0)
ROT = (255,0,0)
GRUEN=(0,255,0)
Random_Color = ((random.randint(0,255), random.randint(0,255), random.randint   (0,255)))
FENSTERHOEHE= 400
FENSTERBREITE= 600
screen= pygame.display.set_mode((FENSTERBREITE,FENSTERHOEHE))
#TItel für fensterkopf
pygame.display.set_caption("Unser erstes Pygame Spiel")
spielaktiv= True #solange true, spiel geht weiter
clock=pygame.time.Clock()
ballpos_x = 300
ballpos_y = 30
BALL_DURCHMESSER = 20
bewegung_y = 3
bewegung_x = 3
aktion=0

while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False

    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        aktion=1
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        aktion=2
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        aktion=3
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        aktion=4
    if event.type != pygame.KEYDOWN:
        aktion=0

    screen.fill(Random_Color)
    pygame.draw.ellipse(screen,ROT,[ballpos_x,ballpos_y,BALL_DURCHMESSER,BALL_DURCHMESSER])
    if ballpos_y >= FENSTERHOEHE - BALL_DURCHMESSER or ballpos_y<=0:
        bewegung_y = bewegung_y *(-1)
        Random_Color = ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    if ballpos_x >= FENSTERBREITE - BALL_DURCHMESSER or ballpos_x<=0:
        bewegung_x = bewegung_x *(-1)
        Random_Color = ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    if aktion == 1:
            ballpos_y = ballpos_y + bewegung_y
    if aktion == 2:
            ballpos_x = ballpos_x + bewegung_x
    if aktion == 3:
            ballpos_y = ballpos_y - bewegung_y
    if aktion == 4:
            ballpos_x = ballpos_x - bewegung_x
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
"""    
    if ballpos_y < FENSTERHOEHE - BALL_DURCHMESSER:
        ballpos_y += bewegung_y
    if ballpos_y == 380:
        ballpos_y -= bewegung_y
"""
