import random
import matplotlib.pyplot as plt

def sum_random_numbers():
    """
    Simulates summing 100 random numbers (generated between 0 and 1) across 100,000 trials,
    plots a histogram of the sums, and calculates the percentage of trials where the sum
    is less than 42 or greater than 58.

    The function performs the following tasks:
    1. Simulates 100,000 trials, where each trial generates and sums 100 random numbers.
    2. Plots a histogram of the sums with 50 bins, ranging from 30 to 70.
    3. Calculates and prints the percentage of trials where the sum is less than 42.
    4. Calculates and prints the percentage of trials where the sum is greater than 58.

    Parameters:
    None

    Returns:
    None
    """
    sums = []

    # Perform 100,000 trials
    for _ in range(100000):
        random_numbers = 0
        for _ in range(100):
            random_numbers += random.random()
        sums.append(random_numbers)

    # Create a histogram of the sums
    plt.hist(sums, bins=50, range=(30, 70), edgecolor='black')
    plt.xlabel('Sum of 100 Random Numbers')
    plt.ylabel('Frequency')
    plt.title('Histogram of Sum of 100 Random Numbers')
    plt.show()

    # Calculate percentage of sums less than 42
    less_than_42 = []
    for s in sums: # I do not use [s for s in sums if s < 42] and then sum() Cause I'm not sure if we are allowed to. Same for above while generating random results
        if s < 42:
             less_than_42.append(s)
    percentage_less_than_42 = (len(less_than_42) / 100000) * 100
    print(f"The percentage of experiments with a sum lower than 42 is: {percentage_less_than_42:.4f}%") # 4.f just so it looks good visually

    # Calculate percentage of sums greater than 58
    more_than_58 = []
    for s in sums:
        if s > 58:
            more_than_58.append(s)
    percentage_more_than_58 = (len(more_than_58) / 100000) * 100
    print(f"The percentage of experiments with a sum higher than 58 is: {percentage_more_than_58:.4f}%")

sum_random_numbers()
