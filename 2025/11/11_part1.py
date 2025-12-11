with open("11.txt", "r") as f:
  inp = f.read().splitlines()

def helper(device):
  if device == "out":
    return 1
  res = 0
  for out_device in d[device]:
    res += helper(out_device)
  return res

d = {}

for line in inp:
  k, v = line.split(":")
  v = v.split()
  d[k] = v

print(helper("you"))
