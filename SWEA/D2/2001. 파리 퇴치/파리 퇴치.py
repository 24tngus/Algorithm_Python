T = int(input())

for num in range(1, T+1):
    N, M = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max = 0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            sum = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum += arr[x][y]
                    
            if (sum > max):
                 max = sum
             
    print("#%d %d" %(num, max))