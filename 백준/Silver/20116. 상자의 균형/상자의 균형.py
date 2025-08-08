import sys
input = sys.stdin.readline

n, l = map(int, input().split())
x_lst = list(map(int, input().split()))
sum_lst = x_lst[:]
for i in range(n-2, 0, -1):
    sum_lst[i] = sum_lst[i] + sum_lst[i+1]

def is_unstable(x_lst):
    for i in range(1, n):
        left_end = x_lst[-i - 1] - l
        right_end = x_lst[-i - 1] + l

        centers_x = sum_lst[n-i] / i
        if centers_x <= left_end or right_end <= centers_x:
            return True

    return False

if is_unstable(x_lst):
    print("unstable")
else:
    print("stable")
