with open("9.txt", "r") as f:
  inp = f.read().replace("\n", "")

def separate_blocks(inp):
  disk_map = []
  count = 0
  for idx, char in enumerate(inp):
    if idx % 2 == 0:
      disk_map += [count] * int(char)
      count += 1
    else:
      disk_map += ["."] * int(char)
  return disk_map

def move_blocks(inp):
  i, j = 0, len(inp) - 1
  while i < j:
    while inp[i] != ".":
      i += 1
    while inp[j] == ".":
      j -= 1
    inp[i], inp[j] = inp[j], inp[i]
  return [n for n in inp if n != "."]

def final_checksum(inp):
  return sum(idx * num for idx, num in enumerate(inp))

print(final_checksum(move_blocks(separate_blocks(inp))))
