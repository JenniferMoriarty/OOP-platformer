import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spring Scene")

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Sky
    screen.fill((135, 206, 235))

    # Grass
    pygame.draw.rect(screen, (60, 179, 113), (0, 400, 800, 200))

    # Sun
    pygame.draw.circle(screen, (255, 223, 0), (700, 100), 50)

    # Rainbow (flipped so it's a proper arch)
    pygame.draw.arc(screen, (255, 0, 0), (200, 300, 400, 400), 0, math.pi, 10)
    pygame.draw.arc(screen, (255, 127, 0), (210, 310, 380, 380), 0, math.pi, 10)
    pygame.draw.arc(screen, (255, 255, 0), (220, 320, 360, 360), 0, math.pi, 10)
    pygame.draw.arc(screen, (0, 255, 0), (230, 330, 340, 340), 0, math.pi, 10)
    pygame.draw.arc(screen, (0, 0, 255), (240, 340, 320, 320), 0, math.pi, 10)
    pygame.draw.arc(screen, (75, 0, 130), (250, 350, 300, 300), 0, math.pi, 10)
    pygame.draw.arc(screen, (148, 0, 211), (260, 360, 280, 280), 0, math.pi, 10)

    # Flower 1
    pygame.draw.circle(screen, (255, 105, 180), (90, 450), 10)
    pygame.draw.circle(screen, (255, 105, 180), (110, 450), 10)
    pygame.draw.circle(screen, (255, 105, 180), (100, 440), 10)
    pygame.draw.circle(screen, (255, 105, 180), (100, 460), 10)
    pygame.draw.circle(screen, (255, 255, 0), (100, 450), 8)
    pygame.draw.line(screen, (0, 100, 0), (100, 460), (100, 500), 3)

    # Bee 1
    pygame.draw.ellipse(screen, (255, 215, 0), (150, 200, 30, 20))
    pygame.draw.line(screen, (0, 0, 0), (155, 200), (155, 220), 2)
    pygame.draw.line(screen, (0, 0, 0), (165, 200), (165, 220), 2)
    pygame.draw.ellipse(screen, (255, 255, 255), (155, 190, 10, 15))
    pygame.draw.ellipse(screen, (255, 255, 255), (165, 190, 10, 15))


    pygame.display.flip()



pygame.quit()


