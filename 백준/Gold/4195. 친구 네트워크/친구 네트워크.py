import sys

input = sys.stdin.readline



def union(a,b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot == bRoot :
        return
    else :
        parent[bRoot] = aRoot
        size[aRoot] += size[bRoot]

def find(a):
    if parent[a] != a :
        parent[a] = find(parent[a])
    return parent[a]

T = int(input())
for t in range(T) :
    F = int(input())
    parent = dict()
    size = dict()

    for i in range(F) :
        a,b = map(str,input().split())
        if a not in parent :
            parent[a] = a
            size[a] = 1
        if b not in parent :
            parent[b] = b
            size[b] = 1
        union(a,b)
        
        print(size[find(a)])
