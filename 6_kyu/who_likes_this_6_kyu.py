"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function names :: [String] -> String, which must take in input array,
containing the names of people who like an item. It must return the display text as shown in the examples:

names([]) # must be "no one names this"
names(["Peter"]) # must be "Peter names this"
names(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
names(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
names(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases."""


def likes(names):
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    else:
        return "no one likes this"
