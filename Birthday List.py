# Setup
import random
gifts = ["a puppy", "a bike", "a new game", "a computer", "a phone"]
choice = random.randint(0, len(gifts) - 1)

# Output
print(gifts)
print("For my birthday I would like " + gifts[choice])
