
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
my_image = pygame.image.load("images/basketball_small.png").convert_alpha()
image_rect = my_image.get_rect(center=(320,240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((0, 0, 0))
image_rect.x += 1 # Move the image to the right
if image_rect.x > screen.get_width(): # If the image goes off the right edge
    image_rect.x = -image_rect.width # Move it to the left edge

screen.blit(my_image, image_rect)
pygame.display.flip()
clock.tick(15) # Limit the frame rate to 60 FPS
