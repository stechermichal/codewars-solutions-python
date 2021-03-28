"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"""""


def to_camel_case(text):
    if text:
        if text[0].istitle():
            text = text.title()
            return text.replace('-', '').replace('_', '')
        elif not text.istitle():
            text = text.title()
            text = text[0].lower() + text[1:]
            return text.replace('-', '').replace('_', '')
    else:
        return ''
