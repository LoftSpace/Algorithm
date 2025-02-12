def solution(n, times):
    left = 0
    right = max(times) * n
    while left <= right :
        mid = (left + right) // 2
        people = 0
        for i in times :
            people += (mid // i)
        if people < n :
            left = mid + 1
        else :
            right = mid - 1
    answer = left
    return answer