def apply_discount(price, discount):
    if type(price) is not int and type(price) is not float:
        return "The price should be a number"

    if type(discount) is not int and type(discount) is not float:
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    return price - (price * discount / 100)
