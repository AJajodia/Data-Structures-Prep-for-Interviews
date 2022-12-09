# PROBLEM STATEMENT

# Here is a self check that really covers everything so far. You may have heard of the infinite monkey theorem?
# The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will
# almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a
# monkey with a Python function. How long do you think it would take for a Python function to generate just one
# sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel” You are not going to want to
# run this one in the browser, so fire up your favorite Python IDE. The way we will simulate this is to write a function
# that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus
# the space. We will write another function that will score each generated string by comparing the randomly generated
# string to the goal. A third function will repeatedly call generate and score, then if 100% of the letters are correct
# we are done. If the letters are not correct then we will generate a whole new string. To make it easier to follow your
# program’s progress this third function should print out the best string generated so far and its score every 1000
# tries.

# EXTENSION

# See if you can improve upon the program in the self check by keeping letters that are correct
# and only modifying one character in the best string so far.

import random


usable = "abcdefghijklmnopqrstuvwxyz "


string = "methinks it is like a weasel"


def generator(letters):
    result = ""
    for i in range(28):
        result += letters[random.randint(0, 26)]
    return result


def score(target, actual):
    points = 0
    for i in range(len(target)):
        if target[i] == actual[i]:
            points += 1
    return points/len(target)*100


def swapper(target, current, letters):
    for i in range(len(target)):
        if target[i] != current[i]:
            badindex = i
    currlist = [i for i in current]
    currlist[badindex] = letters[random.randint(0, 26)]
    return "".join(currlist)


def monkeytype(letters, target):
    tries = 0
    nope = True
    beststring = ""
    while nope:
        if beststring == "":
            beststring = currstring = generator(letters)
        currstring = swapper(target, currstring, letters)
        if score(target, currstring) == 100.0:
            beststring = currstring
            nope = False
        if score(target, currstring) > score(target, beststring):
            beststring = currstring
        print(currstring + " " + str(score(target, currstring)))
    return beststring


print(monkeytype(usable, string) + " is correct")
