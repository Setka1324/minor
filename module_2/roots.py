import math
import matplotlib.pyplot as plt

def roots(a, b, c):
    """
    Calculates the real roots (if any) of a quadratic equation of the form ax^2 + bx + c = 0
    using the quadratic formula. Returns the roots in ascending order if they exist.

    Parameters:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.

    Returns:
    list: A list of the real roots (can be one or two roots) or an empty list if no real roots exist.
    """
    roots = []  # List to store the roots if found

    part_one = b / (2 * a)  # Calculate the b / (2a) part of the quadratic formula
    d = part_one**2 - (c / a)  # Calculate the discriminant (d)

    # Check if the discriminant is non-negative (which would mean real roots exist)
    if d >= 0:
        d_root = math.sqrt(d)  # Calculate the square root of the discriminant
        root_1 = round(-part_one - d_root, 2)  # First root of the quadratic equation
        root_2 = round(-part_one + d_root, 2)  # Second root of the quadratic equation

        roots.extend([root_1, root_2])  # Add both roots to the list

    roots.sort()  # Sort the roots in ascending order

    # Print each root
    for root in roots:
        print(root)

    return roots  # Return the list of roots (empty if no real roots)


def plot_roots(a, b, c):
    """
    Plots the quadratic function f(x) = ax^2 + bx + c and marks the roots on the graph.
    The roots are calculated using the roots() function.

    Parameters:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.

    Returns:
    None: This function generates a plot.
    """
    answer = roots(a, b, c)  # Get the roots of the quadratic equation

    x_values = []  # List to store x values for plotting
    y_values = []  # List to store corresponding y values

    x_max = 5  # Default x-axis range

    # Set the range for x-axis based on the roots, if they exist
    if answer:
        x = answer[0] - abs(answer[0] * 0.2)  # Start a little before the first root
        x_max = answer[1] + abs(answer[1] * 0.2)  # End a little after the second root
    else:
        x = -5  # Default x-axis start if no roots

    # Generate x values from the starting point to x_max
    while x <= x_max:
        x_values.append(x)
        x += 0.01  # Increment x in small steps for a smooth curve

    # Calculate corresponding y values for the quadratic function
    for x in x_values:
        y = a * x**2 + b * x + c  # Calculate f(x) = ax^2 + bx + c
        y_values.append(y)

    # Plot the quadratic curve
    plt.plot(x_values, y_values, 'b-')

    # Plot the roots as red dots, if they exist
    if answer:
        plt.plot(answer, [0, 0], 'ro')

    plt.show()  # Display the plot
    
plot_roots(3, 6, 9)
