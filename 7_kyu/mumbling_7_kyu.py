"""This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""


def accum(word):
    word = [char for char in word]
    for i, ch in enumerate(word):
        word[i] = ch * (i+1)
    word = [char.title() for char in word]
    return '-'.join(word)
