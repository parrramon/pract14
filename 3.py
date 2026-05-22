n = int(input())
dictionary = {}

for i in range(n):
    w1, w2 = input().split()
    dictionary[w1] = w2
    dictionary[w2] = w1

word = input()
if word in dictionary:
    print(dictionary[word])
else:
    print(word)