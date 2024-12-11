with open("11.txt", "r") as f:
  inp = f.read()

stones = list(map(int, inp.split()))

for _ in range(25):
  temp = []
  for stone in stones:
    if stone == 0:
      temp.append(1)
    elif len(str(stone)) % 2 == 0:
      mid = len(str(stone)) // 2
      temp.append(int(str(stone)[:mid]))
      temp.append(int(str(stone)[mid:]))
    else:
      temp.append(stone*2024)
  stones = temp

print(len(stones))
