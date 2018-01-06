def capitalize(string):
    print string
    first = True
    result = ""
    for c in string:
        if first and not c.isspace():
            result = result + c.upper()
            first = False
        elif c.isspace():
            result = result + c
            first = True
        else:
            result = result + c
    return result



print capitalize("uday patel    lives in california")