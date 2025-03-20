def solution(n, times):
    MAX = max(times) * n
    
    left = 0
    right = MAX
    #left most
    while left <= right :
        mid = (left + right) // 2
        #print(left,mid,right)
        count = 0
        for i in times :
            count += (mid // i)
        if count < n :
            left = mid + 1
        elif count > n :
            right = mid - 1
        else :
            right = mid - 1
    return left