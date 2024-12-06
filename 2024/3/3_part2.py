import re

with open("3.txt", "r") as f:
  inp = f.read()

pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
matches = re.findall(pattern, inp)

res = 0
is_enabled = True

for m in matches:
  if m == "don't()":
    is_enabled = False
  elif m == "do()":
    is_enabled = True
  elif is_enabled: 
    x = int(m.split(",")[0][4:])
    y = int(m.split(",")[1][:-1])
    res += x * y

print(res)
