import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))

lists = [(200, 25), (300, 25), (300, 50)]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))
    pygame.draw.polygon(window, (231, 43, 12), lists)
    pygame.display.flip()

    x_input = int(input("What is the x input for the polygon? "))
    y_input = int(input("What is the y input for the polygon? "))
    if x_input == "quit":
        break
    if y_input == "quit":
        break

    point = (int(x_input), int(y_input))
    lists.append(point)

    print(str(lists))
    print()
