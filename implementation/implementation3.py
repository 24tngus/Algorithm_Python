data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]

    if nrow > 1 and nrow <= 8 and ncol > 1 and ncol <= 8:
        result += 1

print(result)