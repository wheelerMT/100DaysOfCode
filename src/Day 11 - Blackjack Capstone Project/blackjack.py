import art
import random


def start_game():
    play = input("Do you want to play a game of blackjack? (y/n): ")
    if play == "n":
        exit("Thanks for playing!")
    else:
        deal_cards()


def deal_cards():
    computer_cards = []
    player_cards = []

    # Generate initial two cards
    for _ in range(2):
        computer_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))

    # If sum of dealers cards is less than 14 then add another card
    while sum(computer_cards) <= 14:
        computer_cards.append(random.choice(cards))

    print("Your current cards are: {}".format(player_cards))
    print("The dealers first card is: {}".format(computer_cards[0]))

    another_card(player_cards, computer_cards)


def another_card(player_cards, computer_cards):
    another_c = input("Do you want another card? (y/n): ")

    if another_c == "y":
        player_cards.append(random.choice(cards))

        # ! Check if now bust:
        while sum(player_cards) > 21:
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
            else:
                print("You bust! You had: {}".format(player_cards))
                print("The computer had {}".format(computer_cards))
                print("=============================================")
                start_game()
        print("Your current cards are: {}".format(player_cards))
        another_card(player_cards, computer_cards)
    else:
        determine_winner(player_cards, computer_cards)


def determine_winner(player_cards, computer_cards):
    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)

    if player_sum > computer_sum:
        print("You win!")
        print("You won with the hand: {}".format(player_cards))
        print("The computer had {}".format(computer_cards))
        print("=============================================")
    elif player_sum <= 21 and computer_sum > 21:
        print("You win!")
        print("You won with the hand: {}".format(player_cards))
        print("The computer had {}".format(computer_cards))
        print("=============================================")
    elif player_sum == computer_sum:
        print("Draw!")
        print("The computer had {}".format(computer_cards))
        print("You had: {}".format(player_cards))
        print("=============================================")
    else:
        print("You lost!")
        print("The computer had {}".format(computer_cards))
        print("You had: {}".format(player_cards))
        print("=============================================")

    start_game()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)
start_game()
