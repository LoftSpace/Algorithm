
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
def solution(n):
    answer = []

    graph = []
    num = 0
    for i in range(n):
        graph.append([])
        num += (i+1)

    mode = 0
    D = 0
    R = 0
    U = 0

    cnt = n
    cnt2 = 0
    row = 0
    for i in range(num):
        if mode == 0:
            graph[row].insert(D, i+1)
            cnt2 += 1
            if cnt2 < cnt:
                row += 1
            elif cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                mode = 1
                D += 1

        elif mode == 1:
            graph[row].insert(D+cnt2, i+1)    
            cnt2 += 1
            if cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                mode = 2
                R += 1
                row -= 1

        elif mode == 2:
            graph[row].insert(len(graph[row])-U, i+1)
            cnt2 += 1
            if cnt2 < cnt:
                row -= 1
            elif cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                mode = 0
                U += 1
                row += 1

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            answer.append(graph[i][j])

    return answer