def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    answer = 0
    while left <= right :
        boat = limit
        if people[right] + people[left] <= limit :
            right -= 1
            left += 1
        else :
            right -= 1
        answer += 1
    
    return answer