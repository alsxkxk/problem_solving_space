import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.insert(0, 0)

if n==1:
    print(p[1])
else:
    dp = [0] * (n+1)
    dp[1] = p[1]
    for i in range(2, n+1):
        temp = []
        for j in range(1,i):
            temp.append(dp[j]*(i//j)+dp[i%j])
        t_min = min(temp)
        dp[i] = min(t_min, p[i])
    print(dp[n])