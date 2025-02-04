def solution(n, computers):
    network = [0] * n
    def union(a,b):
        
        aRoot = find(a)
        bRoot = find(b)
        if aRoot < bRoot : 
            network[bRoot] = aRoot
        else :
            network[aRoot] = bRoot
            
    def find(a):
        if network[a] != a :
            return find(network[a])
        return network[a]
    
    # init network
    for i in range(n):
        network[i] = i
    
    for i in range(len(computers)):
        for j in range(i,len(computers)):
            if computers[i][j] == 1:
                union(i,j)
    arr = set()
    for i in range(n):
        arr.add(find(i))
   
    answer = len(arr)
    return answer