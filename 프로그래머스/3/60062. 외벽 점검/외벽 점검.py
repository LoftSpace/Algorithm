from itertools import permutations
import copy
def solution(n, weak, dist):
    answer = 10000000
    length = len(weak)
    weak = weak + [num + n for num in weak ]
    #각 시작점에 대해
    for start in range(length):
        #각 경우의 수에 대해
        for friends in list(permutations(dist)):
            # 첫 친구 투입
            count = 1
            # 첫친구 투입후 위치 갱신
            position = weak[start] + friends[count - 1]
            canFix = True
            
            #그 이후에 취약점 탐색
            for i in range(start,start + length):
                #이전 친구가 이번 취약점까지 커버하지 못했다면
                if weak[i] > position :
                    count += 1
                    # 더이상 친구가 없다면
                    if count > len(dist):
                        canFix = False
                        break
                    #새로운 친구 투입
                    position = weak[i] + friends[count - 1]
            if canFix :
                answer = min(answer,count)
                
    if answer > len(dist):
        return -1
    return answer