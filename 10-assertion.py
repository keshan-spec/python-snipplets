#  assert if the data is not correct


def assertion(x, y):
    # raise and assertion if the data is in the wrong format
    assert y != 0
    return x/y


print(assertion(100, 10)) # Correct
print(assertion(100, 0)) # Wrong
