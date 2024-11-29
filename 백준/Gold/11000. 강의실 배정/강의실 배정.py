import sys
import heapq

input = sys.stdin.readline

N = int(input())

lectures = []
rooms = [0]
queue = []

heapq.heappush(queue,0)

for i in range(N) :
    lectures.append(list(map(int,input().split())))

lectures.sort(key = lambda x : [x[0],x[1]])

for lecture in lectures :
    if queue[0] <= lecture[0] :
        heapq.heappop(queue)
        heapq.heappush(queue,lecture[1])
    else :
        heapq.heappush(queue,lecture[1])

print(len(queue))

