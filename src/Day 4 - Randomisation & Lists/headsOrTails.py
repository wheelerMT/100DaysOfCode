import random

random_int = random.randint(0, 1)  # 0 for Tails, 1 for Heads

if random_int == 1:
    print('Heads')
elif random_int == 0:
    print('Tails')
