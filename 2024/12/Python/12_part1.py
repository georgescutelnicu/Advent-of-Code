from collections import deque

with open("12.txt", "r") as f:
  grid = f.read().splitlines()

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
regions = []
seen = set()
res = 0

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if (r, c) not in seen:
      seen.add((r, c))
      q = deque([(r, c)])
      region = [(r, c)]
      while q:
        curr_r, curr_c = q.popleft()
        for x, y in coords:
          _r, _c, = curr_r + x, curr_c + y
          if (still_in_grid(_r, _c) and (_r, _c) not in region and
              grid[_r][_c] == grid[curr_r][curr_c]):
            region.append((_r, _c))
            q.append((_r, _c))
            seen.add((_r, _c))
      regions.append(region)

for region in regions:
  perimeter = 0
  for r, c in region:
    neighbors = 0
    for x, y in coords:
      _r, _c = r + x, c + y
      if (_r, _c) in region:
        neighbors += 1
    perimeter += 4 - neighbors
  res += perimeter * len(region)

print(res)
