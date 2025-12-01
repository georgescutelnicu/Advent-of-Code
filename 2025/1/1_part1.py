with open("1.txt", "r") as f:
  inp = [(rotation[0], int(rotation[1:])) for rotation in f.read().splitlines()]

res = 0
dial = 50

for direction, distance in inp:
  if direction == "L":
    dial = (dial - distance) % 100
  else:
    dial = (dial + distance) % 100
  if dial == 0:
    res += 1

print(res)
