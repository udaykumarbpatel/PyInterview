def merge_the_tools(string, k):
    # your code goes here
    for i in list(string[0 + i:k + i] for i in range(0, len(string), k)):
        res = ""
        for c in i:
            if c not in res:
                res = res + c
        print res


merge_the_tools('AABCAAADA', 3)