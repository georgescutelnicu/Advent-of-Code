with open("5.txt", "r") as f:
  intervals, ingredients = f.read().strip().split("\n\n")

intervals = [tuple(map(int, interval.split("-"))) for 
             interval in intervals.splitlines()]
intervals.sort(key=lambda t: t[0])

interval_start, interval_end = intervals[0]
merged_intervals = []

for i1, i2 in intervals[1:]:
  if i1 <= interval_end:
    interval_end = max(interval_end, i2)
  else:
    merged_intervals.append((interval_start, interval_end))
    interval_start, interval_end = i1, i2

merged_intervals.append((interval_start, interval_end))
  
print(sum(j - i + 1 for i, j in merged_intervals))
