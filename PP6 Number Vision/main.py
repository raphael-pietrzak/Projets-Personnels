import scikit
import pygame

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen.fill((0,0,0))
click = False 
draw = True
x0, y0 = 0,0
while draw:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            click = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            x0, y0 = pygame.mouse.get_pos()

        
    if click:
        x1, y1 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(255,255,255),(x0, y0), (x1, y1),3)
        x0, y0 = x1, y1
    pygame.display.flip()
for i in range(0,screen.get_size()[0],5):
    for j in range(0,screen.get_size()[1],5):
        pygame.draw.circle(screen,(255,255,255),(i, j),5,5)
        if pygame.Surface.get_at(screen, (i,j)) == (255, 255, 255, 255):
            pygame.draw.circle(screen,(255,0,0),(i, j),5,5)
            pygame.display.flip()

pygame.image.save(screen, "screen.png")


