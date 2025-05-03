s = input().strip()
a = s.count('a')
s = s * 2
ans = 100000000

for i in range(len(s)// 2):
    #print(s[i:i + a])
    ans = min(ans,s[i:i + a].count('b'))
print(ans)