def solution(info, edges):
    answer = []
    trees = [[] for _ in range(len(info))]
    for parent, child in edges:
        trees[parent].append(child)

    def follow_me(node, sheep, wolves, next_lst):
        if sheep <= wolves:
            return

        answer.append(sheep)

        for i in range(len(next_lst)):
            next_node = next_lst[i]
            
            next_visit = next_lst[:i]+next_lst[i+1:] + trees[next_node]


            if info[next_node]:
                follow_me(next_node, sheep, wolves + 1, next_visit)
            else:
                follow_me(next_node, sheep + 1, wolves, next_visit)

    follow_me(0, 1, 0, trees[0])

    return max(answer)