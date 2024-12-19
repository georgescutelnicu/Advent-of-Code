with open("19.txt", "r") as f:
  inp = f.read().split("\n\n")
  patterns = inp[0].split(", ")
  designs = inp[1].strip().split("\n")

def count_different_ways(design, patterns, cache):
  if not design:
    return 1
  count = 0
  if design in cache:
    return cache[design]
  for pattern in patterns:
    if design.startswith(pattern):
        count += count_different_ways(design[len(pattern):], patterns, cache)        
  cache[design] = count
  return count

cache = {}
res = 0

for design in designs:
  res += count_different_ways(design, patterns, cache)

print(res)
