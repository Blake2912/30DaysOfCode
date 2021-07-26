# Today is Day8 and I will be making a snakes and ladder game
# The player needs to reach 100 to win, here I am taking 2 players
import random
import pyfiglet

position_of_snakes = [3, 10, 13, 22, 38, 45, 51, 62, 77, 86, 93, 98]
position_of_ladder = [5, 12, 33, 23, 44, 50, 60, 89]
position_of_player_one = 1
position_of_player_two = 1


def roll_dice():
    return random.randint(1, 6)


def move_back():
    return random.randint(1, 15)


def bonus_moves():
    return random.randint(1, 10)


welcome_line = pyfiglet.figlet_format("Welcome to Snakes and Ladders")
print(welcome_line)
print("This game is currently limited to two players only!")
while True:
    start_query = input("Do you want to start the game?\n").lower()
    if start_query == "yes":
        print("Welcome to the game please follow the following instructions")
        print("You will be asked to enter the player's name and then you need to type 'roll' to\n"
              "roll the dice, then the game will take care of everything you just need to type 'roll'\n"
              "when prompted! all the best for this game... :)\n")
        player_one_name = input("Enter the name of player one: ")
        player_two_name = input("Enter the name of player two: ")
        print("{0}'s Position -> {1}".format(player_one_name, position_of_player_one))
        print("{0}'s Position -> {1}".format(player_two_name, position_of_player_two))
        while position_of_player_one != 100 or position_of_player_two != 100:
            p1 = input("{} type 'roll' to roll the dice: ".format(player_one_name)).lower()
            if p1 == 'roll':
                number_dice = roll_dice()
                print("You rolled: {}".format(number_dice))
                position_of_player_one = position_of_player_one + number_dice
                if position_of_player_one > 100:
                    position_of_player_one = position_of_player_one - number_dice
                    print("Position of {0} -> {1}".format(player_one_name, position_of_player_one))
                else:
                    for i in position_of_snakes:
                        if position_of_player_one == i:
                            move_back_steps = move_back()
                            position_of_player_one = position_of_player_one - move_back_steps
                            print("You landed on a snake so you need to move back {} spaces".format(move_back_steps))
                            if position_of_player_one <= 0:
                                position_of_player_one = 1
                            print("Position of {0} -> {1}".format(player_one_name, position_of_player_one))
                    for i in position_of_ladder:
                        if position_of_player_one == i:
                            move_ahead = bonus_moves()
                            position_of_player_one = position_of_player_one + move_ahead
                            print("You have landed on a ladder so you move ahead by {} spaces".format(move_ahead))
                            print("Position of {0} -> {1}".format(player_one_name, position_of_player_one))
                    print("You are safe!")
                    print("Position of {0} -> {1}".format(player_one_name, position_of_player_one))
            else:
                print("Wait till for your next turn and type roll properly!")
            p2 = input("{} type 'roll' to roll the dice: ".format(player_two_name)).lower()
            if p2 == 'roll':
                number_dice = roll_dice()
                print("You rolled: {}".format(number_dice))
                position_of_player_two = position_of_player_two + number_dice
                if position_of_player_two > 100:
                    position_of_player_two = position_of_player_two - number_dice
                    print("Position of {0} -> {1}".format(player_two_name, position_of_player_two))
                else:
                    for i in position_of_snakes:
                        if position_of_player_two == i:
                            move_back_steps1 = move_back()
                            position_of_player_two = position_of_player_two - move_back_steps1
                            print("You landed on a snake so you need to move back {} spaces".format(move_back_steps1))
                            if position_of_player_two <= 0:
                                position_of_player_two = 1
                            print("Position of {0} -> {1}".format(player_two_name, position_of_player_two))
                    for i in position_of_ladder:
                        if position_of_player_two == i:
                            move_ahead1 = bonus_moves()
                            position_of_player_two = position_of_player_two + move_ahead1
                            print("You have landed on a ladder so you move ahead by {} spaces".format(move_ahead1))
                            print("Position of {0} -> {1}".format(player_two_name, position_of_player_two))
                    print("You are safe!")
                    print("Position of {0} -> {1}".format(player_two_name, position_of_player_two))
            else:
                print("Wait till for your next turn and type roll properly!")
            if position_of_player_one == 100:
                break
            elif position_of_player_two == 100:
                break
            else:
                continue
        print("{0}'s Position -> {1}".format(player_one_name, position_of_player_one))
        print("{0}'s Position -> {1}".format(player_two_name, position_of_player_two))
        if position_of_player_one == 100:
            print("{} wins!".format(player_one_name))
        else:
            print("{} wins!".format(player_two_name))
        break
    elif start_query == "no":
        print("Come back later and type yes to start playing!")
        break
    else:
        print("Type yes or no, type yes to start playing!")
