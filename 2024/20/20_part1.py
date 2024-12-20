from collections import deque

with open("20.txt", "r") as f:
   grid = [list(line) for line in f.read().splitlines()]

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == "S":
      START = (r, c)
    if grid[r][c] == "E":
      END = (r, c)

def find_racetrack(grid):
  coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  q = deque([(START[0], START[1], 1)])
  seen = set(START)

  while q:
    r, c, s = q.popleft()
    for x, y in coords:
      _r, _c = r + x, c + y
      if (_r, _c) == END:
        return s
      if still_in_grid(_r, _c) and (_r, _c) not in seen and grid[_r][_c] != "#":
        q.append((_r, _c, s+1))
        seen.add((_r, _c))

default_picoseconds = find_racetrack(grid)
res = 0

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == "#":
      grid[r][c] = "."
      picoseconds = find_racetrack(grid)
      if (default_picoseconds - picoseconds) >= 100:  
        res += 1
      grid[r][c] = "#"
      count += 1

print(res)

# Since its a brute-force solution, it runs pretty slow (~5 minutes on my setup)
