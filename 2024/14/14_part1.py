import re

with open("14.txt", "r") as f:
  inp = f.read()

positions = re.findall(r"-?\d+", inp)
W, H = 101, 103
H_MID, W_MID = H // 2, W // 2
robots = []
final_positions = []
q1, q2, q3, q4 = 0, 0, 0, 0

for i in range(0, len(positions), 4):
  robots.append(tuple(map(int, (positions[i], positions[i+1], 
                                positions[i+2], positions[i+3]))))

for robot in robots:
  c, r, y, x = robot
  r = (r + (x * 100)) % H 
  c = (c + (y * 100)) % W 
  final_positions.append((r, c))
  
for final_position in final_positions:
  r, c = final_position
  if r < H_MID and c < W_MID:
    q1 += 1
  if r < H_MID and c > W_MID:
    q2 += 1
  if r > H_MID and c < W_MID:
    q3 += 1
  if r > H_MID and c > W_MID:
    q4 += 1

safety_factor = q1 * q2 * q3 * q4
print(safety_factor)
