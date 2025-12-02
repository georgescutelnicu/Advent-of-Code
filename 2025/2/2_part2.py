with open("2.txt", "r") as f:
  inp = [tuple(map(int, part.split("-"))) for part in f.read().split(",")]

def is_repeated(s):
  if len(s) == 1:
    return False
  if len(set(s)) == 1:
    return True
  size = len(s)
  for i in range(1, size//2+1):
    if size % i != 0:
      continue
    if s == s[:i] * (size//i):
      return True
  return False

res = 0

for i1, i2 in inp:
  for n in range(i1, i2+1):
    sn = str(n)
    if is_repeated(sn):
      res += n
      
print(res)
