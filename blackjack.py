from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 0
game_com = -1  # separate from game_num for calculations in option 3
player_wins = 0
dealer_wins = 0
tie_games = 0
card_str = ''

while game_continue:
    game_num += 1  # keeps user updated on which number game they are on after the game ends
    game_com += 1  # this is for calculating the number of games and percentage in option 3
    print(f"START GAME #{game_num}")
    player_hand = 0
    card = rng.next_int(13) + 1  # [1, 13], deals user a card in the range
    if card == 1:
        card_str = 'ACE'
        card = 1
    elif card == 11:
        card_str = 'JACK'
        card = 10
    elif card == 12:
        card_str = "QUEEN"
        card = 10
    elif card == 13:
        card_str = "KING"
        card = 10
    else:
        card_str = str(card)  # gives cards that are just the face value, not Ace, Jack, etc.
    player_hand += card  # adding the given card to the player's hand
    print(f'\nYour card is a {card_str}!')  # prints the given card
    print(f'Your hand is: {player_hand}')  # prints the player's hand

    no_winner = True
    while no_winner:
        dealer_hand = 0
        print('''
1. Get another card
2. Hold hand
3. Print statistics
4. Exit''')
        option = int(input("\nChoose an option: "))  # asks user to pick an option from the menu above
        if option == 1:
            card = rng.next_int(13) + 1  # deals another card to the player
            if card == 1:
                card_str = 'ACE'
                card = 1
            elif card == 11:
                card_str = 'JACK'
                card = 10
            elif card == 12:
                card_str = "QUEEN"
                card = 10
            elif card == 13:
                card_str = "KING"
                card = 10
            else:
                card_str = str(card)
            player_hand += card
            print(f'\nYour card is a {card_str}!')
            print(f'Your hand is: {player_hand}')
            # below: prints out the message depending on if player/dealer wins, adds increments of 1 to winner
            # for calculations in option 3
            if player_hand == 21:
                print("\nBLACKJACK! You win!\n")
                player_wins += 1
                no_winner = False  # gets out of nested loop
            elif player_hand > 21:
                no_winner = False
                print("\nYou exceeded 21! You lose.\n")
                dealer_wins += 1
        elif option == 2:
            dealer_hand = rng.next_int(11) + 16  # deals a card to the dealer
            print(f"\nDealer's hand: {dealer_hand}")  # shows dealer hand versus the player hand
            print(f"Your hand is: {player_hand}")
            # below: prints out the message depending on win/lose, adds increments of 1 to winner for option 3
            # no_winner = False exits the nested loop
            if dealer_hand > 21:
                print('\nYou win!\n')
                player_wins += 1
                no_winner = False
            elif dealer_hand == 21:
                print('\nDealer wins!\n')
                dealer_wins += 1
                no_winner = False
            elif player_hand == 21:
                print('\nBLACKJACK! You win!\n')
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print('\nYou exceeded 21! You lose.\n')
                dealer_wins += 1
                no_winner = False
            elif dealer_hand > player_hand:  # if the player hand is less than the dealer hand, win goes to dealer
                print('\nDealer wins!\n')
                dealer_wins += 1
                no_winner = False
            elif player_hand == dealer_hand:
                print("\nIt's a tie! No one wins!\n")
                tie_games += 1
                no_winner = False
        elif option == 3:
            print(f'\nNumber of Player wins: {player_wins}')
            print(f'Number of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {tie_games}')
            print(f'Total # of games played is: {game_com}')
            print(f'Percentage of Player wins: {((player_wins / game_com) * 100): .1f}%')
        elif option == 4:
            no_winner = False
            game_continue = False
            # gets out of inner loop > gets outside of outer loop > breaks
        else:
            print('\nInvalid input!')
            print('Please enter an integer value between 1 and 4.')
            # forces user to input a number on the list
