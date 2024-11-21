import sys
input=sys.stdin.readline

n=int(input())
dp=[1,1]
num=0
num1=0
def fib(n):
    global num
    if n==1 or n==2:
        num+=1
        return 1
    else:
        
        return fib(n-1)+fib(n-2)

for i in range(2,n):
    dp.append(dp[i-1]+dp[i-2])
    num1+=1

fib(n)
print(num,end=" ")
print(num1)

