#### ---- SETUP ---- ####
import random
people = []
user_name = ""

#### ---- INPUT LOOP ---- ####
while user_name != "done":

    # --- Add new name to list --- #
    user_name = input("Enter a name (or done): ")
    if user_name == "done":
        break
    people.append(user_name)

# --- Pick who the vampire is --- #    
index = random.randint(0, len(people) - 1)
random_person = people[index]
print()

#### ---- GUESSING LOOP ---- ####
while len(people) > 1:

    # --- User guess --- #
    print(people)
    guess = input("Who do you think the vampire is? ")

    # --- Check for correct answer --- #
    if guess == random_person:
        print("Congratulations! ")
        break

    # --- Remove incorrect guess --- #
    if guess in people:
        print("You were incorrect. ")
        people.remove(guess)
    print()

#### ---- FINAL OUTPUT ---- ####
if len(people) == 1:
    print("You didn't guess it in time. The vampire was " + str(random_person) + ". ")
