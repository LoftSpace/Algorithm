from collections import deque
def solution(info, edges):
    N = len(info)
    answer = 0
    graph = [[] for _ in range(N)]
    
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        if info[child] == 0:
            weight = 1
        else :
            weight = -1
        graph[parent].append([child,weight])
    
    queue = deque([])
    p = set()
    queue.append([0,p,1,0])
   
    while queue :
        node,path,sheep,wolf = queue.popleft()
        answer = max(answer,sheep)
        #if sheep == 6:
         #   print(path)
        #인접한 노드들을 방문 가능 노드에 넣는다
        for i in graph[node]:
            path.add((i[0],i[1]))
            
        #방문 가능한 노드 중
        for nextNode in path:
            nextNode_num = nextNode[0]
            nextNode_weight = nextNode[1]
            if sheep - wolf + nextNode_weight > 0 :
                temp = path.copy()
                temp.remove(nextNode)
                if nextNode_weight == 1:
                    queue.append([nextNode_num,temp, sheep + 1,wolf])
                else :
                    queue.append([nextNode_num,temp, sheep,wolf + 1])
    
    return answer