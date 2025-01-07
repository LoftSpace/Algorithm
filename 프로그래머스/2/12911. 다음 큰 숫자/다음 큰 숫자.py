def solution(n):
    check = bin(n)[2:].count('1')
    n += 1
    while True :
        if bin(n)[2:].count('1') == check :
            break
        n +=1
    answer = n
    return answer