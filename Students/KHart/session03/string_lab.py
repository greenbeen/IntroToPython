def first_last(string):
    return string[-1] + string[1:-1] + string[0]

def every_other(string):
    return string[::2]

def four_every_other(string):
    return string[4:-4:2]

def reversed(string):
    return string[::-1]

def third(string):
    return string[len(string)/3:] + string[:len(string)/3]

def third2(string):
    third = len(string)/3
    return string[third:] + string[:third]








#print first_last("abcdef")
#print every_other("1234567890")
#print four_every_other("111123456789999")
#print reversed("1234567")
#print third("123456789")
print third2("123456789")
