import random
import math

# I used AI to generate text for docstrings/comments, I hope thats ok

def square(n):
    """
    Simulates a process where random differences in x and y coordinates are generated,
    calculates the Euclidean distance (delta) for each pair of differences, and then
    returns the average of these distances over n iterations.

    Parameters:
    n (int): The number of iterations to perform.

    Returns:
    float: The average Euclidean distance after n iterations.
    """

    avarage_total = 0  # Initialize the sum for averaging

    for _ in range(n):
        # Generate random differences for x and y coordinates
        x_dif = random.random() - random.random()
        y_dif = random.random() - random.random()

        # Calculate the Euclidean distance between the two points
        delta = math.sqrt(x_dif**2 + y_dif**2)

        # Accumulate the weighted delta to the total
        avarage_total += delta * (1/n)

    return avarage_total  # Return the computed average distance
