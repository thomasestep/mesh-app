import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

nodes = [
    (0.00, 0.00), (1.00, 0.00), (2.00, 0.00),
    (0.00, 1.00), (1.00, 1.00), (2.00, 1.00),
    (0.00, 2.00), (1.00, 2.00), (2.00, 2.00)
]

for i, n in enumerate(nodes):
    g.add_node(i+1)
    g.node[i+1]['XY'] = n

#1
g.add_edge(1, 5)
g.add_edge(5, 4)
g.add_edge(4, 1)
#2
g.add_edge(1, 2)
g.add_edge(2, 5)
g.add_edge(5, 1)
#3
g.add_edge(2, 6)
g.add_edge(6, 5)
g.add_edge(5, 2)
#4
g.add_edge(2, 3)
g.add_edge(3, 6)
g.add_edge(6, 2)
#5
g.add_edge(4, 8)
g.add_edge(8, 7)
g.add_edge(7, 4)
#6
g.add_edge(4, 5)
g.add_edge(5, 8)
g.add_edge(8, 4)
#7
g.add_edge(5, 9)
g.add_edge(9, 8)
g.add_edge(8, 5)
#8
g.add_edge(5, 6)
g.add_edge(6, 9)
g.add_edge(9, 5)
for node in g.nodes():
    x, y = g.node[node]['XY']
    print(x, y)