import sys
input = sys.stdin.readline


while True :
    n, p = map(float,input().split())
    if n == 0 and p == 0.00 :
        break
    n = int(n)
    p = int(p * 100 + 0.5)
    dp = [0] * (p + 1)

    candies = []
    for i in range(n) :
        calorie , price = map(float,input().split())
        calorie = int(calorie)
        price  = int(price * 100 + 0.5)
        candies.append([calorie,price])

    for calorie, price in candies :
        for j in range(price, p + 1) :
            dp[j] = max(dp[j],dp[j-price] + calorie)

    print(max(dp))