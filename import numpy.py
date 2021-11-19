input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
print('list: ', user_list)
# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
x = float(1/1/user_list)


