from collections import deque 

with open("7.txt", "r") as f:
  grid = f.read().splitlines()

def find_start(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "S":
        return (r, c)

def still_in_grid(r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

res = 0 
q = deque([find_start(grid)])
seen = set()

while q:
  for _ in range(len(q)):
    r, c = q.popleft()
    r += 1
    if still_in_grid(r, c):
      if grid[r][c] == ".":
        q.append((r, c))
      else:
        split = False
        if still_in_grid(r, c+1) and (r, c+1) not in seen:
          q.append((r, c+1))
          seen.add((r, c+1))
          split = True
        if still_in_grid(r, c-1) and (r, c-1) not in seen:
          q.append((r, c-1))
          seen.add((r, c-1))
          split = True
        if split: res += 1

print(res)
