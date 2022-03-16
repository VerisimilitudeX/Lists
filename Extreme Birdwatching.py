#### ---- SET UP ---- ####

# --- Library --- #
import random

# --- Lists --- #
birds = ["Actitis macularius", "Aix sponsa", "Amphispiza bilineata", "Anas acuta", "Anas americana", "Anas clypeata", "Anas crecca", "Anas discors"]
adj = ["great", "live", "startled", "blue", "rare", "powerful", "wretched", "chirping", "royal", "stuffed", "tropical"]
boasts = ["with my eyes closed", "from across a crowded forest", "before breakfast", "from over 1000 yards", "while sleeping", "single-handedly"]
q = []

#### ---- MAIN LOOP ---- ####
while q != "quit":
    q = input("Input enter or quit")

    #### ---- GET RANDOM CHOICES ---- ####

    # --- Random bird --- #
    index = random.randint(0, len(birds) - 1)
    bird_choice = birds[index]

    # --- Random adjective --- #
    index = random.randint(0, len(adj) - 1)
    adj_choice = adj[index]

    # --- Random boast --- #
    index = random.randint(0, len(boasts) - 1)
    boast_choice = boasts[index]

    #### ---- OUTPUT ---- ####
    print("Well, I spotted a " + adj_choice + " " + bird_choice + " " + boast_choice + "!")
    print()
