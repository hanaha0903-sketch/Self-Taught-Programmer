def cubed(i):
    try:
        i = int(i)
        return i ** 3
    except (ValueError, TypeError):
        return "Error: Input must be a number"
