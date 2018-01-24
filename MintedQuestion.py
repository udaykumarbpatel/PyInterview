# We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

# Sample input:
#     expression1 = "5+16-((9-6)-(4-2))"
#     expression2 = "22+(2-4)"

# Sample output:
#     evaluate(expression1) => 20
#     evaluate(expression2) => 20


def calculate(input_string):
    result = ''
    digit = ''
    operator = ''

    #     for c in input_string:
    #         if c in ('+','-'):
    #             if result is '':
    #                 result = digit
    #             else:
    #                 result = cal(operator, result, digit)
    #             digit = ''
    #             operator = c
    #         elif c is '(':

    #         else:
    #             digit += c

    for c in range(len(input_string)):
        if input_string[c] in ('+', '-'):
            if result is '':
                result = digit
            else:
                result = cal(operator, result, digit)
            digit = ''
            operator = input_string[c]
        elif input_string[c] is '(':
            i, pran_str = paren_string(input_string[c:])
            print "String to function : ", pran_str[1:-1]
            digit = calculate(pran_str[1:-1])
            result = cal(operator, result, digit)
            c = i
        else:
            digit += input_string[c]

    if operator is '':
        return input_string
    else:
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

    return len(stripped_string), stripped_string


def cal(operator, f_num, s_num):
    print "In function"
    print f_num, s_num
    if operator is '+':
        return int(f_num) + int(s_num)
    else:
        return int(f_num) - int(s_num)


print calculate("((9-6)-(4-2))")
