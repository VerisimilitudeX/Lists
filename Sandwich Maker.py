import random
running = True
ingr_list = []

while running:
    user_input = input("Enter an ingredient: [done to end ingredient collection] ")
    if user_input == "done":
        break
    else:
        ingr_list.append(user_input)
        
num_index = 0
sand_ingr = []

while num_index < 3:
    index = random.randint(0, len(ingr_list) - 1)
    ingr = ingr_list[index]
    sand_ingr.append(ingr)
    num_index += 1
    
print("Make a sandwich out of " + str(sand_ingr))
