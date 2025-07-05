import numpy as np
from sympy import symbols, expand
from z3 import Real, Solver, Abs, And

# Define symbolic function using SymPy
x_sym = symbols('x')
f_expr = expand(x_sym**3 - 2*x_sym + 1)

# Function to evaluate numerically
def check_precision(target_relative_error, precision_bits, samples=100):
    if precision_bits == 16:
        dtype = np.float16
    elif precision_bits == 32:
        dtype = np.float32
    else:
        dtype = np.float64

    x_values = np.linspace(-10, 10, samples)

    for x in x_values:
        real_val = x**3 - 2 * x + 1
        x_low = dtype(x)
        approx_val = x_low**3 - 2 * x_low + 1

        scale = abs(real_val) if abs(real_val) > 1e-8 else 1e-8
        relative_error = abs(approx_val - real_val) / scale

        if relative_error > target_relative_error:
            print(f"Precision {precision_bits}-bit is NOT sufficient for relative error {target_relative_error}. Failed at x = {x:.4f} with relative error {relative_error:.2e}")
            return False

    print(f"Precision {precision_bits}-bit is sufficient for relative error {target_relative_error}.")
    return True

#Example
if __name__ == "__main__":
  check_precision(target_relative_error=1e-2, precision_bits=16)
  check_precision(target_relative_error=1e-5, precision_bits=32)
  check_precision(target_relative_error=1e-10, precision_bits=64)

