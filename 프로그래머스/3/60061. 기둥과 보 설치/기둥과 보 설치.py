from copy import deepcopy
def able0(x,y,lst):
    if y == 0 :
        return True
    elif ([x-1,y,1] in lst) or ([x,y,1] in lst):
        return True
    elif [x,y-1,0] in lst :
        return True
    else :
        return False
def able1(x,y,lst):
    if ([x,y-1,0] in lst) or ([x + 1,y - 1, 0] in lst):
        return True
    elif ([x-1,y,1] in lst) and ([x + 1,y,1] in lst):
        return True
    else :
        return False
def del0(x,y,lst):
    nlst = deepcopy(lst)
    nlst.remove([x,y,0])
    #위에 기둥이 있을 때 확인
    if ([x,y+1,0] in nlst) and not able0(x,y+1,nlst):
        return False
    #위에 보가 있을 때 확인
    elif ([x,y+1,1] in nlst) and not able1(x,y+1,nlst):
        return False
    #위 옆에 보가 있을 때 확인
    elif ([x-1,y+1,1] in nlst) and not able1(x-1,y+1,nlst):
        return False
    else:
        return True
def del1(x,y,lst):
    nlst = deepcopy(lst)
    nlst.remove([x,y,1])
    #이 위치에 기둥이 있을 때 확인
    if [x,y,0] in nlst and not able0(x,y,nlst):
        return False
    #오른쪽에 기둥이 있을 때
    if [x+1,y,0] in nlst and not able0(x+1,y,nlst):
        return False
    #왼쪽에 보 있을 때 확인
    elif [x-1,y,1] in nlst and not able1(x-1,y,nlst):
        return False
    #오른쪽에 보 있을 때 확인
    elif [x+1,y,1] in nlst and not able1(x+1,y,nlst):
        return False
    else:
        return True
def solution(n, build_frame):
    answer = []
    for x,y,k,ox in build_frame:
        if k == 0 and ox == 1 and able0(x,y,answer):
            answer.append([x,y,0])
        elif k == 0 and ox == 0 and del0(x,y,answer):
            answer.remove([x,y,0])
        elif k == 1 and ox == 1 and able1(x,y,answer):
            answer.append([x,y,1])
        elif k == 1 and ox == 0 and del1(x,y,answer):
            answer.remove([x,y,1])
    answer.sort()
    return answer