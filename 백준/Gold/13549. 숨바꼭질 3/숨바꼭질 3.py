import sys
import heapq

INF = 1e8

start,end = map(int,input().split())

graph = [[] for _ in range(200001)]
dist = [INF]*(200001)
dist[start]=0

for node in range(0,100001):
    if node -1 >=0:
        graph[node].append((1,node-1))
    graph[node].append((1,node+1))
    graph[node].append((0,node*2))



def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))

    while(queue):

        #print(queue)
        cost , node = heapq.heappop(queue)

        if dist[node] < cost:
            continue

        for nextNode in graph[node]:
            if dist[nextNode[1]] > nextNode[0] + dist[node] :
                dist[nextNode[1]] = nextNode[0] + dist[node]
                heapq.heappush(queue,(dist[nextNode[1]],nextNode[1]))

dijkstra(start)

print(dist[end])