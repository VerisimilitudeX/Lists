count = 0
user_list = []
while count < 10:
    user_input = int(input("Enter 10 integers: "))
    user_list.append(user_input)
    count += 1
while 0 in user_list:
    user_list.remove(0)
print(user_list)
