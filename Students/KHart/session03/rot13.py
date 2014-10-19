#!/usr/bin/python

# creating translation table
from string import maketrans
intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
outtab = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
trantab = maketrans(intab, outtab)

def rot13(string, p=True):
    '''converts each alpha charector to letter 13 away, p allows printing of before and after'''
    translated = string.translate(trantab)
    if p:
        print "Input:\t\t%s" % string
        print "Translated:\t%s" % translated
    return translated


to_translate = raw_input("Enter any string here: ")
rot13(to_translate)


if __name__ == "__main__":
    test_in = "Hello, there!"
    test_out = rot13(test_in, p=False)
    assert rot13(test_out, p=False) == test_in
    print "All tests passed"

