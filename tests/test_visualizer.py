from graphlib.data.graph import Graph
from graphlib.plot.visualizer import draw_graph

def test_visualizer():
    g = Graph()
    g.add_edge("X", "Y", 2)
    g.add_edge("Y", "Z", 3)

    draw_graph(g)

    print("Visualizer test passed!")