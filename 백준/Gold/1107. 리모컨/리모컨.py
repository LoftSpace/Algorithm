import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
M = int(input())
broken = []
if M != 0 :
    broken = list(map(str,input().split()))

Min = abs(100 - N)

for nums in range(999999):
    count = 0
    numStr = str(nums)
    for num in range(len(numStr)):
        if numStr[num] in broken :
            break
        count += 1
   
    if count == len(numStr) :
        Min = min(Min, count + abs(N - nums))
  
print(Min)