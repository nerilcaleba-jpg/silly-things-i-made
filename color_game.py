# color game
import random
cube_color_list = ['red', 'blue', 'yellow', 'green', 'pink', 'orange']
cube_1_color = ''
cube_2_color = ''
starting_credit = 25
current_credits = 25
credit_goal = 100
print("color game start")
while current_credits < credit_goal:
    chosen_color = str(input("place your bets on 1 color: ")
                       )  # must be in the color list
    # don't gamble more credits than what you have
    gambled_credits = int(input("credits to be gambled: "))
    current_credits = current_credits - gambled_credits

    cube_1_color = random.choice(cube_color_list)
    cube_2_color = random.choice(cube_color_list)

    print(f"cube 1 is {cube_1_color} and cube 2 is {cube_2_color}")

    if chosen_color != cube_1_color or cube_2_color:
        print("no cube gave you a win")
    elif chosen_color == cube_1_color or cube_2_color:
        current_credits = current_credits + (gambled_credits * 2)
        print("one cube gave you a win")
    elif chosen_color == cube_1_color and cube_2_color:
        current_credits = current_credits + (gambled_credits * 3)
        print("both cubes gave you a win")

    print(f"your current credits is {current_credits}")

    if current_credits >= credit_goal:
        print("you have reached the credit goal and you win the game")
        break
    elif current_credits <= 0:
        print("you have lost all you credits and you lost the game")
        break
    print("next round start")
