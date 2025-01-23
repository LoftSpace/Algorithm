import sys

input = sys.stdin.readline

N = int(input())

targets = [[0,0]]
for i in range(N):
    targets.append(list(map(int,input().split())))

targets.sort(key = lambda x: [x[1] , x[0]])

e = 0
count = 0

for target in targets :
    if target[0] >= e :
        e = target[1]
        count +=1

print(count-1)