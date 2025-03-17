import sys
from collections import deque
T = int(input())
ans = []
for t in range(T):
    N, K = map(int,input().split())
    weights = [0]
    inEdge = [0] * (N + 1)
    complete_time = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    queue = deque([])

    temp = list(map(int,input().split()))
    for i in temp :
        weights.append(i)

    for i in range(K):
        u,v = map(int,input().split())
        graph[u].append(v)
        inEdge[v] += 1

    W = int(input())

    for i in range(1, N + 1):
        if inEdge[i] == 0 :
            queue.append(i)
            complete_time[i] = weights[i]

    while queue :
        cur_node = queue.popleft()
        if cur_node == W :
            break
        for nextNode in graph[cur_node]:
            inEdge[nextNode] -= 1
            if inEdge[nextNode] == 0 :
                queue.append(nextNode)
            complete_time[nextNode] = max(complete_time[nextNode],complete_time[cur_node] + weights[nextNode])


    ans.append(complete_time[W])
for i in ans :
    print(i)