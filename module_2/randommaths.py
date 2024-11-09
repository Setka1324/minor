import random

def random_math():
    """
    Simulates a process where random numbers are repeatedly generated and summed until the sum
    exceeds 1. This process is repeated 1,000,000 times, and the function calculates the average
    number of random numbers needed for the sum to exceed 1 across all trials.

    The function returns the average number of random numbers required for the sum to exceed 1.

    Returns:
    float: The average count of random numbers needed for the sum to exceed 1.
    """

    avarage_results = 0  # Initialize the total sum of counts across all trials
    for _ in range(1000000):  # Perform 1,000,000 trials

        avarage = 0  # Reset the sum of random numbers for this trial
        count = 0  # Reset the counter for the number of random numbers generated

        # Continue generating random numbers until the sum exceeds 1
        while avarage < 1.00:
            avarage += random.random()  # Add a random number to the current sum
            count += 1  # Increment the count of numbers generated

        # Accumulate the count from this trial, adjusted by the total number of trials
        avarage_results += count * 0.000001

    return avarage_results  # Return the average count of random numbers needed


print(f"The average amount of numbers generated (based on 1 million trials) is: {random_math()}")
