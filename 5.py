n = int(input())
tree = {}

for i in range(n):
    parent, child = input().split()
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

def count_descendants(name):
    if name not in tree:
        return 0
    count = 0

    for child in tree[name]:
        count += 1 + count_descendants(child)
    return count

person_name = input()
print(count_descendants(person_name))