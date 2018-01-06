def find_num_appear_twice(nums):
    n = len(nums) - 1
    print abs(sum(nums) - ((n* (n+1))/2))

find_num_appear_twice([1,2,3,4,5,6,7,8,2])



