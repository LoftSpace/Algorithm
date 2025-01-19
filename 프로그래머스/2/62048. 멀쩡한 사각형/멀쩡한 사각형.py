import math
def solution(w,h):
    count = 0
    temp = 0
    box_w = w//math.gcd(w,h)
    box_h = h//math.gcd(w,h)
    box_num = w//box_w
  
    return w * h - (box_w + box_h - 1) * box_num
    
    