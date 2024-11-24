import sys 

input = sys.stdin.readline

N = int(input())

L = list(map(int,input().split()))

L.sort()

ans = L[N-1] * (len(L) - 1)

for i in range(0,N-1) :
    ans += L[i]
print(ans)
