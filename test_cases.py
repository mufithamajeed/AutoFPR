from auto_fpr import check_precision

# Test case 1: Loose tolerance
check_precision(target_relative_error=1e-2, precision_bits=16)

# Test case 2: Medium tolerance
check_precision(target_relative_error=1e-5, precision_bits=32)

# Test case 3: Tight tolerance
check_precision(target_relative_error=1e-12, precision_bits=64)