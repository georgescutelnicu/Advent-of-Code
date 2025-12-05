with open("5.txt", "r") as f:
  intervals, ingredients = f.read().strip().split("\n\n")

intervals = [tuple(map(int, interval.split("-"))) for 
             interval in intervals.splitlines()]
intervals.sort(key=lambda t: t[0])
ingredients = list(map(int, ingredients.splitlines()))

res = 0

for ing in ingredients:
  for i1, i2 in intervals:
    if ing < i1:
      break
    if i1 <= ing <= i2:
      res += 1
      break
  
print(res)
