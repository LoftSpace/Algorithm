from collections import deque
def solution(coin, cards):   
    N = len(cards)
    target = N + 1
    rounds = 1
    my_cards = cards[:N//3]
    my_cards = set(my_cards)
    past_cards = set()
    cards = deque(cards[N//3:])

    def match_with_my_cards():
        for my_card in list(my_cards) :
            if (target - my_card) in list(past_cards) :
                past_cards.remove(target - my_card)
                my_cards.remove(my_card)
                return True
        return False
    
    def match_in_past():
        for past_card in list(past_cards) :
            if (target - past_card) in list(past_cards) :
                past_cards.remove(past_card)
                past_cards.remove(target - past_card)
                return True
        return False
    
    def match_in_my_cards():
        for i in list(my_cards) :
            if (target - i) in list(my_cards) :
                my_cards.remove(i)
                my_cards.remove(target - i)
                return True
        return False
                
    #코인을 다 쓰거나 더이상 뽑을 카드가 없다면 종료
    while coin >= 0 and cards :
        past_cards.add(cards.popleft())
        past_cards.add(cards.popleft())
        #내 카드 중에서 짝을 이루면
        if match_in_my_cards():
            pass
        #이미 갖고 있는것과 짝을 이루면
        elif coin >= 1 and match_with_my_cards():
            coin -=1
        #이전에 봤던것들 끼리 짝을 이뤄야 한다면
        elif coin >= 2 and match_in_past():
            coin -= 2
        else :
            break
        rounds += 1
        
    answer = rounds
    return answer