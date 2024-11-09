from time import time
from random import randint

# Function to measure performance of 'in' operation on lists
def measure_list_performance(n, iterations):
    test_list = list(range(n))  # Create a list with n elements (0 to n-1)
    start = time()
    for _ in range(iterations):
        test_value = randint(0, n*2)  # Generate a random value to search for
        test_value in test_list  # Test if this value is in the list
    end = time()
    return end - start

# Function to measure performance of 'in' operation on dictionaries
def measure_dict_performance(n, iterations):
    test_dict = {i: None for i in range(n)}  # Create a dictionary with n elements (0 to n-1)
    start = time()
    for _ in range(iterations):
        test_value = randint(0, n*2)  # Generate a random value to search for
        test_value in test_dict  # Test if this value is in the dictionary
    end = time()
    return end - start

# Main experiment setup
sizes = [10, 100, 1000, 10000, 100000]  # Sizes of lists and dictionaries to test
iterations = 100000  # Number of times to repeat the 'in' operation

# Measuring and displaying the results
print(f"{'Size':<10}{'List Time (s)':<15}{'Dict Time (s)'}")
for size in sizes:
    list_time = measure_list_performance(size, iterations)
    dict_time = measure_dict_performance(size, iterations)
    print(f"{size:<10}{list_time:<15.2f}{dict_time:.2f}")
