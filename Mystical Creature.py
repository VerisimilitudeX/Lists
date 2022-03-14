# --- Setup --- #
import random
animals = ["lion", "horse", "dog", "bird", "human", "bat", "cat", "goat"]

# --- Get random parts --- #
head_index = random.randint(0, len(animals) - 1)
head = animals[head_index]
body_index = random.randint(0, len(animals) - 1)
body = animals[body_index]

# --- Print --- #
print("Your mystical creature is a " + head + body + ". It has the head of a " + head + " and the body of a " + body + ". ")
