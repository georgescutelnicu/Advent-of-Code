with open("3.txt", "r") as f:
  inp = f.read().splitlines()

def calculate_joltage(s, k=12):
  stack = []

  for i, c in enumerate(s):
    while stack and stack[-1] < c and len(stack) - 1 + len(s) - i >= k:
      stack.pop()
    if len(stack) < k:
      stack.append(c)
  
  return "".join(stack)

res = 0

for battery in inp:
  res += int(calculate_joltage(battery))

print(res)
