import sys

input = sys.stdin.readline

T = int(input())


def union(a,b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot == bRoot :
        return
    else :
        network[bRoot] = aRoot
        people[aRoot] += people[bRoot]

def find(a):
    if network[a] != a:
        network[a] = find(network[a])
    return network[a]


for t in range(T):
    F = int(input())
    network = dict()
    people = dict()

    for i in range(F):
        f1 , f2 = map(str,input().split())
        
        if f1 not in network :
            network[f1] = f1
            people[f1] = 1
        if f2 not in network:
            network[f2] = f2
            people[f2] = 1
        union(f1,f2)
        print(people[find(f1)])