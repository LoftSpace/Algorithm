def solution(files):
    digits = '0123456789'
    seperated_files = []
    answer = []
    for file in files :
        number_start = 0
        for index,i in enumerate(file) :
            # 숫자 발견
            if i in digits :
                number_start = index
                break
        while index < len(file) and file[index] in digits :
            index += 1
        number_end = index - 1
        #print(number_end)
        
        if number_end != len(file) - 1:
            seperated_files.append([file[:number_start],file[number_start:number_end + 1],file[number_end + 1:]])
        else :
            seperated_files.append([file[:number_start],file[number_start:number_end + 1]])
        
    seperated_files.sort(key = lambda x : (x[0].casefold(),int(x[1])))
    
    
    
    for i in seperated_files :
        if len(i) == 3 :
            answer.append(i[0] + i[1] + i[2])
        else :
            answer.append(i[0] + i[1])
    
    return answer