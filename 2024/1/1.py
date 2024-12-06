with open("1.txt", "r") as f:
  inp = f.read().splitlines()

nums1 = sorted([int(num.split()[0]) for num in inp])
nums2 = sorted([int(num.split()[1]) for num in inp])

res1 = 0
res2 = 0

for i, j in zip(nums1, nums2):
  res1 += abs(i - j)

for num in nums1:
  count = nums2.count(num)
  res2 += num * count

print(res1)
print(res2)
