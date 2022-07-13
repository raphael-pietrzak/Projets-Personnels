import pygame

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

class Block:
    counter = 0
    def __init__(self, x, l, m, v):
        self.m = m
        self.x = 300+x
        self.l = l
        self.v = v
        self.color = (255,255,255)
        self.rect = pygame.Rect((0,0), (self.l, self.l))
        self.rect.bottomleft = (self.x, 700)
    
    def show(self):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def move(self):
        self.x += self.v
        self.rect.bottomleft = (self.x, 700)
    
    def collide(self, other):
        m_sum = self.m + other.m
        v = (2*other.m/m_sum)*other.v
        v += (( self.m-other.m)/m_sum)*self.v
        return v
    
    def touch(self,other):
        if (self.x+self.l >= other.x):
            v1 = self.collide(other)
            v2 = other.collide(self)
            self.v = v1
            other.v = v2
            Block.counter +=1

        if self.x <0:
            self.v = -self.v
            Block.counter +=1


        

    

B1 = Block(2,40,1,0)
B2 = Block(200,70,10000,-2)
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()


while True:
    clock.tick(30)
    screen.fill((0,0,0))
    B1.move()
    B2.move()
    B1.touch(B2)
    B1.show()
    if (B1.l > B2.x):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(B1.l, 700-B2.l, B2.l, B2.l))
    else:
        B2.show()
    text = font.render(str(Block.counter), True, (255,255,255))
    screen.blit(text, (100,100))

    pygame.display.flip()
