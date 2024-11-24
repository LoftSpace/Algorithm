import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N , M = map(int,input().split())
count = 0
visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = 1
    for nextNode in graph[node]:
        if visited[nextNode] == 0:
            dfs(nextNode)

for i in range(1,len(visited)):
    if visited[i] == 0 :
        count += 1
        dfs(i)

print(count)