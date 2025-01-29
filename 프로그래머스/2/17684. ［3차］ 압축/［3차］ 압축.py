from collections import deque
def solution(msg):
    answer = []
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    queue = deque(msg)
    hash = dict()
    
    for index,i in enumerate(characters) :
        hash[i] = index + 1
    count = 26
    #print(hash)
    
    while queue :
        temp = queue[0]
        search_length = 1
        # 남은 큐의 길이가 충분하다면
        while search_length < len(queue) :
            temp += queue[search_length]
            search_length += 1
            # 색인 추가
            if temp not in hash :
                count += 1
                hash[temp] = count
                temp = temp[:-1]
                search_length -=1
                break
        for j in range(search_length):
            queue.popleft()
        # 출력
        answer.append(hash[temp])
    #print(hash)
    
    
    
    return answer