# --- Setup  --- #
flavors = ["Black Raspberry", "Butterscotch", "Chocolate", "Coconut", "Coffee", "Cookie Dough", "Ketchup", "Lavender", "Mango", "Mint Chip", "Strawberry", "Vanilla"]
favorites = []
count = 0

# --- Loop until five flavors are chosen --- #
while count < 5:

    # --- Print options --- #
    print("Flavors to choose from: ")
    index = 0
    while index < len(flavors):
        print("   -" + flavors[index])
        index += 1

    # --- Record favorite --- #
    favorite = input("What is your favorite flavor? ")

    # --- Increase counter --- #
    count += 1

# --- Print results --- #
print()
print("Your Flavor Rankings:")
index = 0
while index < len(favorites):
    print(str(index + 1) + ". " + favorites[index])
    index += 1
