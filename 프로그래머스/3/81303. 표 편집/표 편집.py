
def solution(n, k, cmd):
    linked_list = {i : [i,i-1,i+1] for i in range(n)}
    linked_list[n-1][2] = -1
    answer = ['O'] * n
    stack = []
    i = 0
    
    for command in cmd :    
        if command[0] == 'U' or command[0] == 'D':
            c1, c2 = command.split(' ')
            c2 = int(c2)
            if c1 == 'U':
                for i in range(c2):
                    k = linked_list[k][1]
            else : 
                for i in range(c2):
                    k = linked_list[k][2]
                
        elif command[0] == 'C':
            answer[k] = 'X'
            prev = linked_list[k][1]
            next = linked_list[k][2]
            stack.append([k,prev,next])
            
            #첫번째 원소 삭제
            if prev == -1 :
                linked_list[next][1] = -1
                k = next
            # 마지막 원소 삭제
            elif next == -1:
                linked_list[prev][2] = -1
                k = prev
            else :
                linked_list[prev][2] = next
                linked_list[next][1] = prev
                k = next
                
        elif command[0] == 'Z':
            node, prev, next = stack.pop()
            answer[node] = 'O'
            if prev == -1:
                linked_list[next][1] = node
            elif next == -1 :
                linked_list[prev][2] = node
            else :
                linked_list[prev][2] = node
                linked_list[next][1] = node
    #print(answer)  
    return ''.join(answer)
