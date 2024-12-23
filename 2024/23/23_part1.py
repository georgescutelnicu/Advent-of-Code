with open("23.txt", "r") as f:
  inp = [tuple(conn.split("-")) for conn in f.read().splitlines()]

connections = {}
lan_connections = set()
res = 0

for conn1, conn2 in inp:
  if conn1 in connections:
    connections[conn1].append(conn2)
  else:
    connections[conn1] = [conn2]
  if conn2 in connections:
    connections[conn2].append(conn1)
  else:
    connections[conn2] = [conn1]

for i in connections:
  for j in connections[i]:
    for k in connections[j]:
      if i in connections[k]:
        lan_connection = tuple(sorted([i, j, k]))
        lan_connections.add(lan_connection)

for conn in lan_connections:
  for c in conn:
    if c.startswith("t"):
      res += 1
      break

print(res)
