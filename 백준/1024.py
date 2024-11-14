import sys
input = sys.stdin.readline

# 입력
n, l = map(int, input().split())

# 탐색
for i in range(l, 101):
    ix = n - (i*(i+1)//2)
    if ix%i==0:
        x = ix//i
        if x+1>=0:
            print(*(i for i in range(x+1, x+i+1)))
            break
else:
    print(-1)