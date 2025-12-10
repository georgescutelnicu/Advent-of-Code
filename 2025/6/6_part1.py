from math import prod

with open("6.txt", "r") as f:
  inp = list(zip(*[line.strip().split() for line in f]))

res = 0

for line in inp:
  if line[-1] == "*":
    total = prod(int(n) for n in line[:-1])
  else:
    total = sum(int(n) for n in line[:-1])
  res += total

print(res)
