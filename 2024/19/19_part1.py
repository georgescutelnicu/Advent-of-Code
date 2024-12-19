with open("19.txt", "r") as f:
  inp = f.read().split("\n\n")
  patterns = inp[0].split(", ")
  designs = inp[1].strip().split("\n")

def can_be_designed(design, patterns, cache):
  if not design:
    return True
  if design in cache:
    return cache[design]
  for pattern in patterns:
    if design.startswith(pattern):
      if can_be_designed(design[len(pattern):], patterns, cache):
        cache[design] = True
        return True
  cache[design] = False
  return False

cache = {}
res = 0

for design in designs:
  if can_be_designed(design, patterns, cache):
    res += 1

print(res)
