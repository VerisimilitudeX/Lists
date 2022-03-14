# Library
import random

# Variables
animal1 = "tiger"
animal2 = "dog"
animal3 = "lizard"
animal4 = "hedgehog"
animal5 = "ferret"
animals = ["tiger", "dog", "lizard", "hedgehog", "ferret"]

# Get random choice
choice = random.randint(1, len(animals) - 1)

# Select animal
if choice == 1:
    pet = animal1
elif choice == 2:
    pet = animal2
elif choice == 3:
    pet = animal3
elif choice == 4:
    pet = animal4
elif choice == 5:
    pet = animal5

# Output
print("Your pet is a " + animals[choice])
