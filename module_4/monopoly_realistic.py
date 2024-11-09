import random
import matplotlib.pyplot as plt

def throw_two_dice():
    """
    Simulates the throw of two six-sided dice and returns the sum of their values.

    Returns:
    int: The sum of two dice values.
    """
    dice_1 = random.randint(1, 6)  # First dice roll
    dice_2 = random.randint(1, 6)  # Second dice roll

    return dice_1 + dice_2

def simulate_monopoly(starting_money_p1=1500, starting_money_p2=1500):
    """
    Simulates a Monopoly game with two players, tracking property ownership until all properties are owned.

    Parameters:
    starting_money_p1 (int): Starting money for player 1.
    starting_money_p2 (int): Starting money for player 2.

    Returns:
    int: The difference in the number of properties owned by player 1 and player 2 at the end of the game.
    """
    starting_money = [starting_money_p1, starting_money_p2]  # Initial money for both players
    position_total = [0, 0]  # Tracks each player's position on the board
    total_lap = [0, 0]  # Tracks laps completed by each player
    # List of property values on the Monopoly board
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]

    # Tracks property ownership for both players, initially set to 0 (not owned)
    possessions_origin = [0] * 40
    possessions = [possessions_origin[:], possessions_origin[:]] # Another neat trick. Otherwise python doesn't see difference between 2 lists

    # The game continues until all 28 purchasable properties are owned
    while not(sum(possessions[0]) + sum(possessions[1]) == 28):

        # Both players throw two dice
        move = [throw_two_dice(), throw_two_dice()]
        position_total[0] += move[0]
        position_total[1] += move[1]
        # Determine each player's position on the board
        position_board = [position_total[0] % 40, position_total[1] % 40]
        # Calculate completed laps
        current_lap = [position_total[0] // 40, position_total[1] // 40]
        # Determine if the current position is a street or an empty space
        position_type = [('empty' if board_values[position_board[0]] == 0 else 'street'),
                         ('empty' if board_values[position_board[1]] == 0 else 'street')]

        # Award $200 for completing a lap
        for i in range(len(starting_money)):
            if total_lap[i] < current_lap[i]:
                starting_money[i] += 200
                total_lap[i] += 1

        # Check if the property is available for purchase by either player
        for i in range(len(starting_money)):
            if (position_type[i] != 'empty') and (possessions[0][position_board[i]] == 0) and (possessions[1][position_board[i]] == 0):
                if board_values[position_board[i]] <= starting_money[i]:
                    # Player buys the property if they can afford it
                    possessions[i][position_board[i]] = 1
                    starting_money[i] -= board_values[position_board[i]]
                    board_values[position_board[i]] = 0

    # Return the difference in property ownership between player 1 and player 2
    return sum(possessions[0]) - sum(possessions[1])

def simulate_monopoly_games(total_games, starting_money_1=1500, starting_money_2=1500):
    """
    Simulates multiple Monopoly games and calculates the average difference in the number of properties
    owned by player 1 and player 2 after all properties have been bought.

    Parameters:
    total_games (int): The number of games to simulate.
    starting_money_1 (int): Initial amount of money for player 1.
    starting_money_2 (int): Initial amount of money for player 2.

    Returns:
    float: The average difference in property ownership between player 1 and player 2.
    """
    game_differences = []  # List to store the results of each game

    # Simulate the specified number of games
    for game in range(total_games):
        game_difference = simulate_monopoly(starting_money_1, starting_money_2)
        game_differences.append(game_difference)

    # Return the average difference in property ownership between player 1 and player 2
    return sum(game_differences) / len(game_differences)

def equilibrium():
    """
    Simulates a series of Monopoly games where player 2's starting money is gradually increased,
    and plots the results showing how the difference in property ownership changes.

    Returns:
    list: A list of the results of each simulation (differences in property ownership).
    """
    x_values = []  # List of starting money values for player 2
    results = []  # List of results (differences in property ownership)

    # Simulate games for different starting amounts of money for player 2
    for i in [0, 50, 100, 150, 200]:
        result = simulate_monopoly_games(10000, 1500, 1500 + i)
        results.append(result)
        x_values.append(1500 + i)

    # Plot the results
    plt.plot(x_values, results, 'bo-')
    plt.xlabel('Player 2 Starting Money', fontsize=15)
    plt.ylabel('Difference in Property Ownership', fontsize=15)
    plt.show()

    return results

def main():
    """
    Main function to simulate Monopoly games and analyze the results of two players
    """
    result = simulate_monopoly_games(10000)
    print("Monopoly simulator: two players, 1500 euro starting money, 10000 games",
          f"On average player 1 has {result} more streets in their possession when all streets have been bought",
          sep="\n")

    equilibrium()  # Simulate and print the results of the equilibrium experiment
    print("Monopoly simulator: 2 players",
          "On average, if player 2 receives 100 euros more starting money, both players collect an equal number of streets",
          sep="\n")

if __name__ == '__main__':
    main()
