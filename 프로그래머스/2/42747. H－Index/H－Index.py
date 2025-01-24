def solution(citations):
    citations.sort(reverse = True)
    Max = 0
    n = len(citations)
    for i in range(n):
        Max = max(Max,min(citations[i], i + 1))
    
    return Max