from collections import deque
def solution(begin, target, words):
    def find_next_word(current_word,word_set):
        next_word_list = []
        for word in word_set :
            differents = 0
            for i in range(len(current_word)) :
                if word[i] != current_word[i] :
                    differents += 1
            if differents == 1 :
                next_word_list.append(word)
        return next_word_list
    queue = deque([])
    word_set = set()
    for word in words : 
        word_set.add(word)
    queue.append([begin,word_set.copy(),0])
    while queue :
        current_word, word_set, count = queue.popleft()
        if current_word == target :
            return count
        next_word_list = find_next_word(current_word,word_set)
        if next_word_list : 
            for next_word in next_word_list:
                new_word_set = word_set.copy()
                new_word_set.remove(next_word)
                queue.append([next_word,new_word_set,count + 1])
        
    answer = 0
    return answer