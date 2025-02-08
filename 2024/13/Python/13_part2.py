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
offset = 10000000000000
a_price = 3
b_price = 1
res = 0

for a_x, a_y, b_x, b_y, p_x, p_y in numbers:
  p_x, p_y = p_x + offset, p_y + offset
  a_count = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
  b_count = (p_x - a_x * a_count) / b_x
  if a_count == int(a_count) and b_count == int(b_count):
    res += a_count * a_price + b_count * b_price

print(int(res))

# Equations to get a_count and b_count
# a_x * a_count + b_x * b_count = p_x
# a_y * a_count + b_y * b_count = p_y

# Multiply first eq by b_y and second by b_x so we can simplify later
# a_x * b_y * a_count + b_x * b_y * b_count = p_x * b_y
# a_y * b_x * a_count + b_y * b_x * b_count = p_y * b_x

# Substract the equations
# (a_x * b_y * a_count + b_x * b_y * b_count) - 
# (a_y * b_x * a_count + b_y * b_x * b_count) = p_x * b_y - p_y * b_x

# Simplify by b_x * b_y * b_count
# a_x * b_y * a_count - a_y * b_x * a_count = p_x * b_y - p_y * b_x

# Multiply by the common term
# (a_x * b_y - a_y * b_x) * a_count = p_x * b_y - p_y * b_x

# Get a_count
# a_count =  (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)

# Get b_count from the first equation (a_x * a_count + b_x * b_count = p_x)
# b_count = (p_x - a_x * a_count) / b_x
