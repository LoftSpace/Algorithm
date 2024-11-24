import sys
input = sys.stdin.readline


N = int(input())

T = [1]
P = [0]
Max = 0

for i in range(N):
    t , p = map(int,input().split())
    T.append(t)
    P.append(p)

def func(day, t , p):
    global Max
    Max = max(Max , p)
    # 다음 상담일 찾기
    for k in range(day + t, N + 1):
        # k일짜의 상담이 퇴사일을 넘기지 않을 때
        if k + T[k] - 1 <= N :
            #print("%d -> %d and %d -> %d" %(day,k,p,p+P[k]))
            func(k,T[k],p + P[k])
            
func(0,1,0)
print(Max)