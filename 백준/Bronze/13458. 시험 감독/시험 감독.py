import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())
Sum = 0


for i in range(N) :
    if A[i] - B > 0 :
        if (A[i] - B) % C == 0:
            Sum += (A[i] - B) // C
        else :
            Sum += (A[i] - B) // C + 1
Sum += N


print(Sum)
