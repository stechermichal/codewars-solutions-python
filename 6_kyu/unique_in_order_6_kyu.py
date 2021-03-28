"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]"""


def unique_in_order(iterable):
    final_list = []
    for i in iterable:
        # If the list is empty, then always throw the character in.
        if not final_list:
            final_list.append(i)
        # If the previously appended character isn't the same, throw it in.
        elif final_list[-1] != i:
            final_list.append(i)
    return final_list
