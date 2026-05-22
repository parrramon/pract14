n = int(input())
dictionary = {}

for i in range(n):
    line = input().split()
    quality = line[0]
    objects = line[1:]

    for object in objects:
        dictionary[object] = quality
        
word = input()
if word in dictionary:
    print(dictionary[word])
else:
    print(word)