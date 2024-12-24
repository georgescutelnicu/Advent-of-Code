with open("24.txt", "r") as f:
  inp = f.read().splitlines()

values, operations = {}, {}
res = ""

is_op = False
for line in inp:
  if line == "":
    is_op = True
    continue
  if is_op:
    wire_1, op, wire_2, val = line.replace(" ->", "").split(" ")
    operations[val] = (wire_1, op, wire_2)
  else:
    wire, val = line.split(": ")
    values[wire] = int(val)

while len(operations) != 0:
  to_remove = []
  for k, v in operations.items():
    wire_1, op, wire_2 = v
    if wire_1 in values and wire_2 in values:
      to_remove.append(k)
      if op == "AND":
        values[k] = values[wire_1] and values[wire_2]
      elif op == "OR":
        values[k] = values[wire_1] or values[wire_2]
      else:
        values[k] = values[wire_1] ^ values[wire_2]    
  for item in to_remove:
    del operations[item]

for k, v in sorted(values.items()):
  if k.startswith("z"):
    res += str(v)

print(int(res[::-1], 2))
