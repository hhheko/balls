n, m = list(map(int, input().split()))
matrix = []
way = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
data = [[0 for i in range(m)] for i in range(n)]
data[0][0] = matrix[0][0]
for i in range(1, m):
    data[0][i] = matrix[0][i] +  data[0][i - 1]
for i in range(1, n):
    data[i][0] = matrix[i][0] + data[i - 1][0]
for i in range(1, n):
    for j in range(1, m):
        data[i][j] = matrix[i][j] + max(data[i][j - 1], data[i - 1][j])
y = n - 1
x = m - 1
while x != 0 or y != 0:
    if (x - 1) > -1 and (y - 1) > -1:
        if data[y][x - 1] >= data[y - 1][x]:
            way.append('R')
            x -= 1
        else:
            way.append('D')
            y -= 1
    elif y - 1 <= -1:
        way.append('R')
        x -= 1
    elif x - 1 <= -1:
        way.append('D')
        y -= 1
print(data[-1][-1])
if way:
    print(*(way[::-1]))
