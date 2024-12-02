import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = map(int,input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M) :
    u ,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start,end):
    queue = []
    queue = deque()
    queue.append([start,0])

    while queue :
        node , count = queue.popleft()
        if node == end :
            print(count)
            return
        for nextNode in graph[node]:
            if not visited[nextNode]:
                queue.append([nextNode,count + 1])
                visited[nextNode] = True
    print(-1)
bfs(a,b)

