
with open("12.txt", "r") as f:
  inp = f.read().strip().split("\n\n")[-1].split("\n")

presents = [tuple(map(int, i.split(":")[1].split())) for i in inp]
regions = [tuple(map(int, i.split(":")[0].split("x"))) for i in inp]

print(sum(1 for p, (x, y) in zip(presents, regions) if 
          (x // 3) * (y // 3) >= sum(p)))
