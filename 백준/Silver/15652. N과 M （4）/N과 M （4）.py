n, m = map(int, input().split())


def dfs(i, now, ans):
    if now == m:
        print(*ans)
        return

    for idx in range(i, n + 1):
        dfs(idx, now + 1, ans + [idx])


dfs(1, 0, [])