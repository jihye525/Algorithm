# N = int(input())
# s = 0
# cnt = 0
# for i in range(1, N):
#     s += i
#     cnt += 1
#     if s > N:
#         s -= i
#         cnt -= 1
#     if s == N:
#         break
#
# print(cnt)

t = int(input())


def find(a, b, result):
    disjoint_chk = 1
    if a == 1 or b == 1:
        print(result * a * b)
        return

    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            find(a // i, b // i, result * i)
            disjoint_chk = 0
            break

    if disjoint_chk:
        print(result * a * b)
        return

for _ in range(t):
    n1, n2 = map(int, input().split())
    find(n1, n2, 1)








