# --- Setup --- #
import pygame
import random
pygame.init()
window = pygame.display.set_mode([300, 300])
color = 255
c = pygame.time.Clock()

keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

print("Can you guess the right key (1-9?)")

# Get a random key
index = random.randint(0, len(keys) - 1)
correct_key = keys[index]

# --- Main loop --- #
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # --- User guesses --- #
        if event.type == pygame.KEYDOWN:

            # If the event key is the right key,
            # end the program and print a message
            if event.key == correct_key:
                print("You guessed it! ")
                drawing = False

            color -= 25
            if color < 0:
                color = 0

    # --- Draw --- #
    window.fill((0, color, 60))
    pygame.draw.circle(window, (255-color, 0, 0), (150, 150), 50)

    pygame.display.flip()
    c.tick()
