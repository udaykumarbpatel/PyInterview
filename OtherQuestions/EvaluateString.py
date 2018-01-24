# We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

# Sample input:
#     expression1 = "5+16-((9-6)-(4-2))"
#     expression2 = "22+(2-4)"

# Sample output:
#     evaluate(expression1) => 20
#     evaluate(expression2) => 20


def calculate(input_string):
    if input_string.find("+") == -1 and input_string.find("-") == -1:
        return input_string.replace('(', '').replace(')', '')

    result = None
    digit = None
    operator = None

    c = 0
    while c < len(input_string):
        if input_string[c] in ('+', '-'):
            if digit is None:
                digit = input_string[c]
            elif result is None:
                result = digit
                digit = None
                operator = input_string[c]
            else:
                result = cal(operator, result, digit)
                digit = None
                operator = input_string[c]
        elif input_string[c] is '(':
            i, paran_str = paren_string(input_string[c:])
            digit = calculate(paran_str[1:-1])
            result = cal(operator, result, digit)
            digit = None
            c = c + i
        else:
            if digit:
                digit += input_string[c]
            else:
                digit = input_string[c]
        c += 1

    return cal(operator, result, digit)


def paren_string(stripped_string):
    count = 0
    for c in range(len(stripped_string)):
        if stripped_string[c] is '(':
            count += 1
        elif stripped_string[c] is ')':
            count -= 1
            if count == 0:
                return c, stripped_string[:c + 1]


def cal(operator, f_num, s_num):
    if s_num is None:
        s_num = 0
    if f_num is None:
        return s_num

    if operator is '+':
        return int(f_num) + int(s_num)
    else:
        return int(f_num) - int(s_num)


print calculate("()")
print calculate("-9-5-4+25+5-8")
print calculate("(290)")
print calculate("20+16")
print calculate("5+16-((9-6)-(4-2))")
print calculate("22+(2-4)")
print calculate("+15-10-4+(1+(8+8-19)-18)-19+27")
