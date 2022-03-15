# --- Setup --- #
animals = []
animal = ""
# --- Enter animals --- #

while animal != "done":
    animal = input("Enter an animal (done to exit) ")
    if animal == "done":
        break
    animals.append(animal)

# --- Print results --- #
cage = "+===============+"
index = 0
print("ZOO MAP:")
print(cage)
while index < len(animals):
    row = "| " + animals[index]
    spaces = 14 - len(animals[index])
    while spaces > 0:
        row += " "
        spaces -= 1
    row += "|"
    print(row)
    print(cage)
    index += 1
