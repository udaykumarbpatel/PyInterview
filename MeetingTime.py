meets = [(10,12),(11,12), (2,3), (5,7), (1,3)]
#meets =[(1, 3), (2, 3), (5, 7), (9, 11), (10, 12)]
# result = [(1,3) , (5,7], (9,11)

#meets = [(7, 8), (9, 11), (10, 12), (1, 3), (2, 4), (1, 5)]
#result= [(1, 3), (1, 5), (2, 4), (7, 8), (9, 11), (10, 12)]
#answe = [(1,3),(7,8), (9,12)]

def meeting_schedule(meets):
    meets.sort()
    print meets

    old_tup = [meets[0][0],meets[0][1]]
    result = []
    for tup in meets:
        if tup[0] < old_tup[1]:
            if tup[1] >= old_tup[1]:
                old_tup[1] = tup[1]
        else:
            result.append((old_tup[0], old_tup[1]))
            old_tup = [tup[0],tup[1]]

    result.append((old_tup[0], old_tup[1]))
    print result


meeting_schedule(meets)