def solution(n, s, a, b, fares):
    INF = int(1e8)
    graph = [[INF] * (n+1) for _ in range(n + 1)]
    answer = INF
    for edge in fares:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        graph[u][v] = w
        graph[v][u] = w
    for i in range(1, n + 1):
        graph[i][i] = 0
    for k in range(1, n + 1):
        for u in range(1, n + 1):
            for v in range(1, n + 1):
                graph[u][v] = min(graph[u][v], graph[u][k] + graph[k][v])
    
    for u in range(1, n + 1):
        #if u!=s :
            #합승을 한다면
        answer = min(answer,graph[s][u] + graph[u][a] + graph[u][b])
    #따로 간다면
    answer = min(answer,graph[s][a] + graph[s][b])
    
    return answer