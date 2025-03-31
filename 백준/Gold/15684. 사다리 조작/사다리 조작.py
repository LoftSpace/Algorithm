import sys
N,M,H = map(int, sys.stdin.readline().split())
sadari = [[0] * N for _ in range(H)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    sadari[a-1][b-1] = 1


# 1자로 내려가는지 확인하는 함수 = bebero
# 가로선 개수 0개부터 3개까지 생성하고 bebero 함수 실행 완전탐색
def bebero(): # 1자로 내려가는지 확인하는 함수 1자로 내려가면 True 아니면 False
    for i in range(N): # 처음 시작할 사다리 번호
        start_num = i   
        for j in range(H):
            if sadari[j][start_num]==1:
                start_num += 1
            elif start_num>0 and sadari[j][start_num-1] == 1:
                start_num -= 1    
        if i != start_num:
            return False
    return True
def dfs(cnt, x, y):
    global answer
    if answer <= cnt:   # 가로선을 정답보다 많이 만든 경우 확인 필요 x
        return
    if bebero():      # i번 세로선의 결과가 i번이 나오는지 체크
        answer = min(answer, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, H): 
        for j in range(0, N - 1):
            if sadari[i][j] == 0: # 0인 경우 가로줄 만들고, 연속된 가로선을 만들지 않기 위해 j + 2호출
                sadari[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                sadari[i][j] = 0
answer = 4
dfs(0,0,0)
if answer>3:
    answer = -1
print(answer)
