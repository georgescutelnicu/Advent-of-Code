with open("9.txt", "r") as f:
  inp = [tuple(map(int, coord.split(","))) for coord in f.read().splitlines()]

inp.sort(key=lambda x: (x[1], x[0]))

res = 0

for i in range(len(inp)-1):
  x1, y1 = inp[i]
  for j in range(i+1, len(inp)):
    x2, y2 = inp[j]
    x_area = x2 - x1 + 1
    y_area = abs(y2 - y1) + 1
    res = max(res, x_area * y_area)

print(res)
