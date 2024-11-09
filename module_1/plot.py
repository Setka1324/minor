import math
import matplotlib.pyplot as plt

x_values = []
y_values = []

x = 0
while x <= 4:
    x_values.append(x)
    x += 0.01

for x in x_values:
    y = 12.38 * x**4 - 84.38 * x**3 + 165.19 * x**2 - 103.05 * x
    y_values.append(y)

index = 0
min = float("inf")
for i in range(len(x_values)):
    if y_values[i] < min:
        min = y_values[i]
        index = i

x_min = round(x_values[index], 2)
y_min = round(y_values[index], 2)

plt.plot(x_values, y_values, 'b-', x_min, y_min, 'ro')
plt.xlabel('x', fontsize = 15)
plt.ylabel('f(x)', fontsize = 15)
plt.text(x_min, y_min, f"(xmin, ymin) = ({x_min}, {y_min})", color = 'black', fontsize = 10)
plt.show()

print(f"(xmin, ymin) = ({x_min}, {y_min})")
