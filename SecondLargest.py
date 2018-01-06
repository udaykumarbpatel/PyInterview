import sys

n = int(raw_input())
arr = map(int, raw_input().split())

maximum = max(arr)
sec_max = -sys.maxint

for i in arr:
    if i < maximum and i > sec_max:
        sec_max = i

print sec_max