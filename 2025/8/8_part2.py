import networkx as nx

with open("8.txt", "r") as f:
  inp = [list(map(int, box.split(","))) for box in f.read().splitlines()]

distances = []

for i in range(len(inp)-1):
  for j in range(i+1, len(inp)):
    (x1, y1, z1), (x2, y2, z2) = inp[i], inp[j]
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
    distances.append((dist, i, j))

distances.sort(key=lambda x: x[0])

G = nx.Graph()
G.add_nodes_from(range(len(inp)))

for _, i, j in distances:
  G.add_edge(i, j)
  last_pair = (i, j)
  if nx.number_connected_components(G) == 1:
    break

print(inp[last_pair[0]][0] * inp[last_pair[1]][0])
