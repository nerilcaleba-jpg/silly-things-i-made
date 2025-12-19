# random rock paper scissors
# it works hell yeah
import random
hand_list = ['rock', 'paper', 'scissors']
player_1_hand_input = input("choose player 1 hand: ")
player_2_hand_input = input("choose player 2 hand: ")
winner = ""
match_started = True

while match_started == True:
    print("round start")
    # played hand if input is random
    if player_1_hand_input == 'random':
        player_1_hand_input = random.choice(hand_list)
    if player_2_hand_input == 'random':
        player_2_hand_input = random.choice(hand_list)
    player_1_hand = player_1_hand_input
    player_2_hand = player_2_hand_input
    # prints players' hands
    print(f"player 1's hand is {player_1_hand}")
    print(f"player 2's hand is {player_2_hand}")
    # winner check
    if player_1_hand == player_2_hand:
        winner = "draw"
        print("the round is a draw")
        break
    elif (player_1_hand == 'rock' and player_2_hand == 'scissors') \
            or (player_1_hand == 'scissors' and player_2_hand == 'paper')\
            or (player_1_hand == 'paper' and player_2_hand == 'rock'):
        winner = "player 1"
    elif (player_1_hand == 'rock' and player_2_hand == 'paper')\
            or (player_1_hand == 'paper' and player_2_hand == 'scissors')\
            or (player_1_hand == 'scissors' and player_2_hand == 'rock'):
        winner = "player 2"
    if winner == "player 1" or "player 2":
        print(f"the winner is {winner}")
        break
