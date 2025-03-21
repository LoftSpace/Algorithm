import sys

input = sys.stdin.readline

N,a,b = map(int,input().split())

if a + b  > N + 1 :
    print(-1)

else :
    add_count = N - (a + b - 1)
    ans = []
    if a >= b :
        
        for i in range(add_count):
            ans.append(1)
        for i in range(1,a + 1):
            ans.append(i)
        for j in range(b-1,0,-1):
            ans.append(j)
       
    if a < b :
        if a > 1 :
            for i in range(add_count):
                ans.append(1)
            for i in range(1,a):
                ans.append(i)
            for j in range(b,0,-1):
                ans.append(j)
        else :
            ans.append(b)
            for i in range(add_count):
                ans.append(1)
            for j in range(b-1,0,-1):
                ans.append(j)
    print(*ans)
            
       