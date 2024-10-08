import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

edges = []

total = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    total += cost
    edges.append((a, b, cost))

edges.sort(key=lambda x:x[2])

parent = [0] * n

for i in range(n):
    parent[i] = i

for edge in edges:
    a, b, cost = edge

    if find_parent(parent, a) != find_parent(parent, b):
        total-=cost
        union_parent(parent, a, b)

print(total)