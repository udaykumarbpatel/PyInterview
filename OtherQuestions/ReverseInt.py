# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: -123
# Output:  -321

import sys


class Solution(object):
    @staticmethod
    def reverseInt(x):
        sign = cmp(x, 0)

        x = sign * x
        result = '0'
        while x > 0:
            result = result + `(x % 10)`
            x = x / 10

        return int(result) * sign * (int(result) < 2 ** 31)


print Solution.reverseInt(123)
