# Function to calculate ISBN-10 check digit
def calculate_check_digit_10(isbn):
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (i + 1)
    remainder = total % 11
    return 'X' if remainder == 10 else str(remainder)

# Function to calculate ISBN-13 check digit
def calculate_check_digit_13(isbn):
    total = 0
    for i in range(12):
        factor = 1 if i % 2 == 0 else 3
        total += int(isbn[i]) * factor
    remainder = total % 10
    check_digit = (10 - remainder) % 10
    return str(check_digit)

# Function to validate ISBN
def validate_isbn(isbn, length):
    isbn = isbn.strip()
    length = int(length)
    
    if length not in [10, 13]:
        return "Length should be 10 or 13."
    
    if len(isbn) != length:
        return f"ISBN-{length} code should be {length} digits long."
    
    try:
        if length == 10:
            check_digit = calculate_check_digit_10(isbn)
        else:
            check_digit = calculate_check_digit_13(isbn)
    except ValueError:
        return "Invalid character was found."
    
    if isbn[-1].upper() == check_digit:
        return "Valid ISBN Code."
    else:
        return "Invalid ISBN Code."

# Main function to take user input
def main():
    user_input = input("Enter ISBN and length: ")
    try:
        isbn, length = user_input.split(',')
    except ValueError:
        print("Enter comma-separated values.")
        return

    try:
        length = int(length)
    except ValueError:
        print("Length must be a number.")
        return
    
    try:
        result = validate_isbn(isbn, length)
    except ValueError:
        print("Invalid character was found.")
        return

    print(result)

# Commented out for testing purposes
# main()
