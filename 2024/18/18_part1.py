from collections import deque

with open("18.txt", "r") as f:
  inp = [tuple(map(int, item.split(","))) for item in f.read().splitlines()]

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

grid_size = 70
grid = [["." for i in range(grid_size+1)] for j in range(grid_size+1)]
coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for x, y in inp[:1024]:
  grid[x][y] = "#"

q = deque([(0, 0, 0)])
seen = set((0, 0))
found = False
res = 0

while q and not found:
  r, c, cost = q.popleft() 
  for x, y in coords:
    _r, _c = r + x, c + y
    if still_in_grid(_r, _c) and grid[_r][_c] != "#" and (_r, _c) not in seen:
      if (_r, _c) == (grid_size, grid_size):
        res = cost + 1
        found = True
        break
      seen.add((_r, _c))
      q.append((_r, _c, cost+1))
  
print(res)
