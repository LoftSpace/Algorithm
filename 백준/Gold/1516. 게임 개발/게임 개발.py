import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
cost = [0] * (N + 1)
inEdge = [0] * (N + 1)

for i in range(1,N + 1):
    arr = list(map(int,input().split()))
    cost[i] = arr[0]
    for j in arr[1:-1] : 
        graph[j].append(i)
        inEdge[i] += 1

queue = deque()

for i in range(1, N + 1):
    if inEdge[i] == 0 :
        queue.append(i)
topological = [0] * (N + 1)

while queue :
    node = queue.popleft()
    topological[node] += cost[node]
    for nextNode in graph[node] :
        
        inEdge[nextNode] -= 1
        topological[nextNode] = max(topological[nextNode],topological[node])
        if inEdge[nextNode] == 0 :
            queue.append(nextNode)

for i in range(1, N+1):
    print(topological[i])