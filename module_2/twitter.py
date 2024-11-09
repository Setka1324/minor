import random
import math
import matplotlib.pyplot as plt

# I was quite confused with the task, I guess thats te right approach. I guessed the limits for box a couple of times

# Function to check if a point is inside the Twitter egg based on the new formula
def is_inside_egg(x, y):
    term1 = math.sqrt(x**2 + y**2)
    term2 = (2/3) * math.sqrt(x**2 + ((5/6) - y)**2)
    return term1 + term2 <= 1

# Function to estimate the area using Monte Carlo method
def estimate_twitter_egg_area(total_points):
    points_inside = 0
    x_vals_inside = []
    y_vals_inside = []
    x_vals_outside = []
    y_vals_outside = []

    area_estimations = []
    x_min, x_max = -0.75, 0.75  # Adjusted x bounds
    y_min, y_max = -0.3, 1      # Adjusted y bounds
    bounding_box_area = (x_max - x_min) * (y_max - y_min)

    for i in range(total_points):
        # Generate random points within the adjusted bounds
        x_rand = x_min + (x_max - x_min) * random.random()
        y_rand = y_min + (y_max - y_min) * random.random()

        if is_inside_egg(x_rand, y_rand):
            points_inside += 1
            x_vals_inside.append(x_rand)
            y_vals_inside.append(y_rand)
        else:
            x_vals_outside.append(x_rand)
            y_vals_outside.append(y_rand)

        # Every 1000 points, store the current estimation of the area
        if (i + 1) % 1000 == 0:
            estimated_area = (points_inside / (i + 1)) * bounding_box_area
            area_estimations.append(estimated_area)

    final_area = (points_inside / total_points) * bounding_box_area
    return final_area, x_vals_inside, y_vals_inside, x_vals_outside, y_vals_outside, area_estimations

# Function to plot the results and display the final area
def plot_egg():
    total_points = 1000000  # Generate 1 million points
    final_area, x_in, y_in, x_out, y_out, area_estimations = estimate_twitter_egg_area(total_points)

    # Print the final area estimate
    print(f"The area of the Twitter egg is {final_area:.2f}")

    # Plot the points outside the egg in blue
    plt.figure(figsize=(8, 8))
    plt.scatter(x_out, y_out, color='blue', s=1)  # Removed label from here

    # Add text inside the egg for total points (placed inside the egg area)
    plt.text(0, 0.5, f'Total Points: {total_points}', fontsize=12, color='black', ha='center')

    # Add labels and title
    plt.title(f"Monte Carlo Estimate of the Twitter Egg Area: {final_area:.2f}")
    plt.xlabel("x")
    plt.ylabel("y")

    # Display the plot
    plt.show()

    # Plot the area estimation over time
    plt.figure(figsize=(8, 6))
    plt.plot(range(1000, total_points + 1, 1000), area_estimations, label='Estimated Area', color='blue')
    plt.axhline(final_area, color='red', linestyle='--', label=f'Final Area: {final_area:.2f}')
    plt.xlabel('Number of Points')
    plt.ylabel('Estimated Area')
    plt.title('Convergence of Area Estimation')
    plt.legend()
    plt.show()

# Call the plot_egg function to run the program
plot_egg()
