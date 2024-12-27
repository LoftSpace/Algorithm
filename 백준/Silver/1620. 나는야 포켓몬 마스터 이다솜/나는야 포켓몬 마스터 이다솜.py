import sys

input = sys.stdin.readline

N , M = map(int,input().split())

number_to_name = dict()
name_to_number = dict()
number = '0123456789'
for i in range(1,N + 1) :
    name = input().split()[0]
    number_to_name[i] = name
    name_to_number[name] = i
ans = []
for i in range(1, M + 1) :
    a = input().split()[0]
    if a[0] in number :
        ans.append(number_to_name[int(a)])
    else :
        ans.append(name_to_number[a])

for i in ans :
    print(i)
