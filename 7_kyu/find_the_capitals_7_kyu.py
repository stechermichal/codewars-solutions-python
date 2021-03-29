"""Instructions
Write a function that takes a single string (word) as argument. The function must return an ordered list containing
the indexes of all capital letters in the string.

Example
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );"""


def capitals(word):
    position_list = []
    for i in range(0, len(word)):
        if word[i].isupper():
            position_list.append(i)
        else:
            pass
    return position_list
