import art
from os import system

print(art.logo)

all_users = []
while True:
    user_name = input("Enter your name: ")
    user_bid = input("Enter your bid: ")
    all_users.append({user_name: user_bid})

    more_users = input("Are there more users to bid? (y/n) ")
    if more_users == 'y':
        system('cls')
        continue
    else:
        break

# Set initial max bid and bidder
max_bidder = None
max_bid = 0

# Check all users bids and update max
for user in all_users:
    for bidder in user:
        if int(user.get(bidder)) > max_bid:
            max_bidder = bidder
            max_bid = int(user.get(bidder))

print(f"{max_bidder} is the highest bidder with {max_bid} dollars!")
