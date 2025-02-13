def solution(sequence):
    n = len(sequence)
    psum = [0] * (n+1)
    for i in range(n):
        psum[i + 1] = psum[i] + sequence[i] * (-1) ** i
        
    answer = max(psum) - min(psum)
    return answer