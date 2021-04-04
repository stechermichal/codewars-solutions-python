"""Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string."""


def fake_bin(x):
    x = [int(i) for i in x]
    for i, value in enumerate(x):
        if value < 5:
            x[i] = 0
        else:
            x[i] = 1
    return ''.join(str(i) for i in x)

