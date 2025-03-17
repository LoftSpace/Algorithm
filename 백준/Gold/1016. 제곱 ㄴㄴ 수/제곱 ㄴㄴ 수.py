import sys
input = sys.stdin.readline

Min, Max = map(int,input().split())
end = (int)(Max ** (1/2))
isPrime = [True] * (end + 1)

for i in range(2,end + 1):
    if not isPrime[i] :
        continue
    for j in range(i * 2,end + 1,i):
        isPrime[j] = False

count = 0
arr = []

for i in range(2,end + 1):
    if isPrime[i] :
        arr.append(i ** 2)
ans = 0
target = dict()
for i in range(Min,Max + 1):
    target[i] = True

for i in arr :
   # print(i)
    start = (Min // i) * i
    k = start
    while k <= Max :
        #print(k)
        if k in target :
            if target[k]:
                count += 1
                target[k] = False
        k += i


ans = Max - Min + 1 - count
print(ans)