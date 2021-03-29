import random

names_string = input("Enter everybody's names, separated by a comma. \n")
names = names_string.split(", ")  # Splits the input according to the parameter passed in split

# Choose randomly from names list and print result
print(f'{random.choice(names)} will pay the bill!')
