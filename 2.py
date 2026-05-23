n = int(input())
dictionary = {}
for i in range(n):
    ru_word, en_word = input().split()
    dictionary[ru_word] = en_word

phrase = input().split()
result = []
for word in phrase:
    if word in dictionary:
        result.append(dictionary[word])
    else:
        result.append(word)

print(' '.join(result))
