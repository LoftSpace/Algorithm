import sys

input  =sys.stdin.readline

arr = []
rotates = []
for i in range(4):
    temp = input().strip()
    temp2 = []
   
    for j in temp :
        temp2.append(int(j))
    arr.append(temp2)
N = int(input())
for i in range(N):
    rotates.append(list(map(int,input().split())))

def rotate_clock(clock):
#    print('시계방향 : ')
 #   print(clock)
    for gear in clock :
        
        temp = arr[gear][7]
        for i in range(7,-1,-1):
            arr[gear][i] = arr[gear][i - 1]
        arr[gear][0] = temp

def rotate_clock_reverse(clock_reverse):
    #print('반시계방향 :')
    #print(clock_reverse)
    for gear in clock_reverse:
        
        temp = arr[gear][0]
        for i in range(7):
            arr[gear][i] = arr[gear][i + 1]
        arr[gear][7] = temp


for rotate in rotates :
 #   print('rotate')
  #  print(rotate)
    gear_num, dir = rotate[0],rotate[1]
    cur_dir = dir
    start = gear_num - 1
    clock = []
    clock_reverse = []
    if dir == 1 :
        clock.append(start)
    else :
        clock_reverse.append(start)
    if start < 3  :
        for i in range(start,3):
        # print(arr[i][2],arr[i + 1][6])
            #반대로 돌려야 한다면 
            if arr[i][2] != arr[i + 1][6] :
            # print('must rotate')
                #현재 기어를 시계로 돌렸다면
                if cur_dir == 1 :
                    #다음 기어는 시계 반대로 
                    clock_reverse.append(i + 1)
                    #현재 방향 업데이트
                    cur_dir = -1
                else :
                    clock.append(i + 1)
                    cur_dir = 1
            else :
                break

    cur_dir = dir
   
    if start > 0 : 
        for i in range(start,0,-1):
            
            if arr[i][6] != arr[i-1][2] :
                if cur_dir == 1 :
                    #다음 기어는 시계 반대로 
                    clock_reverse.append(i -1)
                    #현재 방향 업데이트
                    cur_dir = -1
                else :
                    clock.append(i - 1)
                    cur_dir = 1
            else :
                break
    rotate_clock(clock)
    rotate_clock_reverse(clock_reverse)
   # for i in arr :
    #    print(i)

ans = 0
for index,i in enumerate(arr) :
    ans += i[0] * 2 ** index
#for i in arr :
 #   print(i)
print(ans)