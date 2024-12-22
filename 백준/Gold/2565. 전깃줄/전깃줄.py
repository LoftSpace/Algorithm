import sys

input = sys.stdin.readline


dp = []

N = int(input())

wires=[]
for i in range(N):
    wires.append(list(map(int,input().split())))

wires.sort()
    
dp.append(wires[0][1])
check = 0

for i in range(1,N) :
    if wires[i][1] != 0 :
        if dp[check] < wires[i][1] :
            dp.append(wires[i][1])
            check += 1
        else :
            left = 0
            right =  check
            while left <= right :
                mid = (left + right) // 2
                if dp[mid] == wires[i][1] :
                    left = mid
                    break
                elif dp[mid] < wires[i][1] :
                    left = mid + 1
                else :
                    right = mid - 1
            dp[left] = wires[i][1]


print(N - len(dp))