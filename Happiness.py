# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = raw_input().split()
N = raw_input().split()
A = set(raw_input().split())
B = set(raw_input().split())


print sum([(i in A) - (i in B) for i in N])

