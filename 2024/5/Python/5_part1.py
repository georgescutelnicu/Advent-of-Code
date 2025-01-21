with open("5.txt", "r") as f:
  inp = f.read().splitlines()

def is_correctly_ordered(update):
  ordered = True
  for idx, current_page in enumerate(update[:-1]):
    for next_page in update[idx+1:]:
      if next_page not in page_order[current_page]:
        ordered = False
  return ordered

res = 0
updates = [list(map(int, item.split(','))) for item in inp if ',' in item]
page_order = {}

for item in inp:
  if "|" in item:
    k, v = item.split("|")
    if int(k) in page_order:
      page_order[int(k)].append(int(v))
    else:
      page_order[int(k)] = [int(v)]

for update in updates:
  if is_correctly_ordered(update):
    res += update[len(update) // 2]

print(res)
