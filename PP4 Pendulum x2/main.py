from math import pi, cos, sin

import pygame

pygame.init()


r1 = 200
r2 = 100
m1 = 10
m2 = 10
a1 = pi/4
a2 = pi/8
a1_v = 0
a2_v = 0
a1_a = 0.01
a2_a = 0.001
g = 1


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width_screen = screen.get_size()[0]
click = False

clock = pygame.time.Clock()

while True:

    clock.tick(20)

    num1 = -g * (2 * m1 + m2) * sin(a1)
    num2 = -m2 * g * sin(a1 - 2 * a2)
    num3 = -2 * sin(a1 - a2) * m2
    num4 = a2_v*a2_v * r2 + a1_v*a1_v * r1 * cos(a1 - a2)
    den = r1 * (2*m1 + m2 - m2 * cos(2*a1-2*a2))

    a1_a = (num1 + num2 + num3*num4)/den

    num1 = 2*sin(a1-a2)
    num2 = (a1_v**2)*r1*(m1+m2)
    num3 = g*(m1 + m2)*cos(a1)
    num4 = (a2_v**2) * r2 * m2*cos(a1 - a2)

    a2_a = (num1 * (num2 + num3 + num4))/den

    x0 = width_screen/2
    y0 = 200

    x1 = x0 + sin(a1)*r1
    y1 = y0 + cos(a1)*r1
    x2 = x1 + sin(a2)*r2
    y2 = y1 + cos(a2)*r2

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (x0, y0), (x1, y1), 3)

    pygame.draw.circle(screen, (255, 255, 255), (x1, y1), 10)
    pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 3)
    pygame.draw.circle(screen, (255, 255, 255), (x2, y2), 10)

    pygame.display.update()
