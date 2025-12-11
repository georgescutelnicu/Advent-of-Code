from functools import cache

with open("11.txt", "r") as f:
  inp = f.read().splitlines()

@cache
def helper(device, dac, fft):
  if device == "out" :
    if dac and fft:
      return 1
    return 0
  res = 0
  for out_device in d[device]:
    res += helper(out_device,
                  dac or out_device == "dac",
                  fft or out_device == "fft")
  return res

d = {}

for line in inp:
  k, v = line.split(":")
  v = v.split()
  d[k] = v

print(helper("svr", False, False))
