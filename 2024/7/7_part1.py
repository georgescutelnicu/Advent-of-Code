with open("7.txt", "r") as f:
  inp = f.read().splitlines()

def is_a_match(target, nums, total, idx):
  if idx == len(nums):
    return target == total

  return (is_a_match(target, nums, total + nums[idx], idx + 1) or
          is_a_match(target, nums, total * nums[idx], idx + 1))
 
targets = [int(equation.split(":")[0]) for equation in inp]
numbers = [list(map(int, equation.split(":")[1].split())) for equation in inp]

res = 0

for target, nums in zip(targets, numbers):
  if is_a_match(target, nums, nums[0], 1):
    res += target

print(res)
