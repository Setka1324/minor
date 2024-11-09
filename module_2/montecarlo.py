import random
import math
import matplotlib.pyplot as plt

def montecarlo(func, x1, y1, x2, y2):
    """
    Performs Monte Carlo integration to estimate the area under a given curve in the specified
    rectangular region. It accounts for both positive and negative areas of the curve.

    Parameters:
    func (function): The function to integrate, representing the curve.
    x1 (float): The lower bound of the x-axis (start of the region).
    y1 (float): The lower bound of the y-axis (start of the region).
    x2 (float): The upper bound of the x-axis (end of the region).
    y2 (float): The upper bound of the y-axis (end of the region).

    Returns:
    float: The estimated area under the curve in the specified region.
    """

    points_above_curve = 0  # To track points above the x-axis and under the curve
    points_below_curve = 0  # To track points below the x-axis and under the curve
    total_points = 100000  # Set the number of random points generated

    # Generate random points and check if they fall under the curve
    for _ in range(total_points):
        x_rand = x1 + (x2 - x1) * random.random()
        y_rand = y1 + (y2 - y1) * random.random()

        func_value = func(x_rand)  # Get function value at the random x-coordinate

        # Count as part of positive area
        if func_value >= 0 and 0 <= y_rand <= func_value:
            points_above_curve += 1

        # Count as part of negative area
        elif func_value < 0 and func_value <= y_rand <= 0:
            points_below_curve += 1

    # Calculate the area of the rectangle surrounding the curve
    area_rectangle = (x2 - x1) * (y2 - y1)

    # Estimate the area under the curve
    positive_area = (points_above_curve / total_points) * area_rectangle
    negative_area = (points_below_curve / total_points) * area_rectangle
    area_under_curve = positive_area - negative_area

    return area_under_curve


def plot_montecarlo(func, x1, y1, x2, y2):

    # Generate x-values manually and corresponding function values
    x_vals = []
    y_vals = []
    num_curve_points = 500
    total_points = 100000

    for i in range(num_curve_points):
        x = x1 + (x2 - x1) * (i / num_curve_points)
        x_vals.append(x)
        y_vals.append(func(x))

    # Plot the function curve
    plt.plot(x_vals, y_vals, label='Function Curve')

    # Lists to hold the random points
    correct_points_x = []
    correct_points_y = []
    incorrect_points_x = []
    incorrect_points_y = []

    # Generate random points and classify them
    for _ in range(total_points):
        x_rand = x1 + (x2 - x1) * random.random()
        y_rand = y1 + (y2 - y1) * random.random()

        func_value = func(x_rand)  # Get function value at the random x-coordinate

        if func_value >= 0 and 0 <= y_rand <= func_value:
            correct_points_x.append(x_rand)
            correct_points_y.append(y_rand)
        elif func_value < 0 and func_value <= y_rand <= 0:
            correct_points_x.append(x_rand)
            correct_points_y.append(y_rand)
        else:
            incorrect_points_x.append(x_rand)
            incorrect_points_y.append(y_rand)

    # Plot the correct points in green and incorrect points in red
    plt.scatter(correct_points_x, correct_points_y, color='green', s=1, label='Correct Points')
    plt.scatter(incorrect_points_x, incorrect_points_y, color='red', s=1, label='Incorrect Points')

    # Set plot limits
    plt.xlim(x1, x2)
    plt.ylim(y1, y2)

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Monte Carlo Integration (Accounting for Negative Areas)')
    plt.legend()
    plt.show()

def func1(x):
    return math.sin(x ** 2)

def func2(x):
    return 2 * x

def func3(x):
    return x ** 2

def func4(x):
    return x / (x + 1)

def func5(x):
    return math.sin(x)

def func6(x):
    return math.tan(math.cos(math.sin(x)))

print(montecarlo(func4, 0, -1, math.pi, 1))
plot_montecarlo(func4, 0, -1, math.pi, 1)
