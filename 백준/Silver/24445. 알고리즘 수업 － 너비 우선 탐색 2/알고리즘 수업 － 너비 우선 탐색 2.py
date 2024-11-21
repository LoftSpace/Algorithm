import sys
from collections import deque
input = sys.stdin.readline

N,M,R= map(int,input().split())
G = [[] for i in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(N+1):
    G[i].sort()
    G[i].reverse()
visited=[0]*(N+1)
queue = deque()
#print(G)
def BFS(R):
    queue.append(R)
    count=1
    visited[R]=count
    while(queue):
        for u in G[queue.popleft()]:
            if visited[u]==0:
                queue.append(u)
                count+=1
                visited[u]=count
BFS(R)
#print(visited)
for i in range(1,N+1):
    print(visited[i])

