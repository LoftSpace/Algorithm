# 조건 0 : 맵밖으로 나가면 동작 x
# 조건 1 : 지도위에 윗면 1, 동쪽 3인 상태로 놓여있음 
# 조건 2 : 가장 처음 주사위에는 모든 면 0
# 조건 3 : 주사위를 굴렸을 때 이동한 칸에 쓰인 수가 0이면 주사위 바닥면에 있는 수가 칸에 복사
# 조건 4 : 0이 아니면 칸에 쓰인 수가 주사위 바닥면에 복사되면서 칸에 쓰인 수는 0
def roll(move): # 조건 1을 기준으로 굴리기
    if move == 1: # 동쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2] # 주사위 변화 4 2 1 6 5 3
    elif move == 2: # 서쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3] # 주사위 변화 3 2 6 1 5 4
    elif move == 3: # 북쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1] # 주사위 변화 5 1 3 4 6 2
    elif move == 4: # 남쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4] # 주사위 변화 2 6 3 4 1 5

import sys
N, M, y, x, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dice_move = list(map(int, sys.stdin.readline().split()))
dice = [0, 0, 0, 0, 0, 0] # 조건 2
dy = [0, 0, -1, 1] 
dx = [1, -1, 0, 0]

for i in dice_move:
    if 0 <= y + dy[i-1] < N and 0 <= x + dx[i-1] < M: # 조건 0
        y = y + dy[i-1]
        x = x + dx[i-1]
        roll(i)
        if board[y][x] == 0: # 조건 3
            board[y][x] = dice[5]
        else : # 조건 4
            dice[5] = board[y][x]
            board[y][x] = 0
        print(dice[0])

