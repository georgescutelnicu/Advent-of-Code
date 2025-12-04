with open("4.txt", "r") as f:
  grid = [list(line.strip()) for line in f]

res = 0
removed = True
coords = [(-1, -1), (-1, 0), (1, -1),
         (0, -1),           (0, 1),
         (-1, 1), (1, 0), (1, 1)]

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

while removed:
  removed = False
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "@":
        rolls_of_paper = 0
        for x, y in coords:
          _r, _c = x + r, y + c
          if still_in_grid(_r, _c) and grid[_r][_c] == "@":
            rolls_of_paper += 1
        if rolls_of_paper < 4:
          grid[r][c] = "."
          removed = True
          res += 1
  
print(res)
