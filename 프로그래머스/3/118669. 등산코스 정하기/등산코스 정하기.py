from collections import deque

def solution(n, paths, gates, summits):
    road = [[] for _ in range(n + 1)]
    summits = set(summits)
    gates = set(gates)
    
    for p in paths:
        a, b, c = p
        if a in gates or b in summits:
            road[a].append([b, c])
        elif a in summits or b in gates:
            road[b].append([a, c])
        else:
            road[a].append([b, c])
            road[b].append([a, c])

    queue = deque()
    intensity = [10000001] * (n + 1)

    for g in gates:
        queue.append([g, 0])

    while queue:
        curr, curr_t = queue.popleft()
        if curr in summits:
            continue
        
        if intensity[curr] < curr_t:
            continue

        for next_node, next_w in road[curr]:
            if intensity[next_node] > max(curr_t, next_w):
                intensity[next_node] = max(curr_t, next_w)
                queue.append([next_node, intensity[next_node]])

    ans = [0, 10000001]
    summits = sorted(list(summits))
    for s in summits:
        if ans[1] > intensity[s]:
            ans = [s, intensity[s]]
            
    return ans