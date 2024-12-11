from functools import lru_cache

with open("11.txt", "r") as f:
  inp = f.read()

stones = list(map(int, inp.split()))

@lru_cache(maxsize=None)
def count_stones(stone, iterations):
  if iterations == 0:
    return 1
  if stone == 0:
    return count_stones(1, iterations-1)
  elif len(str(stone)) % 2 == 0:
    mid = len(str(stone)) // 2
    return (count_stones(int(str(stone)[:mid]), iterations-1) + 
            count_stones(int(str(stone)[mid:]), iterations-1))
  else:
    return count_stones(stone*2024, iterations-1)

print(sum(count_stones(stone, 75) for stone in stones))
