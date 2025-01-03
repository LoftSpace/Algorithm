
def solution(storey):
    answer = 0
    while storey :
        remainder = storey % 10
        if remainder < 5 :
            answer += remainder
        elif remainder > 5 :
            answer += (10-remainder)
            storey += 10
        else :
            if (storey // 10) % 10 >= 5 :
                answer += remainder
                storey += 10
            else :
                answer += remainder
        storey //= 10
    return answer