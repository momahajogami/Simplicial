import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([("a","b"),("c","d")])
nx.draw(G)
plt.savefig("path.png")




