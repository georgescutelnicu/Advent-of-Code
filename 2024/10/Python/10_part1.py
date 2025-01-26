from collections import deque

with open("10.txt", "r") as f:
  grid = f.read().splitlines()

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

starting_points = [(r, c) for r in range(len(grid)) for c in range(len(grid[0]))
                                                           if grid[r][c] == "0"]
coords = [(0, 1), (0, -1), (1, 0), (-1, 0)]
res = 0

for start in starting_points:
  start_r, start_c = start[0], start[1]
  q = deque([(start_r, start_c)])
  seen = set((start_r, start_c))

  while len(q) > 0:
    r, c = q.popleft()
    for x, y in coords:
      _r, _c, = r + x, c + y
      if still_in_grid(_r, _c) and (_r, _c) not in seen:
        if grid[_r][_c] == str(int(grid[r][c]) + 1):
          seen.add((_r, _c))
          if grid[_r][_c] == "9":
            res += 1
          else:
            q.append((_r, _c))

print(res)
