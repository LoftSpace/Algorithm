from collections import deque
def solution(numbers, target):
    N = len(numbers)
    answer = 0
    queue = deque()
    queue.append([0,0])
    while queue:
        index, current_number = queue.popleft()
        if index == N and current_number == target :
            answer += 1
        elif index < N :
            queue.append([index + 1, current_number + numbers[index]])
            queue.append([index + 1, current_number - numbers[index]])
            
    return answer