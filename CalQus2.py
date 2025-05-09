import numpy as np

def function_to_integrate(x):
    return np.sin(x) + (3 / (7 * np.pi)) * x

lower_limit = 0
upper_limit = 7 * np.pi / 6

n_intervals = 10000

x_values = np.linspace(lower_limit, upper_limit, n_intervals + 1)
y_values = function_to_integrate(x_values)

dx = (upper_limit - lower_limit) / n_intervals
integral_result = (dx / 2) * (y_values[0] + 2 * np.sum(y_values[1:-1]) + y_values[-1])

print("Area computed using numerical integration (trapezoidal rule):")
print(f"Area = {integral_result:.3f}")

np.random.seed(123)

x_lower = 0
x_upper = 7 * np.pi / 6
y_lower = -0.5
y_upper = 1

num_points = 1000000

x_points = np.random.uniform(x_lower, x_upper, num_points)
y_points = np.random.uniform(y_lower, y_upper, num_points)

sin_values = np.sin(x_points)
line_values = -(3 / (7 * np.pi)) * x_points

points_inside = np.sum((y_points <= sin_values) & (y_points >= line_values))

box_area = (x_upper - x_lower) * (y_upper - y_lower)

monte_carlo_area = (points_inside / num_points) * box_area

print("\nArea estimated using Monte Carlo simulation:")
print(f"Area = {monte_carlo_area:.3f}")