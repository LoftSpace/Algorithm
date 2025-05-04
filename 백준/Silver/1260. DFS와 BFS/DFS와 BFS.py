# 백준 1260 : DFS와 BFS

# 초기 세팅
N, link, V = map(int, input().split())
graph = [ []*(N+1) for _ in range(N+1)]

# 인접 리스트 만들기
for i in range(link):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
# 방문 여부 체크
visited_1 = [False]*(N+1) # dfs용
visited_2 = [False]*(N+1) # bfs용

# 1. DFS 만들기
dfs_visited = []
def dfs(graph, v, visited):
    if visited[v] == False:
        visited[v] = True
        
    global dfs_visited
    dfs_visited.append(v)
    
    # 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            

# 2. BFS 만들기
bfs_visited = []
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v]) # start에 대한 큐
    
    if visited[v] == False:
        visited[v] = True
        
    global bfs_visited
    while queue:
        # 큐에서 하나씩 원소를 뽑아 출력
        i = queue.popleft()
        bfs_visited.append(i) # 방문한 노드 저장
        # 해당 원소(i)와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for j in graph[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
            
            
dfs(graph, V, visited_1)
bfs(graph, V, visited_2)
print(*dfs_visited, sep = ' ')
print(*bfs_visited, sep = ' ')