import sys

input=sys.stdin.readline

n=int(input())

s=list(map(int,input().split()))

ans=[-1]*n
stack=[]
count=[0]*1000001
''' O(N^2)
for i in range(n):
    a.append(s.count(s[i]))
'''
for i in range(n):
    count[s[i]]+=1

for i in range(n):
    while stack and count[s[stack[-1]]]< count[s[i]]:
        ans[stack[-1]]=s[i]
        stack.pop()
    stack.append(i)
print(" ".join(map(str,ans)))
    