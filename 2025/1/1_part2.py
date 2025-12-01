with open("1.txt", "r") as f:
  inp = [(rotation[0], int(rotation[1:])) for rotation in f.read().splitlines()]

res = 0
dial = 50

for direction, distance in inp:
  if direction == "L":
    for _ in range(distance):
      dial -= 1
      if dial == 0:
        res += 1
      if dial == -1:
        dial = 99
  else:
    for _ in range(distance):
      dial += 1
      if dial == 100:
        dial = 0
      if dial == 0:
        res += 1

print(res)
