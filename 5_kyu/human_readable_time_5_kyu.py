"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""

from datetime import datetime


def make_readable(seconds):
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    return '{:02d}'.format(hours) + ':' + '{:02d}'.format(minutes) + ':' + '{:02d}'.format(seconds)