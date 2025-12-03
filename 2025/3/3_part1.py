with open("3.txt", "r") as f:
  inp = f.read().splitlines()

res = 0

for battery in inp:
  max_joltage = ""
  first_battery = 0
  second_battery = 0
  first_battery_idx = 0

  for i, b in enumerate(battery[:-1]):
    if int(b) > first_battery:
      first_battery = int(b)
      first_battery_idx = i
  max_joltage += str(first_battery)

  for b in battery[first_battery_idx+1:]:
    second_battery = max(second_battery, int(b))
  max_joltage += str(second_battery)
  
  res += int(max_joltage)

print(res)
