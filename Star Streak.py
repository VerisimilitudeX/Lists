# --- Libraries --- #
import pygame
import random
pygame.init()

# --- Graphics variables --- #
window = pygame.display.set_mode([800, 600])
c = pygame.time.Clock()
x_positions = []
y_positions = []

# --- Timer variables --- #
timer = 0
star_time = 40

# --- Main loop --- #
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # --- Make stars --- #
    timer += c.get_time()
    if timer >= star_time:
        timer = 0
        x_positions.append(0)
        y_positions.append(random.randint(0, 600))


    # --- Move and draw stars --- #
    window.fill((5, 0, 43))
    index = 0
    while index < len(x_positions):
        x_positions[index] += 1
        pygame.draw.circle(window, (250, 250, 230), (x_positions[index], y_positions[index]), 3)
        index += 1

    pygame.display.flip()
    c.tick()
