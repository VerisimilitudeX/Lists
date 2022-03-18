grocery_list = []
new_item = ""
running = True

while running:
    remove_add = input("Do you want to add or remove an item? [add/remove/quit]")
    if remove_add == "add":
        new_item = input("What do you want to add to the grocery list? ")
        grocery_list.append(new_item)
    elif remove_add == "remove":
        new_item = input("What do you want to remove from the grocery list? ")
        if new_item in grocery_list:
            grocery_list.remove(new_item)
    else:
        running = False
    print("Here is your current grocery list: " + str(grocery_list))
