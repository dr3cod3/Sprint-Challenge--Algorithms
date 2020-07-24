#!/usr/bin/env python3
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if "~" in word:
        inc = word.find("~")
    else:
        inc = 0
        word = "~" + word
    if inc < len(word):
        if inc + 2 >= len(word):
            return 0
        elif f"{word[inc + 1]}{word[inc + 2]}" == "th":
            return 1 + count_th(word[:inc] + word[inc + 1:inc + 3] + "~" + word[inc + 3:])
        else:
            return 0 + count_th(word[:inc] + word[inc + 1] + "~" + word[inc + 2:])
    else:
        return 0
