
def swapcase(s):
    result = ""
    for c in s:
        if ord(c) > 64 and ord(c) < 91:
            result = result +  chr(ord(c) + 32)
        if ord(c) > 96 and ord(c) < 123:
            result = result + chr(ord(c) - 32)

    print result


def print_full_name(a, b):
    print "Hello %s %s! You just delved into python." % (a , b)

swapcase("uday patel")
print_full_name(None, None)