def solution(edges):
    nodes= set()
    numOfNodes = 0
    stick = 0
    doughnut = 0
    eightShape = 0
    newNode = 0
    maxNode = 0
    for edge in edges :
        u = edge[0]
        v = edge[1]
        nodes.add(u)
        nodes.add(v)
        maxNode = max(maxNode,u)
        maxNode = max(maxNode,v)
        
    for i in nodes:
        numOfNodes += 1
        
    inEdges = [0] * (maxNode + 1)
    outEdges = [0] * (maxNode + 1)
   
    for edge in edges :
        u = edge[0]
        v = edge[1]
        
        inEdges[v] += 1
        outEdges[u] += 1
    
    newPoint = 0
    for i in range(1,maxNode + 1) :
        if i in nodes:
            if outEdges[i] == 0 :
                stick += 1
            elif inEdges[i] >= 2 and outEdges[i] == 2 :
                eightShape += 1
            elif inEdges[i] == 0 and outEdges[i] >= 2 :
                newNode = i
            
    doughnut = outEdges[newNode] - stick - eightShape
    
    answer = []
    answer.append(newNode)
    answer.append(doughnut)
    answer.append(stick)
    answer.append(eightShape)
 
    return answer
