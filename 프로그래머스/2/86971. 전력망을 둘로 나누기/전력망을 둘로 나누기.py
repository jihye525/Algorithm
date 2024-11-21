from collections import deque

def bfs(start, n, graph):
    queue = deque([start])
    cnt = 1
    # 시작 노드 방문 처리
    visited = [0 for _ in range(n+1)]
    visited[start] = True

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            #가보지 않은 노드의 경우
            if visited[i] == False:
                cnt += 1 # 노드 cnt +1
                queue.append(i) #큐에 추가
                visited[i] = True # 방문 처리
    return cnt

def solution(n, wires):
    answer = float("inf")
    graph = [[] for _ in range(n+1)] # 그래프 생성

    # wires를 순회하며 그래프 연결
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 노드 하나씩 끊어보기
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        answer = min(abs(bfs(v1, n, graph) - bfs(v2, n, graph)), answer)

        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer