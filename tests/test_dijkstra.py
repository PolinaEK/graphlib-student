from graphlib.data.graph import Graph
from graphlib.algorithms.dijkstra import dijkstra

def test_dijkstra():
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 2)
    g.add_edge("A", "C", 5)

    dist = dijkstra(g, "A")

    assert dist["C"] == 3
    assert dist["B"] == 1

    print("Dijkstra tests passed!")