import sys

input = sys.stdin.readline
N = int(input())
hash = dict()

for _ in range(N) :
    i = int(input())
    if i in hash :
        hash[i] += 1
    else :
        hash[i] = 1
Max = 0
num = 0

for i in hash :
    if Max < hash[i] :
        Max = hash[i]
        num = i
    elif Max == hash[i] :
        if i < num :
            Max = hash[i]
            num = i
   
print(num)