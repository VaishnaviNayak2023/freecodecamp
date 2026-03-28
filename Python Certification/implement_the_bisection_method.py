def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    # Handle negative numbers
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # Handle 0 and 1
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    # Set initial bounds
    low = 0
    high = max(1, number)
    
    iterations = 0
    
    while (high - low) > tolerance and iterations < max_iterations:
        mid = (low + high) / 2
        square = mid * mid
        
        if square == number:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        elif square < number:
            low = mid
        else:
            high = mid
        
        iterations += 1
    
    # Check if we converged
    if (high - low) <= tolerance:
        root = (low + high) / 2
        print(f"The square root of {number} is approximately {root}")
        return root
    else:
        print(f"Failed to converge within {max_iterations} iterations")
        return None
