import sys
import heapq

input  = sys.stdin.readline

N , M = map(int,input().split())

next = [[] for _ in range(N + 1)]
inEdge = [0] * (N + 1)
queue = []
ans = []
for i in range(M) :
    u, v = map(int,input().split())
    next[u].append(v)
    inEdge[v] += 1

for i in range(1,N + 1):
    if inEdge[i] == 0 :
        heapq.heappush(queue,i)

while queue : 
    node = heapq.heappop(queue)
    ans.append(node)
    for nextNode in next[node] :
        inEdge[nextNode] -= 1
        if inEdge[nextNode] == 0 :
            heapq.heappush(queue,nextNode)
print(*ans)