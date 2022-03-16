int_list = []
new_int = 0

while new_int >= 0:
    new_int = int(input("Please enter a positive integer: "))
    if new_int < 0:
        break
    if not (new_int in int_list):
        int_list.append(new_int)
