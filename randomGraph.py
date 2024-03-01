import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import distance

# Create Graph
G = nx.erdos_renyi_graph(7, 0.5)

# Calculate node positions using spring layout
pos = nx.spring_layout(G) 

# Add weights based on Euclidean distance
for edge in G.edges():
    source_pos = pos[edge[0]]
    target_pos = pos[edge[1]]
    dist = distance.euclidean(source_pos, target_pos)
    G[edge[0]][edge[1]]['weight'] = round(dist, 2)

# Display Graph
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()





