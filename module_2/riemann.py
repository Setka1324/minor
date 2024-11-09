import numpy as np
import matplotlib.pyplot as plt

# Quadratic func
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Riemann midpoint calculation
def riemann(a, b, c, begin_x, end_x, n):
    # Rectangle Width
    delta_x = (end_x - begin_x) / n

    total_sum = 0

    # Riemann sum midpoint method
    for i in range(n):
        midpoint_x = begin_x + delta_x * (i + 0.5)
        total_sum += quadratic_function(midpoint_x, a, b, c) * delta_x

    return total_sum


def plot_riemann(a, b, c, begin_x, end_x, n):
    # Generate points for graph
    x_values = []
    y_values = []

    x_1 = begin_x
    while x_1 <= end_x:
        x_values.append(x_1)
        x_1 += 0.01

    for y in x_values:
        y_values.append(quadratic_function(y, a, b, c))

    # Plot the graph
    plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')

    # Plot rectangles
    width = (end_x - begin_x) / n
    for i in range(n):
        x = begin_x + i * width
        plt.bar(x, quadratic_function(x, a, b, c), width=width, align='edge', color='gray', alpha=0.5, edgecolor='black')

    plt.title(f'Riemann Sum for ({a}x^2) + ({b}x) + ({c}) from {begin_x} to {end_x}')
    plt.show()

riemann_value = riemann(1, -2, 1, 0, 5, 100)
plot_riemann(1, -2, 1, 0, 5, 10)

riemann_value
