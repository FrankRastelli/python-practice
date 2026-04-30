import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("Player number", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_idx], "\n")
        roll_result = 0
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                roll_result = 0
                player_scores[player_idx] -= current_score
                current_score = 0
                break
            else:
                roll_result = 0
                roll_result += value
                current_score += value
                print("You rolled a:", value)
                player_scores[player_idx] += roll_result

            print("Your current score is:", player_scores[player_idx])

        print("Your total score is:", player_scores[player_idx], "\n")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner!")