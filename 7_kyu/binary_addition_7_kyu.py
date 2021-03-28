""""Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done
before, or after the addition.

The binary number returned should be a string."""


def add_binary(a, b):
    c = a + b
    binary = []
    while c > 0:
        if c % 2 == 0:
            binary.append('0')
            c = c // 2
        elif c % 2 == 1:
            binary.append('1')
            c = c // 2
    binary.reverse()
    return "".join(binary)
