import sys

input = sys.stdin.readline

N, M, L, K = map(int,input().split())

stars = []

for i in range(K):
    x,y = map(int,input().split())
    stars.append([x,y])
ans = 0

for i in stars :
    x1, y1 = i[0],i[1]
    for j in stars :
        x2,y2 = j[0],j[1]
        standard_x ,standard_y= min(x1,x2),min(y1,y2)
        count = 0
        for k in stars :
            if standard_x <= k[0] <= standard_x + L and standard_y <= k[1] <= standard_y + L :
                count += 1
        ans = max(ans,count)

print(K - ans)