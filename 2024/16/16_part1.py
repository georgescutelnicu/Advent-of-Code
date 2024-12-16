import heapq

with open("16.txt", "r") as f:
  grid = f.read().splitlines()

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == "S":
      start = (r, c)
    if grid[r][c] == "E":
      end = (r, c)

coords = {"horizontal": [(0, -1), (0, 1)],
          "vertical": [(-1, 0), (1, 0)]} 

q = [(0, start, coords["horizontal"][1])] 
seen = set()

while q:
  cost, current_position, current_direction = heapq.heappop(q)
  r, c = current_position                       
  x, y = current_direction
  seen.add((current_position, current_direction))

  if (r, c) == end:
    res = cost
    break

  paths = []
  if (x, y) in coords["horizontal"]:  
    for coord in coords["vertical"]:
      _x, _y = coord
      paths.append((cost + 1001, (r + _x, c + _y), coord))
    for coord in coords["horizontal"]:
      _x, _y = coord
      if (x, y) == coord:
        paths.append((cost + 1, (r + _x, c + _y), coord))
  else:
    for coord in coords["horizontal"]:
      _x, _y = coord
      paths.append((cost + 1001, (r + _x, c + _y), coord))
    for coord in coords["vertical"]:
      _x, _y = coord
      if (x, y) == coord:
        paths.append((cost + 1, (r + _x, c + _y), coord))

  for _cost, _current_position, _current_direction in paths:
    _r, _c = _current_position
    if (grid[_r][_c] != "#" and 
     (_current_position, _current_direction) not in seen):
      heapq.heappush(q, (_cost, _current_position, _current_direction))

print(res)

# The reason i add 1001 instead of 1000 is because when i change direction
# i'm also moving one step forward in that new direction
