import pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Color screen")
blue = (0, 0, 255)
running = True
while running:
    screen.fill(blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    pygame.display.update()
pygame.quit()
