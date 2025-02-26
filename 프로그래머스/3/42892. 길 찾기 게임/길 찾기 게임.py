from collections import deque
import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    max_y = 0
    result = [[],[]]
    max_location = 0
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
        if max_y < nodeinfo[i][1] :
            max_y = nodeinfo[i][1]
            max_location = i
   
    nodeinfo.sort(key = lambda x: x[0])
    
    def func(left,right,depth):
        if left <= right :
            #node num, depth, idx
            highest = [0,-1,0]
            for i in range(left,right + 1):
                if highest[1] < nodeinfo[i][1]:
                    highest[0] = nodeinfo[i][2]
                    highest[1] = nodeinfo[i][1]
                    highest[2] = i
            result[0].append(highest[0])

            #왼쪽 탐색
            func(left,highest[2] - 1,highest[1])
            #오른쪽 탐색
            func(highest[2] + 1,right,highest[1])
            
            result[1].append(highest[0])
    func(0,len(nodeinfo) - 1,0)
    
    #print(result)
    answer = result
    return answer