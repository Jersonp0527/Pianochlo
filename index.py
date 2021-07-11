import pygame

pygame.init()
#Colores
white=(255,255,255) 
gray=(161, 161, 161)
black=(0,0,0)


size = (450,800)
screen = pygame.display.set_mode(size)

run=True

#Las lineas
while run:

    screen.fill(white)
    pygame.draw.line(screen,gray,(112,0),(112,800),3)
    pygame.draw.line(screen,gray,(224,0),(224,800),3)
    pygame.draw.line(screen,gray,(336,0),(336,800),3)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
