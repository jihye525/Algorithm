import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
video = [list(input().rstrip()) for _ in range(n)]

def dfs(r, c, size):
    first = video[r][c]
    same = True
    for i in range(r, r + size):
        for j in range(c, c + size):
            if video[i][j] != first:
                same = False
                break
        if not same:
            break
    
    if same:
        answer.append(first)
        return
    
    half = size // 2
    answer.append("(")
    dfs(r, c, half)                  
    dfs(r, c + half, half)           
    dfs(r + half, c, half)           
    dfs(r + half, c + half, half)    
    answer.append(")")

answer = []
dfs(0, 0, n)
print("".join(answer))