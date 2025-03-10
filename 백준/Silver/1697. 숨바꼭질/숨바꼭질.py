import sys
from collections import deque

input = sys.stdin.readline

N , K = map(int,input().split())
MAX = max(N,K)
dp = [False] * (MAX * 2 + 1)
queue = deque([])

queue.append([N,0])
dp[N] = True

while queue :
    num,count = queue.popleft()
    if num == K :
        print(count)
        break
    if 0 <= num + 1 < MAX * 2 + 1 and not dp[num + 1]:
        dp[num + 1] = True
        queue.append([num + 1,count + 1])
    
    if 0 <= num - 1 < MAX * 2 + 1 and not dp[num - 1]:
        dp[num - 1] = True
        queue.append([num - 1,count + 1])

    if 0 <= num *2  < MAX * 2 + 1 and not dp[num * 2]:
        dp[num * 2] = True
        queue.append([num * 2,count + 1])

