with open("6.txt", "r") as f:
  grid = [list(line) for line in f.read().splitlines()]

def find_guard(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "^":
        return (r, c)

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

coords = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0
visited = set()
guard = find_guard(grid)

while True:
  visited.add(guard)
  r, c = guard[0], guard[1]
  _r, _c = r + coords[direction][0], c + coords[direction][1]

  if still_in_grid(_r, _c):
    while grid[_r][_c] == "#":
      direction = 0 if direction == 3 else direction + 1
      _r, _c = r + coords[direction][0], c + coords[direction][1]
    guard = (_r, _c)

  else:
    break 

print(len(visited))
