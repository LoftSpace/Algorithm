import sys

n = int(input())
s=list(map(int,input().split()))
ans=[-1]*n
stack=[]  #원래 스택의 담을 요소의 index저장 

for i in range(n):

    while stack and s[i] > s[stack[-1]]: #스택의 top값과 인풋값중 비교 
        
        ans[stack[-1]]=s[i] #사실 스택은 index를 저장하므로 
        stack.pop() #스택의 top의 오큰수를 찾음
    stack.append(i)
print(*ans)
        
