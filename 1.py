text = input()

words = text.split()
unique = []

for w in words:
    if w not in unique:
        unique.append(w)

unique.sort(key=lambda x: words.count(x), reverse=True)

for w in unique:
    print(w, words.count(w))