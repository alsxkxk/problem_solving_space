import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if graph[1][k] == INF or graph[k][x] == INF:
    print('INF')
else:
    print(graph[1][k]+graph[k][x])