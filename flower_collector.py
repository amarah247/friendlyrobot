import pygame
import random

pygame.init()

WIDTH,HEIGHT = 800,600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('flower_collector')

clock = pygame.time.Clock()

character_size = 50
character_color = BLUE
character_pos = [WIDTH // 2, HEIGHT // 2]
character_speed = 5

# Flower settings
flower_size = 20
flower_color = PINK
flower_pos = [random.randint(0, WIDTH - flower_size), random.randint(0, HEIGHT - flower_size)]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_pos[0] -= character_speed
    if keys[pygame.K_RIGHT]:
        character_pos[0] += character_speed
    if keys[pygame.K_UP]:
        character_pos[1] -= character_speed
    if keys[pygame.K_DOWN]:
        character_pos[1] += character_speed


    character_rect = pygame.Rect(character_pos[0], character_pos[1], character_size, character_size)
    flower_rect = pygame.Rect(flower_pos[0], flower_pos[1], flower_size, flower_size)
    if character_rect.colliderect(flower_rect):
        flower_pos = [random.randint(0, WIDTH - flower_size), random.randint(0, HEIGHT - flower_size)]

    screen.fill(WHITE)

    pygame.draw.rect(screen, character_color, character_rect)
    pygame.draw.ellipse(screen, flower_color, flower_rect)

    pygame.display.flip()

    clock.tick(30)

pygame.QUIT()