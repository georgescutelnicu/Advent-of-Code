with open("4.txt", "r") as f:
  grid = f.read().splitlines()

res = 0
coords = [(-1, -1), (-1, 0), (1, -1),
         (0, -1),           (0, 1),
         (-1, 1), (1, 0), (1, 1)]

def is_valid(r, c):
  return 0 <= _r < len(grid) and 0 <= _c < len(grid[0])

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == "X":
      for coord in coords:
        _r, _c = r + coord[0], c + coord[1]
        if is_valid(_r, _c) and grid[_r][_c] == "M":
          _r, _c = _r + coord[0], _c + coord[1]
          if is_valid(_r, _c) and grid[_r][_c] == "A":
            _r, _c = _r + coord[0], _c + coord[1]
            if is_valid(_r, _c) and grid[_r][_c] == "S":
              res += 1

print(res)
