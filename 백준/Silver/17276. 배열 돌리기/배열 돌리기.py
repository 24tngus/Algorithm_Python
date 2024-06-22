T = int(input())

for i in range(T):
    N, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            result[i][j] = arr[i][j]

    if r < 0:
        r = 360 + r
# [i][j]    [i][N//2]    [i][N-j]
# [N//2][j] [N//2][N//2] [N//2][N-j] 
# [N-i][j]  [N-i][N//2]  [N-i][N-j]
# (0,0) (0,1) (0,2)    (1,0) (0,0) (0,1)
# (1,0) (1,1) (1,2) -> (2,0) (1,1) (0,2)
# (2,0) (2,1) (2,2)    (2,1) (2,2) (1,2)
    if r == 360 or r == 0:
        for i in range(N):
            for j in range(N):
                print(result[i][j], end = " ")
            print()
    else:
        for _ in range(r // 45):
            for i in range(N):
                for j in range(N):
                    # X자
                    if i == j:
                        result[i][j] = arr[N//2][j]
                    elif i == N-j-1:
                        result[i][j] = arr[i][N//2]
                    # +자
                    elif i == N // 2:
                        result[i][j] = arr[N-j-1][j]
                    elif j == N // 2:
                        result[i][j] = arr[i][i]
                    
            for i in range(N):
                for j in range(N):
                    arr[i][j] = result[i][j]

        for i in range(N):
            for j in range(N):
                print(result[i][j], end = " ")
            print()
