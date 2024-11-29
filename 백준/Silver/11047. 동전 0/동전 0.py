import sys

input = sys.stdin.readline

N , K = map(int,input().split())

coins = [0] * N

for coin in range(N):
    coins[coin] = int(input())

#coins.sort(reverse=True)

Sum = 0
coin = len(coins) - 1
count = 0

while K > 0 :
    count += K // coins[coin]
    K = K % coins[coin]
    coin -= 1
print(count)