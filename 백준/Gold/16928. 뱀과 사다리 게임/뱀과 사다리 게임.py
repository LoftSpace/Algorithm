import sys
from collections import deque
input=sys.stdin.readline

visited=[-1]*101
#-1: not visited, -2: visited
N,M=map(int,input().split())
for _ in range(N+M):
    u,v=map(int,input().split())
    visited[u]=v

count=[0]*101
def BFS():
    queue=deque()
    queue.append(1)
    while(queue):
        u=queue.popleft()
        if u==100:
            #print(count)
            break
        for v in (u+1,u+2,u+3,u+4,u+5,u+6):
            if v <=100:
                if visited[v]==-1:
                    queue.append(v)
                    visited[v]=-2
                    count[v]=count[u]+1
                    
                elif visited[v]!=-2: #jump to next node
                    if visited[visited[v]]==-2:
                        if count[visited[v]] < count[u]+1:
                            continue
                    #print('jump to %d from %d'%(visited[v],v))
                    queue.append(visited[v])
                    count[v]=count[u]+1
                    count[visited[v]]=count[u]+1
                    #print("count[%d] is %d"%(visited[v],count[visited[v]]))
                    visited[visited[v]]=-2
                    visited[v]=-2
                    
                else: 
                    if count[v] > count[u]+1:
                        queue.append(v)
                        count[v]=count[u]+1

                        
BFS()
print(count[100])