import random
import matplotlib.pyplot as plt

def practice_with_dice():
    """
    Simulates 1000 throws of two dice, counts how many times doubles (same value on both dice) occur,
    and prints the percentage of double throws.
    """
    double_count = 0  # Counter for double throws

    # Loop for 1000 dice throws
    for i in range(1, 1001):
        dice_1 = random.randint(1, 6)  # First dice roll
        dice_2 = random.randint(1, 6)  # Second dice roll

        # Print the total value of the two dice
        print(f"throw {i}: total value of 2 dice = {dice_1 + dice_2}")

        # Check if a double occurred
        if dice_1 == dice_2:
            print(f"        Yes, we have a double: {dice_1}+{dice_2}")
            double_count += 1

    # Print the percentage of double throws
    print(f"The percentage of double throws = {double_count / 10} percent")

def throw_two_dice():
    """
    Simulates the throw of two six-sided dice and returns the sum of their values.

    Returns:
    int: The sum of two dice values.
    """
    dice_1 = random.randint(1, 6)  # First dice roll
    dice_2 = random.randint(1, 6)  # Second dice roll

    return dice_1 + dice_2

def simulate_monopoly(starting_money):
    """
    Simulates a Monopoly game where a player starts with a fixed amount of money
    and rolls two dice to move around the board. The player can purchase properties,
    and the game ends when all properties are owned.

    Parameters:
    starting_money (int): Initial amount of money the player has.

    Returns:
    int: The number of dice rolls it took to acquire all properties.
    """
    count = 1  # Counter for the number of moves
    position_total = 0  # Total position on the board
    total_lap = 0  # Count of laps completed around the board

    # List of board property values, including non-purchasable spaces (0)
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]

    # List to track property ownership (1 = owned, 0 = not owned)
    possessions = [0] * 40 # Neat trick that I googled

    # The game continues until all properties are owned
    while sum(possessions) != 28:

        # Roll two dice and move the player
        move = throw_two_dice()
        position_total += move
        position_board = position_total % 40  # Current position on the board
        current_lap = position_total // 40  # Count of completed laps

        # Check if the player completed a lap, award $200
        if total_lap < current_lap:
            starting_money += 200
            total_lap += 1

        # Determine the type of the space (empty or street)
        position_type = 'empty' if board_values[position_board] == 0 else 'street'

        # If the space is a street and is not yet owned, the player buys it
        if position_type != 'empty' and possessions[position_board] == 0:
            if board_values[position_board] <= starting_money:
                possessions[position_board] = 1  # Mark the property as owned
                starting_money -= board_values[position_board]  # Deduct cost
                board_values[position_board] = 0  # Mark property as unavailable

        count += 1  # Increment move counter

    return count  # Return the number of moves it took to own all properties

def simulate_monopoly_games(total_games, starting_money):
    """
    Simulates multiple Monopoly games and plots a histogram of the game lengths.

    Parameters:
    total_games (int): The number of games to simulate.
    starting_money (int): Initial amount of money the player starts with.

    Returns:
    float: The average number of dice rolls it took to acquire all properties.
    """
    game_length = []  # List to store the number of throws for each game

    # Simulate the specified number of games
    for game in range(total_games):
        number_of_throws = simulate_monopoly(starting_money)  # Simulate one game
        game_length.append(number_of_throws)  # Store the result

    # Plot a histogram of the game lengths
    plt.hist(game_length, bins=50, range=(28, max(game_length)), edgecolor='black')
    plt.xlabel('Game length')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of Game length for {total_games} games')
    plt.show()

    # Print average game length and other details
    average_game_length = sum(game_length) / len(game_length)
    print(f"Monopoly simulator: 1 player, {starting_money} euros starting money, {total_games} games")
    print(f"It took an average of {average_game_length} throws for the player to collect all streets")

    return average_game_length

def main():
    """
    Main function to simulate multiple Monopoly games with a starting amount of money.
    """
    simulate_monopoly_games(10000, 1500)  # Simulate 10,000 games with a starting money of 1500

if __name__ == '__main__':
    main()
