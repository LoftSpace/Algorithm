import sys
input = sys.stdin.readline
#variables

t =int(input())
sum=0
for _ in range(t):
    k=int(input())
    K=k
    files=list(map(int,input().split()))
    sums=[files[0]]

    for i in range(1,len(files)):
        sums.append(sums[i-1]+files[i])

    dp=[[0]*k for i in range(k)]
    for i in range(len(files)-1):
        dp[i][i+1]=files[i]+files[i+1]
    for j in range(2,len(files)):
        i=0
        while i+j <len(files):
            for k in range(i,i+j):
                if i==0:
                    sum=sums[i+j]
                else:
                    sum= sums[i+j]-sums[i-1]
                if dp[i][i + j] == 0:
                    dp[i][i + j] = dp[i][k] + dp[k + 1][i + j] + sum
                else:
                    dp[i][i + j] = min(dp[i][i + j], dp[i][k] + dp[k + 1][i + j] + sum)
                
            i+=1   
    print(dp[0][-1])