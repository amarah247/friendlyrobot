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


# Load flower images
flower_images = [
    pygame.image.load('flower2.jpg'),
    pygame.image.load('flower.jpg')
]
flower_rects = [img.get_rect() for img in flower_images]
print(flower_rects)
# Randomly position the first flower
current_flower_index = 0
flower_rects[current_flower_index].topleft = (
    random.randint(0, WIDTH - flower_rects[current_flower_index].width),
    random.randint(0, HEIGHT - flower_rects[current_flower_index].height)
)

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
    # flower_rect = pygame.Rect(flower_pos[0], flower_pos[1], flower_size, flower_size)
    if character_rect.colliderect(flower_rects[current_flower_index]):
        current_flower_index = random.randint(0, len(flower_images) - 1)
        flower_rects[current_flower_index].topleft = (
            random.randint(0, WIDTH - flower_rects[current_flower_index].width),
            random.randint(0, HEIGHT - flower_rects[current_flower_index].height)
        )

    screen.fill(WHITE)

    pygame.draw.rect(screen, character_color, character_rect)
    screen.blit(flower_images[current_flower_index], flower_rects[current_flower_index])


    pygame.display.flip()

    clock.tick(30)

pygame.QUIT()