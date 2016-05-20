# compute the simplicial homology of a sphere.
import networkx as nx
import matplotlib.pyplot as plt
def finOrdCompose(f,g):
    pass
G = nx.DiGraph()
n=s=e=w= 3
nw=ne=se=sw = 2
G.add_edge("nw","n",f=[1,2])
G.add_edge("nw","w",f=[1,2])
G.add_edge("sw","s",f=[0,1])
G.add_edge("sw","w",f=[0,1])
G.add_edge("se","s",f=[1,2])
G.add_edge("se","e",f=[1,2])
G.add_edge("ne","n",f=[0,1])
G.add_edge("ne","e",f=[0,1])

nx.draw(G)
plt.savefig("sphere.png")




