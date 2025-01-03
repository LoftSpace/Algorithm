from collections import deque
import copy
register_count = 0
profit = 0
def solution(users, emoticons):
    sale_ratios = [10,20,30,40]
    numOfEmoticons = len(emoticons)
    #register_count = 0
    #profit = 0
    def bfs(start_sale_ratio):
        global register_count
        global profit
        queue = deque()
        queue.append([[start_sale_ratio],1])
        while queue:
            sale_list , count = queue.popleft()
            if count == numOfEmoticons :
                cost, register = calculate(sale_list)
                if register > register_count : 
                    register_count = register
                    profit = cost
                elif register == register_count :
                    if profit < cost :
                        profit = cost
            else :
                for ratio in sale_ratios :
                    new_sale_list = copy.deepcopy(sale_list)
                    new_sale_list.append(ratio)
                    queue.append([new_sale_list,count + 1])
           
    def calculate(sale_list):
        total_cost = 0
        total_register = 0
        for user in users :
            user_sale = user[0]
            cost = 0
            for i in range(numOfEmoticons) :
                # 유저 기준보다 더 많이 세일을 한다면
                if sale_list[i] >= user_sale :
                    # 구매
                    cost += (100 - sale_list[i]) * emoticons[i] / 100
            # 총 구매 비용이 기준 금액 이상이면 구독
            if cost >= user[1] :
                total_register += 1
            # 구독안함
            else :
                total_cost += cost
        return total_cost, total_register
    for i in sale_ratios :
        bfs(i)
    
            
    answer = [register_count,profit]
    return answer