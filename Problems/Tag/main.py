def tagged(func):
    def wrapper(arg):
        return f"<title>{func(arg)}</title>"

    return wrapper


@tagged
def from_input(inp):
    string = inp.strip()
    return string
