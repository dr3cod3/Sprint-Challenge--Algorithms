#!/usr/bin/env python3
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# def count_th(word):
#     # What is the base case to stop or not to recurse
#     wlen = len(word)
#     count = 0
#     if wlen == 0:
#         return
#     # what is the recursive case
#     # Have to go through the input "word" compare the
#     # strings and update the variable tracking the count

#     else:
#         if "th" in count_th(word):
#             count += 1
#         wlen - 1

#     return count

#     # TBC


def count_th(word):
    if "~" in word:
        inc = word.find("~")
    else:
        inc = 0
        word = "~" + word
    # print(word)
    if inc < len(word):
        if inc + 2 >= len(word):
            return 0
        elif f"{word[inc + 1]}{word[inc + 2]}" == "th":
            return 1 + count_th(word[:inc] + word[inc + 1:inc + 3] + "~" + word[inc + 3:])
        else:
            return 0 + count_th(word[:inc] + word[inc + 1] + "~" + word[inc + 2:])
    else:
        return 0
