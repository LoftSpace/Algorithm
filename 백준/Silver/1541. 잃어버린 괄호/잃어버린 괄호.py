import sys

input = sys.stdin.readline

eq = input().split()[0]

tokens = []

words = ''
for word in eq:
    if word != '+' and word != '-' :
        words += word
    else :
        tokens.append(int(words))
        tokens.append(word)
        words = ''
tokens.append(int(words))
#print(tokens)
num1 = 0
num2 = 0
foundMinus = False
token = 0
while token < len(tokens) :
    if token % 2 == 0 :
        num1 += tokens[token]
    else :
        if tokens[token] == '-' :
            while token < len(tokens) :
                if token % 2 == 0 :
                    num2 += tokens[token]
                token += 1
    token += 1

print(num1 - num2)