import random

presents = ["computer", "airplane", "yacht", "phone"]
print(presents)

index = random.randint(0, len(presents) - 1)
random_item = presents[index]

print(random_item)
