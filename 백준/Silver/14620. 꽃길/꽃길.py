import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

def isIntersect(a,b) :
    if b != a + 1 and b != a + 2 and b != a + N - 1 and b != a + N and b != a + N + 1 and b != a + N + N :
        return False
    else: return True
    
    
def cost(row,col):
    return (board[row][col] + board[row + 1][col] + board[row-1][col] + board[row][col-1] + board[row][col+1]) 

ans = 10000000

for i in range(N * N) :
    for j in range(i + 1,N * N - 1):
        for k in range(j + 1,N * N - 2):
            if isIntersect(i,j) or isIntersect(j,k) or isIntersect(i,k):
                continue
            iRow = i // N
            iCol = i % N
            jRow = j // N
            jCol = j % N
            kRow = k // N
            kCol = k % N
            if 1 <= iRow < N-1 and 1 <= iCol < N-1 and 1 <= jRow < N-1 and 1 <= jCol < N-1 and 1 <= kRow < N-1 and 1<= kCol < N-1 :
               
                ans = min(ans,cost(iRow,iCol) + cost(jRow,jCol) + cost(kRow,kCol))

print(ans)