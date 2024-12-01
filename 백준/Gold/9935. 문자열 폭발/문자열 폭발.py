import sys
input= sys.stdin.readline

def check(): #K
    global l
    if len(stack)>=l:
        for i in range(-1-l+1,0):
            if stack[i]!=b[i+1+l-1]:
                return 0
    else:
        return 0
    return -1


s=input().strip()
b=input().strip()
stack=[]
l=len(b)
for i in range(len(s)): #N
    stack.append(s[i])
    if check()==-1:
        for j in range(l):
            stack.pop()
if len(stack)==0:
    print("FRULA")
else:
    for i in range(len(stack)):
        print(stack[i],end="")
