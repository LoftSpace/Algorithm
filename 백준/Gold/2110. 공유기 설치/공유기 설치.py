import sys

input = sys.stdin.readline

N, C = map(int,input().split())

houseLocations = [0] * N

for houseLocation in range(N):
    houseLocations[houseLocation] = int(input())

houseLocations.sort()


left = 1
right = houseLocations[N-1] - houseLocations[0]

def C_possible(distance):
    i = 0
    count = 1
    start = houseLocations[0]

    while i <= N - 1 :
        end = houseLocations[i]
        if end - start >= distance :
            start = houseLocations[i]
            count += 1
        i += 1
    return count

while left <= right :
    mid = (left + right) // 2
    
    if C_possible(mid) >= C : 
        left = mid + 1
    else :
        right = mid - 1

print(right)