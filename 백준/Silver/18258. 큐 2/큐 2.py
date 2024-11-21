import sys
from collections import deque
input= sys.stdin.readline

deque= deque()

n = int(input())
for _ in range(n):
    cmd=input()
    if 'push' in cmd:
        l=cmd.split()
        deque.append(int(l[1]))
        #print(deque)
    elif cmd=='pop\n':
        if len(deque)!=0:
            print(deque.popleft())
        else:
            print(-1)
    elif cmd=='size\n':
        print(len(deque))
    elif cmd=='empty\n':
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif cmd=='front\n':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif cmd=='back\n':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])
     
   