def fibonacci(n):
    sequence = [0, 1]

    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Build sequence up to n using dynamic programming
    for i in range(2, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)

    # The nth Fibonacci number is stored at index n
    return sequence[n]
