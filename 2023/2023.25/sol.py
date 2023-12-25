#!/usr/bin/env python3

import sys, pprint, math, networkx as nx

data = [ s.strip().split() for s in open(sys.argv[1]) ]

G = nx.Graph()
for v in data:
    v[0] = v[0].strip(':')
    for w in v[1:]: G.add_edge(v[0], w)


G.remove_edges_from(nx.minimum_edge_cut(G))

print(math.prod([len(c) for c in nx.connected_components(G)]))

# for i in range(1,5): print(f"can disconnect by removing {i-1} edges?", not nx.is_k_edge_connected(G, i))

# res = [len(s) for s in list(nx.k_edge_components(G, 4))]
# print("Part 1:", math.prod(res))

# for v in G: print(v,"-- {",' '.join([w for w in G[v]]),"}")