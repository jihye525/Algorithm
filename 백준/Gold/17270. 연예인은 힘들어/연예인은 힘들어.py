import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distances = [INF] * (v + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for next_node, next_weight in graph[current_node]:
            distance = current_distance + next_weight
            if current_distance + next_weight < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances


v, m = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

j, s = map(int, input().split())

j_dist = dijkstra(j)
s_dist = dijkstra(s)
min_dis = INF
result = []

for i in range(1, v+1):
    if i == j or i == s:
        continue

    if j_dist[i] + s_dist[i] < min_dis:
        result = []
        min_dis = j_dist[i] + s_dist[i]

    if j_dist[i] + s_dist[i] == min_dis and j_dist[i] <= s_dist[i]:
        result.append([min_dis, j_dist[i], i])

result.sort(key=lambda x: (x[1]))
print(result[0][2] if result else -1)