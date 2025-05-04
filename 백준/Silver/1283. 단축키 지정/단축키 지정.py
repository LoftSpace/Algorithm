N = int(input())


options = []
for i in range(N):
    options.append(input().split(' '))

hash = dict()

def check_word(option):
    for index,word in enumerate(option) :
        #해당 단어의 첫글자를 단축키로 사용 가능
        if word[0] not in hash :
            hash[word[0].upper()] = True
            hash[word[0].lower()] = True
            word = '[' + word[0] + ']' + word[1:]
            #print(word)
            option[index] = word
            return True
    return False

def check_alphabet(option):
    for j,word in enumerate(option):
        for index,alphabet in enumerate(word) :
            if alphabet not in hash :
                hash[alphabet.upper()] = True
                hash[alphabet.lower()] = True
                word = word[:index] + '[' + word[index] + ']' + word[index + 1:]
                option[j] = word
                return True
    return False
#각 옵션
for option in options :
    #각 옵션의 각 단어
    if not check_word(option):
        check_alphabet(option)

for ans in options :
    print(' '.join(ans))