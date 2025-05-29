def fibonacci_iterative(n):
    """
    Generates Fibonacci numbers up to the n-th term using an iterative approach.

    Args:
        n (int): The number of Fibonacci terms to generate.
                 Must be a non-negative integer.

    Returns:
        list: A list containing the first n Fibonacci numbers.
              Returns an empty list if n is 0.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

# --- Examples ---
print("Iterative Fibonacci:")
print(f"Fibonacci(0): {fibonacci_iterative(0)}")   # Output: []
print(f"Fibonacci(1): {fibonacci_iterative(1)}")   # Output: [0]
print(f"Fibonacci(2): {fibonacci_iterative(2)}")   # Output: [0, 1]
print(f"Fibonacci(5): {fibonacci_iterative(5)}")   # Output: [0, 1, 1, 2, 3]
print(f"Fibonacci(10): {fibonacci_iterative(10)}") # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Example of generating a specific number without the full sequence
def get_nth_fibonacci_iterative(n):
    """
    Calculates the n-th Fibonacci number using an iterative approach.

    Args:
        n (int): The index of the Fibonacci number to find (0-indexed).
                 Must be a non-negative integer.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

print("\nN-th Fibonacci (Iterative):")
print(f"0th Fibonacci: {get_nth_fibonacci_iterative(0)}") # Output: 0
print(f"1st Fibonacci: {get_nth_fibonacci_iterative(1)}") # Output: 1
print(f"5th Fibonacci: {get_nth_fibonacci_iterative(5)}") # Output: 5
print(f"10th Fibonacci: {get_nth_fibonacci_iterative(10)}") # Output: 55 (Note: 0-indexed, so 10th term is 55)