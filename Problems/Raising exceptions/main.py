def sum_with_exceptions(a, b):
    sum = a + b
    if sum < 0:
        raise NegativeSumError
    else:
        return sum


class NegativeSumError(Exception):
    pass
