n = int(input())
dictionary = {}

for i in range(n):
    line = input().split()
    quality = line[0]
    objects = line[1:]

    for obj in objects:
        dictionary[obj] = quality
        
word = input()
if word in dictionary:
    print(dictionary[word])
else:
    print(word)
