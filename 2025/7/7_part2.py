from functools import cache

with open("7.txt", "r") as f:
  grid = f.read().splitlines()

def find_start(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "S":
        return (r, c)

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

@cache
def helper(r, c):
  if not still_in_grid(r, c):
    return 1
  if grid[r][c] != "^":
    return helper(r+1, c)
  else:
    return helper(r, c+1) + helper(r, c-1)

print(helper(*find_start(grid)))
