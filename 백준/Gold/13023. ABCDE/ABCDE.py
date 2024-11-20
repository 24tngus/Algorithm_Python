import sys

N, M = map(int, sys.stdin.readline().strip().split())

result = 0
arr = [[] for _ in range(N)]
visit = [0] * (N)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start, cnt):
    global result

    cnt += 1
    visit[start] = 1

    if cnt == 5:
        result = 1
        return
    
    for i in arr[start]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i, cnt)

    visit[start] = 0

for i in range(N):
    if result == 1:
        break
    dfs(i, 0)

print(result)
