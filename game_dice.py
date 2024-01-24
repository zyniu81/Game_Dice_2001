import random


def game_dice(n=4):
    """
    Simulates a dice game between a user and a computer.

    The game continues until either the user or the computer reaches a score of 2001 or more.

    Parameters:
        n (int): Number of dice rolls in each round. Default is 2.

    Rules:
        - If the sum of the dice rolls is 11, the player's current score is multiplied by 11.
        - If the sum of the dice rolls is 7, the player's current score is divided by 7.
        - Otherwise, the sum of the dice rolls is added to the player's current score.

    The game displays the results of the initial round, the current score of the user and the computer,
    and announces the winner when one of them reaches a score of 2001 or more.

    Pressing Enter allows the user to roll the dice for each round.

    Interrupting the game with a KeyboardInterrupt (e.g., pressing Ctrl+C) gracefully exits the game.

    Note:
        This code uses input() to pause the game for the user to press Enter, and it relies on random
        module for simulating dice rolls.

    """
    user_list = []
    computer_list = []
    user = input("Press Enter")
    rounds_sum_user = sum(random.randint(1, 6) for _ in range(n))
    user_list.append(rounds_sum_user)
    print(rounds_sum_user)
    rounds_sum_computer = sum(random.randint(1, 6) for _ in range(n))
    computer_list.append(rounds_sum_computer)
    print(rounds_sum_computer)
    print(f"User have a {sum(user_list)} pts.")
    print(f"Computer have a {sum(computer_list)} pts.")
    try:
        while sum(user_list) < 2001 and sum(computer_list) < 2001:
            user = input("Press Enter")
            rounds_sum_user = sum(random.randint(1, 6) for _ in range(n))
            print(rounds_sum_user)
            if rounds_sum_user == 11:
                result = sum(user_list) * 11
                user_list.clear()
                user_list.append(result)
            elif rounds_sum_user == 7:
                result = sum(user_list) // 7
                user_list.clear()
                user_list.append(result)
            else:
                user_list.append(rounds_sum_user)

            rounds_sum_computer = sum(random.randint(1, 6) for _ in range(n))
            print(rounds_sum_computer)
            if rounds_sum_computer == 11:
                result = sum(computer_list) * 11
                computer_list.clear()
                computer_list.append(result)
            elif rounds_sum_computer == 7:
                result = sum(computer_list) // 7
                computer_list.clear()
                computer_list.append(result)
            else:
                computer_list.append(rounds_sum_computer)

            print(f"User have a {sum(user_list)} pts.")
            print(f"Computer have a {sum(computer_list)} pts.")
            if sum(user_list) >= 2001:
                print("User win!")
            elif sum(computer_list) >= 2001:
                print("Computer win!")
    except KeyboardInterrupt:
        print(" Interrupted by user")


game_dice()
