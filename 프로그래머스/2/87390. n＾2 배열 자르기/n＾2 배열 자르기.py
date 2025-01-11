def solution(n, left, right):
    arr = []
    start = left // n
    end = right // n
    gap = right - left
    for i in range(start + 1,end + 2):
        
        for j in range(i) :
            arr.append(i)
        for j in range(i + 1, n + 1):
            arr.append(j)
    #print(arr)
    s = left % n
    answer = arr[s:s + gap + 1]
    return answer