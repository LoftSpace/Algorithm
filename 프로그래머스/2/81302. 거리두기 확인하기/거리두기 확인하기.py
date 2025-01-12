from itertools import combinations
def solution(places):
    answer = [0,0,0,0,0]
    people = [[] for _ in range(5)]
    cases = []
    for i in range(5) :
        for j in range(5) :
            for k in range(5) :
                if places[i][j][k] == 'P' :
                    people[i].append([j,k])
                    
    #각 강의실에 대해 cases[i] = i 번째 강의실의 조합
    for place in people :
        cases.append(list(combinations(place,2)))
    
    
    def check(place):
        #각 사람 조합에 대해
        for case in cases[place] :
            first = case[0]
            second = case[1]
            distance = abs(second[1] - first[1]) + abs(second[0] - first[0])
            
            # 거리가 2 이하다
            if distance == 1 : 
                return False
            elif distance == 2 :
                # 같은 열
                if first[0] == second[0] :
                    # 사이에 파티션이 없다
                    if places[place][first[0]][first[1] + 1] == 'O' :
                        return False
                # 같은 행
                elif first[1] == second[1] :
                    if places[place][first[0] + 1][first[1]] == 'O' :
                        return False
                # 대각
                else :
                    if places[place][second[0]][first[1]] != 'X' or places[place][first[0]][second[1]] != 'X':
                        return False
                    
                   
                    
        return True
                            
                        
    #각 강의실에 대해
    for place in range(5) :
        if check(place) :
            answer[place] = 1
        else :
            answer[place] = 0
                            
    return answer