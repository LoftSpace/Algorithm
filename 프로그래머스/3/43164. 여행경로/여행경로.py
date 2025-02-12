import heapq
def solution(tickets):
    used = [False] * len(tickets)
    answer = []
    
    def dfs(currentNode, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return 
        else :
            for index,ticket in enumerate(tickets) :
                if ticket[0] == currentNode and not used[index] :
                    used[index] = True
                    dfs(ticket[1],path + [ticket[1]])
                    used[index] = False
    
    dfs('ICN',['ICN'])
    answer.sort()
    return answer[0]