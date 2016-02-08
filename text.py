__author__ = 'spotapov'
import string
import random

#makes random string of 129 characters
def big_text():
    text = ''
    l = 0
    for i in range(0,129):
        text += random.choice(string.ascii_letters)
    print(text)

    for k in text:
        l = l + 1
    print(l)


big_text()

