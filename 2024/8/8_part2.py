with open("8.txt", "r") as f:
  grid = f.read().splitlines()

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def antinode_offset(r_1, r_2, c_1, c_2):
  r_diff = abs(r_1 - r_2)
  c_diff = abs(c_1 - c_2)

  if r_1 < r_2:
    r_an = r_1 - r_diff
  else:
    r_an = r_1 + r_diff

  if c_1 < c_2:
    c_an = c_1 - c_diff
  else:
    c_an = c_1 + c_diff

  return (r_an, c_an)

antennas = {}
antinodes = set()

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] != ".":
      antinodes.add((r, c))
      if grid[r][c] not in antennas:
        antennas[grid[r][c]] = [(r, c)]
      else:
        antennas[grid[r][c]].append((r, c))

for antena, location in antennas.items():
  location_len = len(location)
  for i in range(location_len):
    for j in range(location_len):
      if i == j:
        continue

      r_1 = location[i][0]
      c_1 = location[i][1]
      r_2 = location[j][0]
      c_2 = location[j][1]

      r_an, c_an = antinode_offset(r_1, r_2, c_1, c_2)

      while still_in_grid(r_an, c_an):
        antinodes.add((r_an, c_an))
        r_2, c_2 = r_1, c_1
        r_1, c_1 = r_an, c_an
        r_an, c_an = antinode_offset(r_1, r_2, c_1, c_2)

print(len(antinodes))
