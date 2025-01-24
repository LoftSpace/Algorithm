def solution(numbers):
    arr = [str(i) for i in numbers]
    arr.sort(reverse = True, key = lambda x : x*3)
    
    answer = ''.join(arr)
    return str(int(answer))