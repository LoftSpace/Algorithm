def solution(arr):
    answer = []
    global zero
    global one
    zero = 0
    one = 0
    def devide_and_conquer(row1,col1,row2,col2):
        
        global one
        global zero
        first_element = arr[row1][col1]
        devide = False
        for row in range(row1,row2 + 1):
            for col in range(col1,col2 + 1):
                if first_element != arr[row][col] :
                    devide = True
                    break
        
        if devide : 
            #print(row1,col1,row2,col2)
            #print("devide")
            mid_row = (row1 + row2) // 2
            mid_col = (col1 + col2) // 2
            devide_and_conquer(row1,col1,mid_row,mid_col)
            devide_and_conquer(row1,mid_col + 1,mid_row,col2)
            devide_and_conquer(mid_row + 1,col1,row2,mid_col)
            devide_and_conquer(mid_row + 1,mid_col + 1,row2,col2)
        else :
            #print(row1,col1,row2,col2)
            #print("finish")
            if first_element == 1 :
                one += 1
            else :
                zero += 1
    devide_and_conquer(0,0,len(arr) - 1,len(arr[0]) - 1)
    answer.append(zero)
    answer.append(one)
    return answer