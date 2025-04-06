import sys
import heapq
input = sys.stdin.readline

arr = []
N = int(input())
hash = dict()
heap = []
ans = 0

heapq.heapify(heap)

for i in range(N):
    location, height = map(int,input().split())
    arr.append(height)

for i in range(N) :
    cur_height = arr[i]
   # print(cur_height)
    #if heap : 
     #   print(heap)
    #리스트에 이 높이가 없으면 해시와 힙에 넣는다
    if cur_height not in hash or not hash[cur_height]:
        hash[cur_height] = True
        heapq.heappush(heap,-cur_height)
    #현재 높이보다 큰 것들 전부 pop, 힙에서 삭제
    while -heap[0] > cur_height :
        removed_building = -heapq.heappop(heap)
        hash[removed_building] = False
        ans += 1

for i in heap :
    if i != 0 :
        ans += 1
print(ans)