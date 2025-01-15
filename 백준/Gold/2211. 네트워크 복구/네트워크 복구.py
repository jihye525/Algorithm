import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한대를 표현할 변수 INF 설정


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)  # 가장 거리가 짧은 노드 선택

        if distance[now] < dist:  # 이미 처리된 노드는 스킵
            continue

        for next_node, next_cost in graph[now]:
            # 현재 노드와 연결된 노드들에 대해
            # 시작 노드에서 현재 노드까지의 거리에 연결된 노드까지의 거리를 더함
            cost = dist + next_cost

            if distance[next_node] > cost:
                # 기존에 저장된 거리보다 새로 계산된 거리가 더 짧다면
                # 부모노드를 현재 노드로 갱신하고 거리를 갱신
                parent[next_node] = now
                distance[next_node] = cost

                # 우선순위 큐에 추가하여 다음 노드로 탐색 진행
                heapq.heappush(q, (cost, next_node))


n, m = map(int, input().split())

distance = [INF] * (n + 1)
parent = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향 그래프이므로 각 노드에 연결된 노드와 가중치를 추가
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)  # 다익스트라 알고리즘을 시작 노드를 1로 하여 실행

print(n - 1)
for i in range(2, n + 1):
    print(i, parent[i])