def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper


@price_string
def new_price(old_value):
    return 0.9 * old_value
