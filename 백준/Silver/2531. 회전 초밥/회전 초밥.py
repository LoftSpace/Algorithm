import sys

input = sys.stdin.readline

N , d , k , c = map(int,input().split())
hash = [0] * (d + 1)
hash[c] = 1
table = []
total = 1
ans = 0

for i in range(N) :
    food = int(input())
    table.append(food)
# 초기 k개 배열
for i in range(0,k) :
    foodNum = table[i]
    # 초기 k개 배열에 새로운 원소 삽입이라면,
    if hash[foodNum] == 0 :
        total += 1
    hash[foodNum] += 1
ans = total



for left in range(1, N) :
    
    right = (left + k - 1) % N
    
    hash[table[left-1]] -= 1
    # k개 배열 내에서 원소가 사라졌다면,
    if hash[table[left-1]] == 0 :
        total -= 1
    # k개 배열내에서 원소가 하나라면,
    if hash[table[right]] == 0 :
        total += 1
    hash[table[right]] += 1
    
    ans = max(ans, total)
    
print(ans)