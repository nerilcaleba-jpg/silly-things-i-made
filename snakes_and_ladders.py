# snakes and ladders
import random 
finish_line_position = 50
snake_positions = [6, 13, 21, 34, 49]
ladder_positions = [7, 15, 24, 37, 45]
ladder_boost = 5
snake_setback = 5
player_1_postion = 0
player_2_postion = 0
player_1 = "mark" # players can be any name
player_2 = "john"  # players can be any name
winner = ""
game_started = True
print("snake and ladders")
print("where the ladders boosts you 5 positions and ladders set you back 5 positions")
print(f"the ladders are in positions {ladder_positions}")
print(f"the snakes are in positions {snake_positions}")

while game_started == True:
    command = input("input 'roll' to start: ") 
    # position function
    if command == 'roll':
        # for player 1
        player_1_roll = random.randint(1, 6)
        player_1_postion = player_1_postion + player_1_roll
        print(f"player 1 moved {player_1_roll} positons")

        # for player 2
        player_2_roll = random.randint(1, 6)
        player_2_postion = player_2_postion + player_2_roll
        print(f"player 1 moved {player_2_roll} positons")

        # snake or ladder check
        if player_1_postion in snake_positions:
            player_1_postion -= snake_setback
            print(f"the player 1 is landed on a snake")
        elif player_1_postion in ladder_positions:
            player_1_postion += ladder_boost
            print(f"the player 1 landed on a ladder")

        if player_2_postion in snake_positions:
            player_2_postion -= snake_setback
            print(f"the player 2 is landed on a snake")
        elif player_2_postion in ladder_positions:
            player_2_postion += ladder_boost
            print(f"the player 2 landed on a ladder")

        # position display
        print(f"player 1 position is {player_1_postion}")
        print(f"player 2 position is {player_2_postion}")

        # winner check
        if player_1_postion >= finish_line_position:
            winner = player_1
            print(f"the winner of this match is {winner}")
            break

        elif player_2_postion >= finish_line_position:
            winner = player_2
            print(f"the winner of this match is {winner}")
            break
