import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
A, B = map(int, input().split())
answer = -1
def bfs(now , count):
    global answer
    if now == B:
        answer = count
        return
    if now > B:
        return

    bfs(now * 10 + 1, count +1)
    bfs(now * 2, count +1)

bfs(A, 1)
print(answer)