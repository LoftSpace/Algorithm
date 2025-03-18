def solution(numbers):
    def int_to_bin(number):
        return bin(number)[2:]
    def binary_to_int(binary):
        count = 0
        Sum=0
        for i in range(len(binary)-1,-1,-1):
            Sum += (2 ** count) * int(binary[i])
            count += 1
        return Sum
    
    answer= []
    for number in numbers :
        binary = list(int_to_bin(number))
       # print(binary)
        if '0' not in binary :
            binary = ['1','0'] + binary[1:]
            #print(binary)
            answer.append(binary_to_int(binary))
        elif binary[-1] == '0':
            answer.append(number + 1)
        else :
            for i in range(len(binary)-1,-1,-1):
                if binary[i] == '0' :
                    binary[i] = '1'
                    binary[i + 1] = '0'
                    break
            #print(binary)
            answer.append(binary_to_int(binary))
    
    
    return answer