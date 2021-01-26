def check_integer(num):
    if not 45 <= num <= 67:
        raise NotInBoundsError
    else:
        return num


def error_handling(num):
    try:
        print(check_integer(num))
    except NotInBoundsError as e:
        print(e)
