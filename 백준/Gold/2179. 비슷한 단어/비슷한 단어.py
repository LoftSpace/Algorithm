import sys
import copy
input = sys.stdin.readline

N = int(input())

dictionary = []
hash = dict()
def compare(word1,word2):
    min_length = min(len(word1),len(word2))
    score = 0
    for i in range(min_length):
        if word1[i] == word2[i] :
            score += 1
        else :
            return score
    return score

for i in range(N):
    word = input().strip()
    dictionary.append(word)
    hash[word] = i
words = copy.deepcopy(dictionary)
dictionary.sort()
#print(dictionary)
score = 0
# S, T, S 순서, T 순서
longest_prefix = dict()
for i in range(N - 1):
    cur_score = compare(dictionary[i],dictionary[i + 1])
  #  print(cur_score,dictionary[i],dictionary[i + 1])
  #  print(dictionary[i][:cur_score])
    if cur_score  == score :
        if dictionary[i][:cur_score] in longest_prefix :
            continue
        else :
            longest_prefix[dictionary[i][:cur_score]] = True
    elif cur_score > score :
      #  print(cur_score,score)
        longest_prefix.clear()
        longest_prefix[dictionary[i][:cur_score]] = True
        score = cur_score
count = 0
#print(longest_prefix)
for word in words :
    for prefix in longest_prefix :
        if prefix == word[:len(prefix)] :
            longest_prefix.clear()
            longest_prefix[prefix] = True
            print(word)
            count += 1
            break
    if count == 2 :
        break

