
def solution(word):
    case = ['A','E','I','O','U']
    global count
    count = 0 
    def dfs(string):
        global count
        count += 1
        if string == word :
            return True
        if len(string) == 5 :
            return False
        for i in case :
            # 여기서 정답 발견 시 탐색 중단하고 리턴
            if dfs(string + i):
                return True
    dfs('')
    
    return count - 1