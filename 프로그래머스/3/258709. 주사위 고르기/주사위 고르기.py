from itertools import combinations, product
from bisect import bisect_left
def solution(dice):
    answer = []
    
    N = len(dice)
    total_games = 6 ** N
    a_dices_index = combinations(range(N),N//2)
 
    for a_dice_index in a_dices_index :
        b_dice_index = [i for i in range(N) if i not in a_dice_index]
        A = []
        B = []
        for each_dice_element_index_set in product(range(6),repeat = N // 2):
            sum = 0
            for dice_num,each_dice_element_index in enumerate(each_dice_element_index_set):
                sum += dice[a_dice_index[dice_num]][each_dice_element_index]
            A.append(sum)
        
        for each_dice_element_index_set in product(range(6),repeat = N // 2):
            sum = 0
            for dice_num,each_dice_element_index in enumerate(each_dice_element_index_set):
                sum += dice[b_dice_index[dice_num]][each_dice_element_index]
            B.append(sum)
        B.sort()
        wins = 0
        for num in A :
            wins += bisect_left(B,num)
        answer.append([wins,a_dice_index])
    answer.sort(key = lambda x : (x[0]),reverse = True)
    print(answer)
    answer = answer[0][1]
    ans = list(answer)
    for i in range(len(answer)):
        ans[i] += 1
    return ans
