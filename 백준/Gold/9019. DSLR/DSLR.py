import sys
from collections import deque

input = sys.stdin.readline

#input : string
## return : string
def D(A):
    1 
    a = int(A)
    aStr = str((a * 2) % 10000)
    lengthA = len(aStr)
    if lengthA != 4:
        return ('0' * (4 - lengthA)) + aStr
    return aStr
def S(A):
    a = int(A)
    if a - 1 >= 0 :
        aStr = str(a-1)
    else :
        return "-"
    lengthA = len(aStr)
    if lengthA != 4:
        return ('0' * (4 - lengthA)) + aStr
    return aStr

def L(A):
    temp = A[0]
    a = A[1:]
    a += temp
    return a
def R(A) :
    temp = A[3]
    a = A[:3]
    temp += a
    return temp

def BFS(A,B):
    visited = [False] * 10000
    queue = []
    queue = deque()
    queue.append([A,''])
    visited[A] = True
    while queue :
        num , ops = queue.popleft()
        if num == B :
            print(ops)
            break

        D = num * 2 % 10000
        if not visited[D] :
            visited[D] = True
            queue.append([D,ops + 'D'])
        
        S = (num - 1) % 10000
        if not visited[S] :
            visited[S] = True
            queue.append([S, ops + 'S'])

        L = num//1000 + (num % 1000) * 10     
        if not visited[L] :
            visited[L] = True
            queue.append([L,ops + 'L'])

        R = num // 10 + (num % 10) * 1000
        if not visited[R] :
            visited[R] = True
            queue.append([R,ops + 'R'])

T = int(input())
for i in range(T):
    A , B = map(int,input().split())
    BFS(A,B)
