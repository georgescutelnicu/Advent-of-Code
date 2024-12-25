with open("25.txt", "r") as f:
  inp = f.read().splitlines()

def get_heights(grid):
  heights = []
  for i in range(5):
    col_height = 0
    for j in range(7):
      if grid[j][i] == "#":
        col_height += 1
    heights.append(col_height)
  return heights

keys, locks, current = [], [], []
res = 0

for line in inp:
  if line == "":
    continue
  current.append(line)
  if len(current) == 7:
    if "#" in current[0]:
      locks.append(current)
    else:
      keys.append(current)
    current = []

for key in keys:
  key_height = get_heights(key)
  for lock in locks:
    lock_height = get_heights(lock)
    overlap = False
    for k, h in zip(key_height, lock_height):
      if (k + h) > 7:
        overlap = True
        break
    if not overlap:
      res += 1

print(res)
