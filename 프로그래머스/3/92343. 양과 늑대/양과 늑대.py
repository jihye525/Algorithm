def solution(info, edges):
    answer = []
    visited_lst = [False] * (len(info))
    trees = [[] for _ in range(len(info))]
    for parent, child in edges:
        trees[parent].append(child)

    def follow_me(node, sheep, wolves, next_lst, visited):
        if sheep <= wolves:
            return

        answer.append(sheep)

        for i in range(len(next_lst)-1, -1, -1):
            next_node = next_lst[i]
            if not visited[next_node]:
                next_visit = next_lst[:]
                next_visit.remove(next_node)
                next_visit += trees[next_node][:]
                next_visited = visited[:]
                next_visited[next_node] = True

                if info[next_node]:
                    next_wolves = wolves + 1
                    follow_me(next_node, sheep, next_wolves, next_visit, next_visited)
                else:
                    next_sheep = sheep + 1
                    follow_me(next_node, next_sheep, wolves, next_visit, next_visited)

    visited_lst[0] = True
    follow_me(0, 1, 0, trees[0][:], visited_lst)

    return max(answer)