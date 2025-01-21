with open("4.txt", "r") as f:
  grid = f.read().splitlines()

res = 0
count = 0
coords = [(-1, 1), (1, 1),
         (-1, -1), (1, -1)]

def is_valid(r, c):
  return 0 <= _r < len(grid) and 0 <= _c < len(grid[0])

def check_diagonal(r, c):
  return ((grid[r+-1][c+1] != grid[r+1][c+-1]) and
         (grid[r+1][c+1] != grid[r+-1][c+-1]))

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == "A":
      for coord in coords:
        _r, _c = r + coord[0], c + coord[1]
        if is_valid(_r, _c) and (grid[_r][_c] == "M" or grid[_r][_c] == "S"):
          count += 1
    if count == 4 and check_diagonal(r, c):
      res += 1
    count = 0

print(res)
