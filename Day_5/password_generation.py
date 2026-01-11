import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print(f"Welcome to the password generation program!")
nr_letters = int(input("How many letters would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
nr_symbols = int(input("How many symbols would you like? "))

#Easy level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# print(f"Your password is: {password}")

# Hard level

# password_list = []
# for char in range(nr_letters):
#     password_list.append(letters[char])
# print(password_list)
# for char in range(nr_numbers):
#     password_list.append(numbers[char])
# print(password_list)
# for char in range(nr_symbols):
#     password_list.append(symbols[char])
# print(password_list)
#
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#     password += char
# print(f"Your password is: {password}")

# with condition first and last character are letters
password_list = []
for char in range(nr_letters):
    password_list.append(letters[char])
print(password_list)
for char in range(nr_numbers):
    password_list.append(numbers[char])
print(password_list)
for char in range(nr_symbols):
    password_list.append(symbols[char])
print(password_list)

random.shuffle(password_list)








