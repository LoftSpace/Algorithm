N = int(input())

arr = list(map(int,input().split()))

stack = []
ans = [0] * N
for index,height in enumerate(arr) : 
    if not stack : 
        stack.append([height,index])
    else :
        while stack and stack[-1][0] < height :
            stack.pop()
        if stack : 
            ans[index] = (stack[-1][1] + 1)
        stack.append([height,index])
print(*ans)