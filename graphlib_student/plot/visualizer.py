import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph):
    G = nx.DiGraph()
    for (u, v), w in graph.weights.items():
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()