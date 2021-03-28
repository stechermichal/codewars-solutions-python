"""Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""


def pig_it(text):
    text_list = text.split()
    for i, value in enumerate(text_list):
        if value.isalpha():
            text_list[i] = value[1:] + value[0:1] + 'ay'
    return ' '.join(text_list)
