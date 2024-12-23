import networkx as nx

with open("23.txt", "r") as f:
  inp = [tuple(conn.split("-")) for conn in f.read().splitlines()]

G = nx.Graph()
G.add_edges_from(inp)

cliques = list(nx.find_cliques(G))
largest_clique = max(cliques, key=len)

print(",".join(sorted(largest_clique)))
