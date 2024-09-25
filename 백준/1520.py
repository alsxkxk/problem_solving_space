import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(y, x):
    if y==m-1 and x==n-1: ## 목표 위치에 도달하면
        return 1
    if dp[y][x]!=-1: ## 방문한 적이 있다면 그 위치에서의 dp값 리턴
        return dp[y][x]

    way = 0 # 현재 위치에서 목표 지점까지 도달할 수 있는 경우의 수
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<m and 0<=nx<n and arr[y][x]>arr[ny][nx]:
            way += dfs(ny, nx)
    dp[y][x] = way
    return dp[y][x]


m, n = map(int, input().split())

arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

dp = [[-1] * n for _ in range(m)]
result = dfs(0, 0)
for i in dp:
    print(i)
# print(dfs(0,0))