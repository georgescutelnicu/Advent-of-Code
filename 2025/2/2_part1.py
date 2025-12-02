with open("2.txt", "r") as f:
  inp = [tuple(map(int, part.split("-"))) for part in f.read().split(",")]

res = 0

for i1, i2 in inp:
  for n in range(i1, i2+1):
    sn = str(n)
    size = len(sn) // 2
    if sn[:size] == sn[size:]:
      res += n

print(res)
