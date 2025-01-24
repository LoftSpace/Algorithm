def solution(name):
    N = len(name)
    answer = 0
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    position = []
    
    for index,i in enumerate(name) :
        if i != 'A':
            position.append(index)
        if ord(i) - ord('A') < 14 :
            answer += (ord(i) - ord('A'))
        else :
            answer += (ord('Z') - ord(i) + 1)
    Min = N - 1
    for i in range(N):
        if name[i] == 'A':
            temp = i
            while temp < N and name[temp] == 'A':
                temp += 1
            left = (0 if i == 0 else i - 1)
            right = N - temp
            Min = min(Min,left + right + min(left,right) )
    answer += Min
    return answer