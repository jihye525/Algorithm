N = int(input())

def dfs(n):
    if n == 1:
        return

    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            dfs(n//i)
            break

dfs(N)