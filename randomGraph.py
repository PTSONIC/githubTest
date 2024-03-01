import networkx as nx

G = nx.erdos_renyi_graph(7, 0.5)
nx.draw(G)
