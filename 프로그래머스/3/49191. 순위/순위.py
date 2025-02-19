def solution(n, results):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for edge in results:
        u = edge[0]
        v = edge[1]
        graph[u][v] = 1
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
    count = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if graph[u][v] != 1e9:
                count[u] += 1
                count[v] += 1
    for i in count : 
        if i == n - 1:
            answer += 1
    
    return answer