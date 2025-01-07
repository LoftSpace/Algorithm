def gcd(a,b):
    
    if b == 0 :
        return a
    else :
        return gcd(b,a%b)

def solution(arrayA, arrayB):
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    answer = 0
   
    for i in arrayA :
        
        gcdA = gcd(gcdA,i)
    for i in arrayB :
        gcdB = gcd(gcdB,i)
    print(gcdA,gcdB)
    
    flagA = True
    for i in arrayA :
        if i % gcdB == 0 :
            flagA = False
            break
    if flagA :
        answer = gcdB
        
    flagB = True
    for i in arrayB :
        if i % gcdA == 0 :
            flagB = False
            break
    if flagB :
        answer = max(gcdA,answer)
    
    return answer