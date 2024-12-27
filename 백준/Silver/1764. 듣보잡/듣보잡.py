import sys

input = sys.stdin.readline

N, M = map(int,input().split())
hash = dict()
ans = []
for i in range(N):
    name = input().split()[0]
    hash[name] = 0

for j in range(M):
    name = input().split()[0]
    if name in hash :
        ans.append(name)
print(len(ans))
ans.sort()
for i in ans :
    print(i)