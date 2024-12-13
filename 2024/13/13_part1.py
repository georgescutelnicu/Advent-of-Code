# Should've used regex instead of extract_numbers func
with open("13.txt", "r") as f:
  inp = f.read()

def extract_numbers(inp):
  machines = inp.split("\n\n")
  numbers = []
  num = ""
  for machine in machines:
    machine_num = []
    for char in machine:
      if char.isdigit():
        num += char
      elif num:
        machine_num.append(int(num))
        num = ""
    if num:
      machine_num.append(int(num))
      num= ""
    numbers.append(machine_num)
  return numbers

numbers = extract_numbers(inp)
a_price = 3
b_price = 1
res = 0

for a_x, a_y, b_x, b_y, p_x, p_y in numbers:
  min_tokens = float("inf")
  for i in range(100):
    for j in range(100):
      if a_x * i + b_x * j == p_x and a_y * i + b_y * j == p_y:
        min_tokens = min(min_tokens, i * a_price + j * b_price)
  res += min_tokens if min_tokens != float("inf") else 0

print(res)
