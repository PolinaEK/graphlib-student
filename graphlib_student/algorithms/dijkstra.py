import heapq

def dijkstra(graph, start):
    # Собираем все вершины: и те, у кого есть рёбра, и те, к кому идут рёбра
    all_nodes = set(graph.edges.keys())
    for u in graph.edges:
        all_nodes.update(graph.neighbors(u))

    distances = {node: float('inf') for node in all_nodes}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        dist, node = heapq.heappop(queue)

        if dist > distances[node]:
            continue

        for neighbor in graph.neighbors(node):
            weight = graph.get_weight(node, neighbor)
            new_dist = dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))


    return distances