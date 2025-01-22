with open("6.txt", "r") as f:
  grid = [list(line) for line in f.read().splitlines()]

def find_guard(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "^":
        return (r, c)

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def is_a_loop(grid, guard):
  coords = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  direction = 0
  visited = set()

  while True:
    visited.add((guard[0], guard[1], coords[direction][0], coords[direction][1]))
    r, c = guard[0], guard[1]
    _r, _c = r + coords[direction][0], c + coords[direction][1]

    if still_in_grid(_r, _c):
      while grid[_r][_c] == "#":
        direction = 0 if direction == 3 else direction + 1
        _r, _c = r + coords[direction][0], c + coords[direction][1]

      guard = (_r, _c)

      if (guard[0], guard[1], coords[direction][0], coords[direction][1]) in visited:
        return True

    else:
      return False 

guard = find_guard(grid)
loops = 0

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == ".":
      grid[r][c] = "#"
      if is_a_loop(grid, guard):
        loops += 1
      grid[r][c] = "."

print(loops)
