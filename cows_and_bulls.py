import random


def num_generator():
    while True:
        computer_num = random.sample("0123456789", 4)
        if computer_num[0] == "0":
            continue
        else:
            break
    computer_num = "".join(computer_num)
    return computer_num


def player_input():
    while True:
        try:
            global player_num
            player_num = input("Enter your number: ")
            if len(player_num) != 4:
                print("Please enter a 4 digit number")
                continue
        except ValueError:
            print("The input you entered is not a number!")
        else:
            x = 0
            for i in range(0, 4):
                x += player_num.count(player_num[i])
            if x != 4:
                print("Enter a number with different digits!")
                continue
            else:
                return


def num_comparison(a, b):
    a = str(a)
    b = str(b)
    for i in range(0, 4):
        for j in range(0, 4):
            if i == j and a[i] == b[j]:
                global bull_count
                bull_count += 1
            elif i != j and a[i] == b[j]:
                global cow_count
                cow_count += 1
            else:
                pass


player_num = 0
user_choice = True
while user_choice:
    cow_count = 0
    bull_count = 0
    game_num = 1234
    score_counter = 0
    while True:
        player_input()
        score_counter += 1
        num_comparison(game_num, player_num)
        if bull_count == 4:
            print("Bull win!")
            print("Bull has completed the game in", str(score_counter), "moves")
            print("Cow's number: ", game_num)
            print("Bull's number: ", player_num)
            print("Cow's score: ", cow_count)
            print("Bull's score: ", bull_count)
            choice = input("Press \"y\" to play again: ")
            if choice.upper() == "Y":
                user_choice = True
            else:
                user_choice = False
            break
        elif cow_count == 4:
            print("Cow win!")
            print("Cow has completed the game in", str(score_counter), "moves")
            print("Cow's number: ", game_num)
            print("Bull's number: ", player_num)
            print("Cow's score: ", cow_count)
            print("Bull's score: ", bull_count)
            choice = input("Press \"y\" to play again: ")
            if choice.upper() == "Y":
                user_choice = True
            else:
                user_choice = False
            break
        else:
            print("Cow's number: ", game_num)
            print("Bull's number: ", player_num)
            print("Cow's score: ", cow_count)
            print("Bull's score: ", bull_count)
            cow_count = 0
            bull_count = 0
