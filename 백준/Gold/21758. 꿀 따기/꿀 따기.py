import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
arrSum = [0] * N
arrSum[0] = arr[0]

for i in range(1,N) :
    arrSum[i] = arr[i] + arrSum[i-1]


##case 1
case1 = arrSum[N-1] - arr[0]
temp = 0
for bee2 in range(1,N-1):
    temp = max(temp , arrSum[N-1] - arrSum[bee2]-arr[bee2])
case1 += temp

##case 2

case2 = 0
for pot in range(1,N-1) :
    case2 = max(case2, arrSum[pot] - arr[0] + arrSum[N-1] - arrSum[pot-1] - arr[N-1])

##case 3
case3 = arrSum[N-1] - arr[N-1]
temp = 0
for bee1 in range(1,N-1) :
    temp = max(temp, arrSum[bee1] - arr[bee1] - arr[bee1])
case3 += temp

ans = 0
ans = max(case1,case2)
ans = max(ans,case3)
print(ans)