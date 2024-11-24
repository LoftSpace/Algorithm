import sys

input = sys.stdin.readline

N = int(input())

p = list(map(int,input().split()))

p.sort()

Sum = 0

for i in range(N) :
    Sum += (N-i) * p[i]

print(Sum)