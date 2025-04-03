import sys



input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

can_see = [0] * N
min_dist = [[100000000,0] for _ in range(N)]
stack = []
stack.append([0,arr[0]])
#print(min_dist)
for building in range(1,N) :    
    #print(building)
    #print(stack)
    while stack and stack[-1][1] <= arr[building] :
        stack.pop()
    if stack :
        can_see[building] += len(stack)
        if min_dist[building][0] > abs(stack[-1][0] - building) :
            min_dist[building] = [abs(stack[-1][0] - building),stack[-1][0] + 1]
        
    stack.append([building,arr[building]])
stack = []
stack.append([N - 1,arr[-1]])
#print(min_dist)
for building in range(N - 1,-1,-1):
 #   print(stack)
    while stack and stack[-1][1] <= arr[building] :
        stack.pop()
    if stack :
        can_see[building] += len(stack)
        #갱신해야됨
        if min_dist[building][0] > abs(stack[-1][0] - building) :
            min_dist[building] = [abs(stack[-1][0] - building),stack[-1][0] + 1]
        # 최소 거리가 같다
        elif min_dist[building][0] == abs(stack[-1][0] - building) :
            #건물 번호가 더 작다면 갱신
            if min_dist[building][1] > stack[-1][0] + 1 :
                min_dist[building] = [abs(stack[-1][0] - building),stack[-1][0] + 1]

    stack.append([building,arr[building]])

#print(can_see)
#print(min_dist)
for index,i in enumerate(can_see) :
    if i == 0 :
        print(0)
    else :
        print(i,min_dist[index][1])