import sys

input = sys.stdin.readline

n , m = map(int,input().split())

parent = [0] * n


def union(a,b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot > bRoot :
        parent[aRoot] = bRoot
    else :
        parent[bRoot] = aRoot

def find(a):
    if parent[a] != a:
        parent[a] =  find(parent[a])
    return parent[a]

for i in range(n):
    parent[i] = i

for i in range(m) :
    #print(parent)
    a,b = map(int,input().split())

    #합치기 전에 사이클  체크
    if find(a) == find(b) :
        print(i + 1)
        exit()

    union(a,b)
print(0)