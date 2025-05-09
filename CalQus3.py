import numpy as np
from scipy.integrate import quad

def integrand(x):
    return (1 + np.log(x)) * np.sqrt(1 + (x * np.log(x))**2)

result, error = quad(integrand, 0.2, 1)

print(f"Definite integral result: {result:.6f}")
print(f"Estimated error: {error:.6e}")