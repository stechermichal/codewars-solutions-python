"""Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as
shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity"""


def capitalize(s):
    s = [char for char in s]
    second_list = s[:]
    for i, value in enumerate(s):
        if i % 2 == 0:
            s[i] = value.lower()
        elif i % 2 == 1:
            s[i] = value.upper()
    for j, value_2 in enumerate(second_list):
        if j % 2 == 0:
            second_list[j] = value_2.upper()
        elif j % 2 == 1:
            second_list[j] = value_2.lower()
    s = ''.join(s)
    second_list = ''.join(second_list)
    return [second_list, s]
