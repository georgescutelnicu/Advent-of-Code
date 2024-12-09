# Im not touching this ever again
with open("9.txt", "r") as f:
  inp = f.read().replace("\n", "")

def separate_blocks(inp):
  disk_map = []
  count = 0
  for idx, char in enumerate(inp):
    if idx % 2 == 0:
      disk_map += [[count] * int(char)]
      count += 1
    else:
      disk_map += [["."] * int(char)]
  return [l for l in disk_map if len(l) != 0]

def move_blocks(inp):
  i = 0
  while i < len(inp) - 1:
    if "." not in inp[i]:
      i += 1
    else:
      for j in range(len(inp) - 1, i, -1):
        if "." not in inp[j] and len(inp[i]) >= len(inp[j]):
          temp = inp[j].copy()
          for k in range(len(inp[j])):
            inp[i].pop()
            inp[j][k] = "."
          if len(inp[i]) == 0:
            inp.pop(i)
          inp.insert(i, temp)
          break
      i += 1
  return [char for l in inp for char in l]

def final_checksum(inp):
  return sum(idx * num for idx, num in enumerate(inp) if num != ".")

print(final_checksum(move_blocks(separate_blocks(inp))))
