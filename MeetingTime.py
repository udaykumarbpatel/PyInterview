meets = [(1, 10), (2, 6), (3, 5), (7, 9)]


def meeting_schedule(meets):
    meets.sort()
    print meets

    old_tup = [meets[0][0], meets[0][1]]
    result = []
    for tup in meets:
        if tup[0] <= old_tup[1]:
            if tup[1] >= old_tup[1]:
                old_tup[1] = tup[1]
        else:
            result.append((old_tup[0], old_tup[1]))
            old_tup = [tup[0], tup[1]]

    result.append((old_tup[0], old_tup[1]))
    print result


meeting_schedule(meets)
