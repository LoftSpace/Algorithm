import sys
sys.setrecursionlimit(10**5)
N,M,R = map(int,input().split())
G = [[] for i in range(N+1)]
visited=[0]*(N+1)
#print(G)
for i in range(M):
    u,v=map(int,input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(N+1):
    G[i].sort()
#print(G)
count=0
def DFS_Visit(i):
    global count
    count+=1
    visited[i]=count
    for j in G[i]:
        #print("%d->%d"%(i,j))
        if visited[j]==0:
            DFS_Visit(j)
    

def DFS(R):
    DFS_Visit(R)

DFS(R)
for i in range(1,N+1):
    print(visited[i])
