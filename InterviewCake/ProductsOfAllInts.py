def product_of_all_ints(x):
    result = [None] * len(x)

    product = 1
    i = 0
    while i < len(x):
        result[i] = product
        product *= x[i]
        i += 1

    product = 1
    i = len(x) - 1
    while i >= 0:
        result[i] *= product
        product *= x[i]
        i -= 1

    return result


if __name__ == "__main__":
    x = map(int, raw_input().strip().split(' '))
    result = product_of_all_ints(x)
    print result
