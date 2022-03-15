import random

presents = ["computer", "airplane", "yacht", "phone"]
print(presents)

index = random.randint(0, len(presents) - 1)
random_item = presents[index]

print("For my birthday, I would like a new " + str(random_item) + ".")
