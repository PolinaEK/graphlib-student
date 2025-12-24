from graphlib import Graph, dijkstra, draw_graph

# Создаём граф
g = Graph()
g.add_edge("A", "B", 1)
g.add_edge("B", "C", 2)
g.add_edge("A", "C", 5)
g.add_edge("C", "D", 1)

print("Соседи A:", g.neighbors("A"))
print("Вес ребра A→B:", g.get_weight("A", "B"))

# Проверяем алгоритм Дейкстры
distances = dijkstra(g, "A")
print("Кратчайшие расстояния от A:", distances)

# Проверяем визуализацию
print("Откроется окно с графом...")
draw_graph(g)