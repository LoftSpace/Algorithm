import sys
import math

input = sys.stdin.readline
N = int(input())
end = int(N **(1/2))
isPrime = [True] * (N + 1)
for i in range(2,end + 1):
    if not isPrime[i]:
        continue
    for j in range(i + i,N + 1,i):
        isPrime[j] = False
primes = []

for i in range(2,N + 1):
    if isPrime[i] :
        primes.append(i)

right = 0
left = 0

arrSum = [0] * (len(primes) + 1)
for i in range(1,len(primes) + 1):
    arrSum[i] = arrSum[i-1] + primes[i-1]
#print(arrSum)
ans = 0

for left in range(len(primes) + 1):
    

    while  right < len(arrSum) and arrSum[right] - arrSum[left] < N :
        right += 1

    if right < len(arrSum) and arrSum[right] - arrSum[left] == N :
        ans += 1
        continue
        
print(ans)