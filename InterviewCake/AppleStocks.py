import sys

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# returns 6 (buying for $5 and selling for $11)

def get_max_profit(s):
    maxv = -sys.maxint
    for i in s.count():
        if maxv > s[i]:
            maxv = s[i]

    return maxv


print get_max_profit(stock_prices_yesterday)
