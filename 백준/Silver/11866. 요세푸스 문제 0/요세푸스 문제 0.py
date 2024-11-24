import sys
#from collections import deque

n,k=map(int,input().split())
q=[]
s=[]
count=1
for i in range(n):
    q.append(i+1)
'''
while(q): #O(NK)
    for _ in range(k-1):
        q.append(q.popleft())
    s.append(q.popleft())
'''
idx=0
while(q):
    idx+=k-1
    if idx >=len(q):
        idx%=len(q)
    s.append(str(q.pop(idx)))

print('<',", ".join(s),">",sep="")
