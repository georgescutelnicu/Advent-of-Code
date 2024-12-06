with open("5.txt", "r") as f:
  inp = f.read().splitlines()

def is_correctly_ordered(update):
  ordered = True
  for idx, current_page in enumerate(update[:-1]):
    count = 0
    for next_page in update[idx+1:]:
      if next_page not in page_order[current_page]:
        ordered = False
      else:
        count += 1
  return ordered

def bubble_sort(update):
  for i in range(len(update) - 1, 0, -1):
    for j in range(i):
      current_page = update[j]
      next_page = update[j+1]
      if next_page not in page_order[current_page]:
        update[j], update[j+1] = update[j+1], update[j]

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
  if not is_correctly_ordered(update):
    bubble_sort(update)
    res += update[len(update) // 2]

print(res)
