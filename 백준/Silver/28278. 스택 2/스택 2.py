import sys

input =sys.stdin.readline

n = int(input())
stack=[]
front=0
back=0

for i in range(n):
    command = input().split()
    
    if  command[0]=='1':
        stack.append(command[1])
        
        front+=1
    elif  command[0]=='2':
        if stack:
            print(stack.pop())
            front-=1
        else:
            print(-1)
    elif  command[0]=='3':
        print(len(stack))
    elif  command[0]=='4':
        
        if not stack:
            print(1)
        else:
            print(0)
    elif  command[0]=='5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    

