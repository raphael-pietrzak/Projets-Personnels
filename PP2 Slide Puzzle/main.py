import random
import pygame
import glob

pygame.init()

files = []
for file in glob.glob("*.jpeg"):
    files.append(file)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
s_width, s_height = screen.get_size()
image = pygame.image.load(files[random.randint(0, len(files)-1)])

class Image(pygame.sprite.Sprite):
    def __init__(self, image, x, y, i, j):
        super().__init__()
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.colms = 3
        self.lines = 3
        self.image = image
        self.width, self.height = image.get_size()
        self.rect = image.get_rect()
        self.rect.center = [x, y]
    

    def generate(self):
        group = pygame.sprite.Group()
        w = int(self.width/self.colms)
        h = int(self.height/self.lines)
        for j in range(0, self.lines):
            for i in range(0, self.colms):
                space = 5
                x, y = self.x-((self.colms-1)*(w+space)/2)+(w+space)*i,self.y-((self.lines-1)*(h+space)/2)+(h+space)*j
                image = self.image.subsurface((i*w, j*h, w, h))
                subImage = Image(image, x, y, i, j)
                group.add(subImage)
        return group




cat = Image(image, s_width/2, s_height/2, 0, 0)
group = pygame.sprite.Group()
group.add(cat)


def move(a):
    v,w = a.i,a.j
    if a.i == empty.i:
        colonne = [i for i in group if i.i == a.i]
        sens = -(a.j - empty.j)/abs(a.j - empty.j)
        for i in colonne:
            if sens*a.j <= sens*i.j < sens*empty.j:
                i.j += sens
                i.rect.centery += (i.height+5)*sens
        empty.i, empty.j = v,w
    elif a.j == empty.j:
        ligne = [i for i in group if i.j == a.j]
        sens = -(a.i - empty.i)/abs(a.i - empty.i)
        for i in ligne:
            if sens*a.i <= sens*i.i < sens*empty.i:
                i.i += sens
                i.rect.centerx += (i.width+5)*sens 
        empty.i, empty.j = v,w



def randomImage(b):
    i = 0
    while i < 20:
        c = random.randint(0,len(group)-1)
        a = random.randint(0,len(group)-1)
        if b[a] != empty and b[c] != empty and (c-a)%2 == 1:
            i+=1
            e = b[a].image
            b[a].image = b[c].image
            b[c].image = e

group = cat.generate()

b = group.sprites()
empty = b[-1]
group.remove(empty)
randomImage(b)


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in group:
                x, y = pygame.mouse.get_pos()
                if i.rect.collidepoint(x, y):
                    move(i)

    group.draw(screen)
    pygame.display.flip()
