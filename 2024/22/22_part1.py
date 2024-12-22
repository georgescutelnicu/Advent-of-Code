with open("22.txt", "r") as f:
  inp = list(map(int, f.read().splitlines()))

res = 0

for num in inp:
  for _ in range(2000):
    num = (((num * 64) ^ num) % 16777216)
    num = (((num // 32) ^ num) % 16777216)
    num = (((num * 2048) ^ num) % 16777216)
  res += num

print(res)
