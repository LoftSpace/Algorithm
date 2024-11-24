import sys

input = sys.stdin.readline

s = input().strip()
q = int(input())
arr = [[0 for i in range(26)] for i in range(len(s))]
arr[0][ord(s[0]) - 97] = 1
for i in range(1,len(s)):
    for j in range(26):
        arr[i][j] = arr[i-1][j]

    arr[i][ord(s[i])-97] += 1 

for i in range(q) :
    a = input().split()
    ans = 0

    if int(a[1]) > 0:
        ans = arr[int(a[2])][ord(a[0])-97] - arr[int(a[1])-1][ord(a[0])-97]
    else :#예외처리
        ans = arr[int(a[2])][ord(a[0]) - 97]
    print(ans)