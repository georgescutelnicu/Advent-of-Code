def is_safe(l):
  if l[0] < l[1]:
    for i in range(1, len(l)):
      if (l[i] - l[i-1] < 1) or (l[i] - l[i-1] > 3):
        return False
  else:
    for i in range(1, len(l)):
      if (l[i-1] - l[i] < 1) or (l[i-1] - l[i] > 3):
        return False
  return True


with open("2.txt", "r") as f:
  reports = f.read().splitlines()
  reports = [list(map(int, report.split())) for report in reports]

safe_reports = 0
safe_reports_2 = 0

for report in reports:
  if is_safe(report):
    safe_reports += 1

for report in reports:
  for i in range(len(report)):
    if is_safe(report[:i] + report[i+1:]):
      safe_reports_2 += 1
      break

print(safe_reports)
print(safe_reports_2)
