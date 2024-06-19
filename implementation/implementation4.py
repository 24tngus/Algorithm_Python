n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())

# 현재 위치 방문
d[x][y] = 1

# 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시작
count = 1
turn = 0

while True:
    left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동 
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 
    else :
        turn += 1
    # 네 방향 모두 갈 수 없는 경우 
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 없을 경우 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우 
        else: 
            break
        turn = 0

print(count)
