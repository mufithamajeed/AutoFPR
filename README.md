# AutoFPR: Floating-Point Precision Reasoning Tool

## Overview
AutoFPR is a lightweight numerical reasoning tool designed to assess whether different floating-point precision levels (16-bit, 32-bit, 64-bit) are sufficient to meet specific numerical accuracy requirements. The goal is to provide a simple, testable framework for understanding how computational errors vary with floating-point representation.

The current demonstration focuses on the polynomial function:
$$
f(x) = x^3 - 2x + 1
$$
but the approach is generalizable to other numerical computations.

## Why Precision Matters
In scientific computing, finance, and embedded systems, floating-point computations can accumulate rounding errors that silently lead to incorrect results, wasted computational resources, or even system failures.

Choosing the correct precision:
- **Avoids unnecessary computation** (lower precision where possible)
- **Maintains numerical accuracy** (higher precision where necessary)
- Balances **performance, energy efficiency, and numerical correctness**

Manual precision selection is often arbitrary or based on trial-and-error. AutoFPR offers an **automated, quantitative approach** to support these decisions.

## How AutoFPR Works
1. The target function is computed using high precision (`float64`) as the reference.
2. The same function is evaluated at lower precisions (`float16`, `float32`).
3. The tool measures the **relative error** between the low-precision result and the reference:
\[
\text{Relative Error} = \frac{|f_{\text{low}} - f_{\text{ref}}|}{|f_{\text{ref}}| + \epsilon}
\]
4. If the maximum observed relative error exceeds a user-defined threshold, the precision is reported as **not sufficient**; otherwise, it is **sufficient**.

### Why Relative Error?
Relative error is used because:
- It scales naturally with the size of the function’s output.
- It reflects the practical significance of numerical differences across varying magnitudes.

## How to Run AutoFPR

1. Install the required packages:
```bash
pip install -r requirements.txt
````

2. Run the main script:

```bash
python auto_fpr.py
```

3. (Optional) Run additional test cases:

```bash
python test_cases.py
```

## Example Results

```
Precision 16-bit is sufficient for relative error 0.01.
Precision 32-bit is sufficient for relative error 1e-05.
Precision 64-bit is sufficient for relative error 1e-10.
```

If a stricter tolerance is specified (e.g., `1e-4` for float16), the tool correctly reports:

```
Precision 16-bit is NOT sufficient for relative error 0.0001.
```

## Key Takeaways

* AutoFPR identifies both cases where low precision is **acceptable** and cases where higher precision is **required**.
* The framework is simple, interpretable, and adaptable to other numerical functions.

## Limitations and Future Directions

* This prototype uses **sampling-based numerical checks** rather than exhaustive formal verification.
* It does not currently model **ULP-level (Unit in the Last Place) errors**, denormalized numbers, or hardware-specific behaviors.
* Future extensions could:

  * Integrate with SMT solvers or theorem provers for **formal verification of numerical guarantees**.
  * Apply this framework to real-world algorithms in fields such as finance, physics, or machine learning.

## Conclusion

AutoFPR is a practical first step toward **precision-aware computing**, providing a simple tool to identify the minimum floating-point precision required to meet numerical accuracy goals. It highlights the importance of balancing computational efficiency and numerical reliability, especially in safety-critical or resource-constrained environments.

## License

For academic and educational use only.
