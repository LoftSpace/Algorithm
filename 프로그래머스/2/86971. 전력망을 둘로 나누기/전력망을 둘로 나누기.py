from collections import deque
def solution(n, wires):
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    #그래프 생성
    for wire in wires :
        u,v = wire[0],wire[1]
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(u,v):
        queue = deque()
        queue.append(u)
        count = 1
       
        while queue :
            
            node = queue.popleft()
            visited[node] = True
            for nextNode in graph[node] :
                if not visited[nextNode] and nextNode != v :
                    
                    visited[nextNode] = True
                    count += 1
                    queue.append(nextNode)
        return count
    def init() :
        for i in range(n + 1) :
            visited[i] = False
    ans = 10000000
    #각 wire에 대하여
    for wire in wires :
        # u -> v
        u,v = wire[0], wire[1]
        a,b = bfs(u,v) , bfs(v,u)
        init()
       
        ans = min(ans,abs(a-b))
        
    answer = ans
    return answer