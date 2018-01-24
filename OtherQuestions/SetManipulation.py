n = input()
s = set(map(int, raw_input().split()))
commands = int(raw_input())

for i in xrange(commands):
    comm = raw_input().split()
    if comm[0] == 'pop':
        s.pop()
    elif comm[0] == 'remove':
        s.remove(int(comm[1]))
    elif comm[0] == 'discard':
        s.discard(int(comm[1]))

print sum(s)
