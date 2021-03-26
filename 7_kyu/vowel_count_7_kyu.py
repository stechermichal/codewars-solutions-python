"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""


def get_count(input_str):
    vowels = set("aeiou")
    return len([x for x in input_str if x in vowels])
