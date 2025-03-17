def f(n,k):
    if n == 1 :
        return k if k <= 2 else k-1
    
    num_1 = 4 ** (n-1) 
    num = 5 ** (n-1)
    loc = k // num
    if k % num == 0 :
        loc -= 1
        
    if loc < 2 :
        return loc * num_1 + f(n-1,k - num * loc)
    elif loc == 2 :
        return 2 * num_1
    else :
        return (loc-1) * num_1 + f(n-1,k - num*loc)

def solution(n, l, r):
    return f(n,r) - f(n,l-1)