def verify_card_number(card_number):
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Convert each character to an integer
    digits = [int(d) for d in card_number]
    
    # Starting from the right, double every second digit (excluding the check digit)
    # We can iterate in reverse
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        # If doubling gives a number > 9, subtract 9
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    
    # Calculate total sum
    total = sum(digits)
    
    # If the total modulo 10 is 0, the card is valid
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
