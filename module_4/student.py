import math
import matplotlib.pyplot as plt
import random

# TA said its good ¯\_(ツ)_/¯

def arange(start, stop, step):
    """
    Generate a list of numbers starting from `start` to `stop`,
    with a given step increment.

    Parameters:
    start (float): The starting value of the sequence.
    stop (float): The end value of the sequence (exclusive).
    step (float): The increment between values.

    Returns:
    list: A list of floating-point numbers incremented by `step`.
    """
    my_list = []  # Initialize an empty list

    # Loop until start reaches stop
    while start < stop:
        my_list.append(start)  # Append current value to the list
        start += step  # Increment the current value by step

    return my_list

# Initialize lists to store x and y coordinates for two points
x_1_coords = [0]  # Starting x coordinate for the first point
y_1_coords = [0]  # Starting y coordinate for the first point

x_2_coords = [0]  # Starting x coordinate for the second point
y_2_coords = [0]  # Starting y coordinate for the second point

# Iterate over a range of steps from 1 to 200
for i in arange(1, 200, 1):

    # Generate random angles for both points, between 0 and 2π
    a_1 = random.uniform(0, 2 * math.pi)  # Random angle for the first point
    a_2 = random.uniform(0, 2 * math.pi)  # Random angle for the second point

    # Update x and y coordinates for the first point
    x_1 = x_1_coords[i - 1] + math.cos(a_1)
    y_1 = y_1_coords[i - 1] + math.sin(a_1)

    # Update x and y coordinates for the second point
    x_2 = x_2_coords[i - 1] + math.cos(a_2)
    y_2 = y_2_coords[i - 1] + math.sin(a_2)

    # Append the new coordinates to the respective lists
    x_1_coords.append(x_1)
    y_1_coords.append(y_1)

    x_2_coords.append(x_2)
    y_2_coords.append(y_2)

    # Plot the paths of the two points
    plt.plot(x_1_coords, y_1_coords, 'r-')  # Plot red line for point 1's path
    plt.plot(x_1, y_1, 'ro', markersize=10)  # Plot red dot for point 1

    plt.plot(x_2_coords, y_2_coords, 'b-')  # Plot blue line for point 2's path
    plt.plot(x_2, y_2, 'bo', markersize=10)  # Plot blue dot for point 2

    # Draw a green line between the two points
    plt.plot([x_1, x_2], [y_1, y_2], 'g-')

    # Set the x and y axis limits for the plot
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)

    # Display the current step out of 200 in the bottom-left corner
    plt.text(-18, -18, f"{i}/200 steps")

    # Update the graph with the new points and lines
    plt.draw()  # Draw the updated plot
    plt.pause(0.1)  # Pause for a short interval to create an animation effect

    # Clear the plot for the next frame
    plt.clf()  # Clears the current figure
