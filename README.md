# Game_Dice_2001

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

## Requirements

- Python 3.x

## Usage

1. Clone the repository.
2. Open the file `guessing_game.py` in your Python IDE (such as PyCharm).
3. Run the file.
4. Follow the instructions on the screen to play the game.

## Author

zyniu81

## License

This project is licensed under the MIT License - see the LICENSE file for details.
