import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Test")

image_path = "image.png"
image = pygame.image.load(image_path)

running = True
while running:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
screen.fill((30, 30, 30))
screen.blit(image, (0, 0))
pygame.display.flip()

pygame.quit()