import re

with open("14.txt", "r") as f:
  inp = f.read()

def check_diagonal(grid, diagonal_size):
  for r in range(len(grid) - diagonal_size):
    for c in range(len(grid[0]) - diagonal_size):
      if all(grid[r + i][c + i] == "@" for i in range(diagonal_size)):
        return True
  return False

positions = re.findall(r"-?\d+", inp)
W, H = 101, 103
robots = []

for i in range(0, len(positions), 4):
  robots.append(tuple(map(int, (positions[i], positions[i+1], 
                                positions[i+2], positions[i+3]))))

count = 0
while True:
  count += 1
  final_positions = []
  for idx, robot in enumerate(robots):
    c, r, y, x = robot
    r = (r + x) % H 
    c = (c + y) % W 
    final_positions.append((r, c))
    robots[idx] = (c, r, y, x)
  grid = [["." for _ in range(W)] for _ in range(H)]
  for r, c in final_positions:
    grid[r][c] = "@"
  if check_diagonal(grid, 13):
    break

print(count)
