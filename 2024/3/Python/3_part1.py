import re

with open("3.txt", "r") as f:
  inp = f.read()

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, inp)

res = 0

for m in matches:
  x = int(m.split(",")[0][4:])
  y = int(m.split(",")[1][:-1])
  res += x * y

print(res)
