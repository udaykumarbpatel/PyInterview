# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.

# class Solution(object):

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        res = max(helper(s, i, i), helper(s, i, i + 1), res, key=len)
    return res


def helper(s, l, r):
    while 0 <= l and r < len(s) and s[l] == s[r]:
        l -= 1;
        r += 1
    return s[l + 1:r]

print longestPalindrome('babad')

