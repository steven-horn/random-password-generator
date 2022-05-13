import random
import string

def length(input):
    """Function to determine whether the length is a valid input"""
    try:
        length = int(input)
        if length >= 8 and length <= 32:
            return length
        else:
            return False
    except ValueError:
        return False

def password_generator(length, omit):
    """Function to generate the password using the length and the omitted characters provided."""
    i = 0
    temp = []
    while i < length:
        symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        for x in omit:
            symbols = symbols.replace(x, "")
        temp.append(''.join(random.sample(symbols, 1)))
        i += 1
    password = ''.join(temp)
    return password

