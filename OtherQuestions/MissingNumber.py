arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

def missingNumbers(arr, brr):
    # Complete this function
    m = max(arr + brr)
    table = [0 for _ in range(m + 1)]

    for a in arr:
        table[a] += 1

    for b in brr:
        table[b] -= 1

    values = [y for y in range(len(table)) if table[y] != 0]
    print values


missingNumbers(arr, brr)
