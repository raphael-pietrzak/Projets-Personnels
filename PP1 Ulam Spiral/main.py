from math import *
import pygame


class Block(pygame.sprite.Sprite):
    width = 5
    height = 5
    id = 0

    def __init__(self):
        super().__init__()
        Block.id += 1
        self.id = Block.id
        self.image = pygame.Surface([Block.width, Block.height])
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = [0, 0]

    def move(self, x, y, absc, aug):
        x += Block.height*absc*aug - Block.height*absc*(not aug)
        y += Block.height*(not absc)*aug - Block.height*(not absc)*(not aug)
        self.rect.center = [x, y]
        return x, y


def turn(absc, aug):
    absc = not absc
    if absc == False:
        aug = not aug
    return absc, aug

def IsPrime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
a, b = screen.get_size()
x, y = a/2, b/2
group = pygame.sprite.Group()
each_two_line = 0
counter = 0
end_line_counter = 1
absc = False
aug = True

continuer = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = not continuer
    if continuer:
        a = Block()
        x, y = a.move(x, y, absc, aug)
        counter += 1

        if counter == end_line_counter:
            each_two_line += 1
            counter = 0
            absc, aug = turn(absc, aug)

        if each_two_line % 3 == 0:
            each_two_line = 1
            end_line_counter += 1

        if IsPrime(a.id):
            print(a.id)
            screen.blit(a.image, a.rect.center)
            # font = pygame.font.SysFont("arial", 20)
            # text = font.render(str(a.id), True, (0, 0, 0))
            # screen.blit(text, a.rect.center)



        pygame.display.flip()
