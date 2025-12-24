from graphlib.data.graph import Graph

def test_graph():
    g = Graph()
    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 1)

    assert g.neighbors("A") == ["B", "C"]
    assert g.get_weight("A", "B") == 3
    assert g.get_weight("A", "C") == 1

    print("Graph tests passed!")