import time


def fibonacci():
    if x in [0, 1]:
        return x
    prev_prev = 0
    prev = 1

    for _ in range(x - 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current


def fibonacci_recursive(x):
    if x in [0, 1]:
        return x
    else:
        return fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2)


if __name__ == "__main__":
    x = int(raw_input())
    print fibonacci()
    print fibonacci_recursive(x)
