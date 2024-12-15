with open("15.txt", "r") as f:
  inp = f.read().split("\n\n")
  grid = [list(row) for row in inp[0].split("\n")]
  directions = "".join(inp[1].split("\n"))

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == "@":
      robot = (r, c)

coords = {"^": (-1, 0),
          ">": (0, 1),
          "v": (1, 0),
          "<": (0, -1)}

for direction in directions:
  r, c = robot
  x, y = coords[direction]
  move_list = [(r, c)]
  while True:
    r, c = r + x, c + y
    if grid[r][c] == "O":
      move_list.append((r, c))
    else:
      move_list.append((r, c))
      break
  last_move_r, last_move_c = move_list[-1]
  if grid[last_move_r][last_move_c] != "#":
    robot = move_list[1]
    for i in range(len(move_list)-1, 0, -1):
      curr_r, curr_c = move_list[i]
      prev_r, prev_c = move_list[i - 1]
      grid[curr_r][curr_c], grid[prev_r][prev_c] = grid[prev_r][prev_c], grid[curr_r][curr_c]
     
res = 0
for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == "O":
      res += 100 * r + c
print(res)
