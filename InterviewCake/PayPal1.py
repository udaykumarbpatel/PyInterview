from collections import defaultdict

def votes(votes):
    count_dic = defaultdict()
    for vote in votes:
        if count_dic.has_key(vote):
            count_dic[vote] = count_dic.get(vote) + 1
        else:
            count_dic[vote] = 1

    

