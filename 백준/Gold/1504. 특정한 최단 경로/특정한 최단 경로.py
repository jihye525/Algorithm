import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    distances = [INF] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if distances[current_node] < current_cost:
            continue

        for next_node, next_weight in graph[current_node]:
            distance = current_cost + next_weight
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances[end]


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

shortest = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n))
print(shortest if shortest < INF else -1)
