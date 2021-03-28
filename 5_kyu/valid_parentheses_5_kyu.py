"""Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the
input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. [], {}, <>)."""


def valid_parentheses(string):
    i = 0
    for c in string:
        if c == '(':
            i += 1
        elif c == ')':
            i -= 1
        if i < 0:
            return False
    if i != 0:
        return False
    else:
        return True
