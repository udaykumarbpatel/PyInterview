def hackerlandRadioTransmitters(x, k):
    x.sort()
    num_of_transmitter = 0
    i = 0

    while i < n:
        num_of_transmitter = num_of_transmitter + 1
        next_point = x[i] + k
        while i < n and x[i] <= next_point:
            i = i + 1
        next_point = x[i - 1] + k
        while i < n and x[i] <= next_point:
            i = i + 1

    return num_of_transmitter


if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = map(int, raw_input().strip().split(' '))
    result = hackerlandRadioTransmitters(x, k)
    print result
