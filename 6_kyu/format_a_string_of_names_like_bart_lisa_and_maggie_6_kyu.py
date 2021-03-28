"""Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be
separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'."""


def namelist(names):
    sentence = []
    for i, name in enumerate(names):
        sentence.append(names[i]['name'])
    if len(sentence) == 2:
        sentence_3 = " & ".join(sentence[-2:])
        return sentence_3
    elif len(sentence) == 1:
        return sentence[0]
    elif len(sentence) > 0:
        sentence_2 = ", ".join(sentence[0:-2])
        sentence_2 = sentence_2 + ", "
        sentence_3 = " & ".join(sentence[-2:])
        return sentence_2+sentence_3
    else:
        return ''
