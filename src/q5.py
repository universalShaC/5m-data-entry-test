def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # Check that both values are numeric (int or float)
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        print("Both num and divisor must be numeric.")
        return False

    # Avoid division by zero
    if divisor == 0:
        print("Divisor cannot be zero.")
        return False

    # Return True if num is divisible by divisor, otherwise False
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

# Calling the function with 10 and 2
result1 = check_divisibility(10, 2)
print("Is 10 divisible by 2?", result1)

# Calling the function with 7 and 3
result2 = check_divisibility(7, 3)
print("Is 7 divisible by 3?", result2)
